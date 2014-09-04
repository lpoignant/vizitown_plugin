# -*- coding: utf-8 -*-
"""
    /***************************************************************************
    VizitownDialog
    A QGIS plugin
    2D to 3D
    -------------------
    begin                : 2014-01-09
    copyright            : (C) 2014 by Cubee(ESIPE)
    email                : vizitown@gmail.com
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
import webbrowser
import time
import logging

from ui_vizitown import Ui_Vizitown
from PyQt4 import QtCore, QtGui
from qgis.core import *
from qgis.gui import *

import core
import vectors

from vt_as_app import AppServer
from vt_as_sync import SyncManager
from vt_as_provider_manager import ProviderManager
from vt_utils_provider_factory import ProviderFactory


## Class VizitownDialog
#  Vizitown dialog in QGIS GUI and
#  Unherited QtGui.QDialog and Ui_Vizitown
class VizitownDialog(QtGui.QDialog, Ui_Vizitown):

    ## Constructor
    #  @param extent the initial extent
    def __init__(self, extent):
        QtGui.QDialog.__init__(self)
        self.logger = logging.getLogger('Vizitown')
        self.setupUi(self)
        self.destroyed.connect(self.closeEvent)
        self.appServer = None
        self.appServerRunning = False
        self.GDALprocess = None
        self.zoomLevel = "1"

        self.scene = core.Scene.instance()
        self.providerManager = ProviderManager.instance()

    ## init_extent method
    #  Set the default extent
    #  @param extent the extent to init the parameter
    def init_extent(self, extent):
        self.extent = extent
        self.set_limit_sb()
        self.le_xmin.setValue(extent.xMinimum())
        self.le_ymin.setValue(extent.yMinimum())
        self.le_xmax.setValue(extent.xMaximum())
        self.le_ymax.setValue(extent.yMaximum())
        self.calculate_size_extent()

    ## set_limit_sb method
    #  Set the limit of the doublespinbox in the tab extent
    def set_limit_sb(self):
        self.le_xmin.setMaximum(sys.maxint)
        self.le_xmin.setMinimum(-sys.maxint)
        self.le_ymin.setMaximum(sys.maxint)
        self.le_ymin.setMinimum(-sys.maxint)
        self.le_xmax.setMaximum(sys.maxint)
        self.le_xmax.setMinimum(-sys.maxint)
        self.le_ymax.setMaximum(sys.maxint)
        self.le_ymax.setMinimum(-sys.maxint)

    ## init_tile_size method
    #  Set the values of the tile by default
    def init_tile_size(self):
        self.cb_tile.clear()
        self.cb_tile.addItem('256 x 256')
        self.cb_tile.addItem('512 x 512')
        self.cb_tile.addItem('1024 x 1024')
        self.cb_tile.addItem('2048 x 2048')
        self.cb_tile.setCurrentIndex(2)

    ## init_layers method
    #  Init combobox and table layers
    def init_layers(self):
        self.reset_all_fields()
        layerListIems = QgsMapLayerRegistry().instance().mapLayers().items()
        factory = vectors.VectorProviderFactory()
        for id, qgisLayer in layerListIems:
            if qgisLayer.type() == QgsMapLayer.RasterLayer and qgisLayer.providerType() == "gdal":
                if qgisLayer.bandCount() == 1:
                    self.cb_dem.addItem(qgisLayer.name(), qgisLayer)

                if qgisLayer.bandCount() >= 3:
                    self.cb_texture.addItem(qgisLayer.name(), qgisLayer)

            if qgisLayer.type() == QgsMapLayer.VectorLayer:
                pvector = factory.create_provider(qgisLayer)

                columnInfoLayer = pvector.get_columns_info()
                item = QtGui.QTableWidgetItem(pvector._vector._display_name)
                item.setData(QtCore.Qt.UserRole, pvector)
                item.setFlags(QtCore.Qt.ItemIsEnabled)
                self.add_vector_layer(item, columnInfoLayer)

    ## reset_all_fields method
    #  Reset all widgets
    def reset_all_fields(self):
        self.cb_dem.clear()
        self.cb_texture.clear()
        self.cb_dem.addItem("None")
        self.cb_texture.addItem("None")
        self.tw_layers.setRowCount(0)
        self.tw_layers.setColumnWidth(0, 45)
        self.tw_layers.setColumnWidth(1, 150)
        self.pb_loading.hide()

    ## has_dem method
    #  Check if a dem is generate
    #  @return true if there is a DEM to generate
    def has_dem(self):
        return self.cb_dem.currentIndex() != 0

    ## has_texture method
    #  Check if a texture is generate
    #  @return true if there is a texture to generate
    def has_texture(self):
        return self.cb_texture.currentIndex() != 0

    ## has_raster method
    #  Check if a raster is generate
    #  @return true if there is a least one raster to generate
    def has_raster(self):
        return self.has_dem() or self.has_texture()

    ## has_vector method
    #  Check if a vector is existing
    #  @return true if there is a least one vector to exist
    def has_vector(self):
        for row_index in range(self.tw_layers.rowCount()):
            if self.tw_layers.item(row_index, 0).checkState() == QtCore.Qt.Checked:
                return True
        return False

    ## has_data method
    #  Check if a data is generate or existing
    #  @return true if there is a least one data to generate or exist
    def has_data(self):
        if self.has_raster() or self.has_vector():
            return True
        return False

    ## add_vector_layer method
    #  Add vector layer in QTableWidget
    #  @param item the new layer
    #  @param columnInfoLayer a dictionnary with the fields and their types
    def add_vector_layer(self, item, columnInfoLayer):
        self.tw_layers.insertRow(0)
        checkBox = QtGui.QTableWidgetItem()
        checkBox.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
        checkBox.setCheckState(QtCore.Qt.Unchecked)
        comboBox = QtGui.QComboBox()
        comboBox.addItem("None")
        for nameColumn, type in columnInfoLayer.items():
            comboBox.addItem(nameColumn + ' - ' + type)
        comboBox.model().sort(0)
        self.tw_layers.setItem(0, 0, checkBox)
        self.tw_layers.setItem(0, 1, item)
        self.tw_layers.setCellWidget(0, 2, comboBox)

    ## get_size_tile method
    #  Get the size tile selected by the user
    #  @return the size tile
    def get_size_tile(self):
        index = self.cb_tile.currentIndex()
        if index == 0:
            return 256
        if index == 1:
            return 512
        if index == 2:
            return 1024
        if index == 3:
            return 2048

    ## get_gui_extent method
    #  Get the extent specified in the GUI or if the fields filled by the user are incoherent it's the extent of current view of QGIS
    #  @return the extent
    def get_gui_extent(self):
        xmin = self.le_xmin.value()
        xmax = self.le_xmax.value()
        ymin = self.le_ymin.value()
        ymax = self.le_ymax.value()
        if float(xmin) < float(xmax) and float(ymin) < float(ymax):
            return [float(xmin), float(ymin), float(xmax), float(ymax)]
        return [float(self.extent.xMinimum()), float(self.extent.yMinimum()), float(self.extent.xMaximum()), float(self.extent.yMaximum())]

    ## set_selected_layers method
    #  Get all layers checked in the GUI and the associated informations
    #  @return the list of selected layers (layer is manipulate using his provider)
    def set_selected_vector_layers(self):
        selectedLayers = []
        for row_index in range(self.tw_layers.rowCount()):
            # if the layer is checked
            if self.tw_layers.item(row_index, 0).checkState() == QtCore.Qt.Checked:
                provider = self.tw_layers.item(row_index, 1).data(QtCore.Qt.UserRole)
                column2 = self.tw_layers.cellWidget(row_index, 2).currentText()
                if column2 != "None":
                    split = column2.split(" - ")
                    cname = split[0]
                    ctype = split[1]
                    provider._vector.define_column2(cname, ctype)
                selectedLayers.append(provider)
        return selectedLayers

    ## on_btn_default_released method
    #  Set the tab advanced option by default
    #  @override QtGui.QDialog
    def on_btn_default_released(self):
        self.sb_port.setValue(8888)
        self.cb_tile.setCurrentIndex(2)

    ## on_btn_generate_released method
    #  Generate and launch the rendering of the 3D scene
    #  @override QtGui.QDialog
    def on_btn_generate_released(self):
        if self.appServerRunning:
            self.closeEvent(None)
            return

        if not self.has_data():
            QtGui.QMessageBox.warning(self, "Warning", ("No data !"), QtGui.QMessageBox.Ok)
            return
        self.pb_loading.show()

        self.scene.set_viewer_param(self.get_gui_extent(), self.sb_port.value(), self.has_raster())
        self.scene.set_tiling_param(self.zoomLevel, self.get_size_tile())
        self.instantiate_providers()
        self.scene.set_all_vectors(self.set_selected_vector_layers())

        self.appServer = AppServer(self)
        self.appServer.start()
        self.btn_generate.setText("Server is running")
        self.appServerRunning = True

        # Little sleep to avoid launch of the webbrowser before the appserver start
        time.sleep(0.5)
        url = 'http://localhost:' + str(self.sb_port.value()) + '/app/index.html'
        webbrowser.open(url)

    ## instantiate_providers method
    #  Create providers in function of the existed data
    def instantiate_providers(self):
        factory = ProviderFactory()
        dem = None
        texture = None
        if self.has_raster():
            if self.has_dem():
                dem = self.cb_dem.itemData(self.cb_dem.currentIndex())
            if self.has_texture():
                texture = self.cb_texture.itemData(self.cb_texture.currentIndex())
            factory.create_raster_providers(dem, texture)

    ## calculate_size_extent method
    #  Calculate the width and the height in kilometers
    def calculate_size_extent(self):
        extent2 = self.get_gui_extent()
        width = extent2[2] - extent2[0]
        height = extent2[3] - extent2[1]
        self.lb_width.setValue(width / 1000)
        self.lb_height.setValue(height / 1000)

    ## closeEvent method
    #  Behavior whit a close event
    #  @override QtGui.QDialog
    #  @param QCloseEvent
    def closeEvent(self, QCloseEvent):
        if self.appServer:
            self.pb_loading.hide()
            self.btn_generate.setText("Server is stopping")
            self.appServer.stop()
            self.btn_generate.setText("Generate")
            self.appServerRunning = False
            SyncManager.instance().remove_all_listener()
            self.providerManager.clear()
            self.scene.clear()
