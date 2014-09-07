# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Vizitown
                                 A QGIS plugin
 QGIS Plugin for viewing data in 3D
                              -------------------
        begin                : 2014-02-03
        copyright            : (C) 2014 by Cubee(ESIPE)
        email                : lp_vizitown@googlegroups.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
import os
import sys
import shutil
import multiprocessing as mp

import core

from vt_utils_tiler import VTTiler, Extent
from vt_as_provider_raster import RasterProvider


## Class ProviderFactory
#  Create the provider in function of the data
class ProviderFactory():

    ## Constructor
    def __init__(self):
        self.scene = core.Scene.instance()
        self.providerManager = self.scene.providerManager

    ## create_raster_providers method
    #  Create all providers for DEM and raster
    #  @param dem the Data Elevation Model
    #  @param texture the texture image
    def create_raster_providers(self, dem, texture):
        dataSrcImg = None
        dataSrcMnt = None
        extent = self.scene.extent
        originExtent = Extent(extent[0], extent[1], extent[2], extent[3])
        tileSize = self.scene.tileSize
        zoomLevel = self.scene.zoomLevel
        path = self.scene.rastersPath
        if dem is not None:
            demProvider = RasterProvider(dem)
            dataSrcMnt = demProvider.source
            self.scene.set_resources_dem(demProvider.httpResource)
            self.providerManager.dem = demProvider
        if texture is not None:
            textureProvider = RasterProvider(texture)
            dataSrcImg = textureProvider.source
            self.scene.set_resources_texture(textureProvider.httpResource)
            self.providerManager.texture = textureProvider

        if os.name == 'nt':
            pythonPath = os.path.abspath(os.path.join(sys.exec_prefix, '../../bin/pythonw.exe'))
            mp.set_executable(pythonPath)
            sys.argv = [None]

        self.clear_rasters_directory(self.scene.rastersPath)
        tiler = VTTiler(originExtent, tileSize, zoomLevel, dataSrcMnt, dataSrcImg)
        self.scene.GDALprocess = mp.Process(target=tiler.create, args=(path, self.scene.GDALqueue))
        self.scene.GDALprocess.start()

    ## clear_rasters_directory method
    #  Clean the rasters directory where the tile of data image are created
    #  @path the path to the repository
    def clear_rasters_directory(self, path):
        for root, dirs, files in os.walk(path, topdown=False):
            for name in dirs:
                shutil.rmtree(os.path.join(root, name))
