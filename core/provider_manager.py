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
import re
import logging

## Provider manager
class ProviderManager:

    ## Constructor
    def __init__(self):
        self.vectors = {}
        self.dem = None
        self.texture = None
        self.logger = logging.getLogger('Vizitown')

    ## add_vector_provider method
    #  Add a vector provider to the manager
    #  @param p the provider to add
    def add_vector_provider(self, p):
        self.vectors[p._vector._uuid] = p

    ## request_tile method
    #  Request a tile for all his providers
    #  @param Xmin
    #  @param Ymin
    #  @param Xmax
    #  @param Ymax
    #  @param uuid
    #  @return the tile
    def request_tile(self, tile, uuid=None):
        result = []
        if uuid is not None:
            result.append(self.vectors[uuid].request_tile(tile))
            return result

        for (uuid, p) in self.vectors.items():
            result.append(p.request_tile(tile))
        return result

    ## clear method
    #  clean all field of the provider to the manager
    def clear(self):
        self.vectors = {}
        self.dem = None
        self.texture = None

    ## add_rasters method
    #  Add a raster in demProvider or in textureProvider to the manager
    #  @param demProvider
    #  @param textureProvider
    def add_rasters(self, demProvider=None, textureProvider=None):
        self.dem = demProvider
        self.texture = textureProvider

    ## get_all_vectors method
    #  Access to all vector in the provider
    #  @return a list with the vectors uuid and name
    def get_all_vectors(self):
        vectors = []
        for (uuid, p) in self.vectors.items():
            vectors.append({'uuid': uuid, 'name': p._layer._displayName})
        return vectors
