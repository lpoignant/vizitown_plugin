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
import sys
import os
import json
import logging
from multiprocessing import Queue

sys.path.insert(0, os.path.dirname(__file__))
from cyclone.websocket import WebSocketHandler
from cyclone.web import StaticFileHandler, RequestHandler
sys.path.pop(0)

import core

from vt_as_sync import SyncManager
from vt_utils_result_vttiler import ResultVTTiler


## Class CorsStaticFileHandler
#  A static file handler which authorize cross origin
#  Unherited cyclone.web.StaticFileHandler
class CorsStaticFileHandler(StaticFileHandler):

    ## set_default_headers method
    #  Define the headers for the default handler
    #  @override cyclone.web.StaticFileHandler
    def set_default_headers(self):
        self.set_header('Access-Control-Allow-Origin', '*')
        self.set_header('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
        self.set_header('Access-Control-Allow-Headers', 'X-Requested-With')


## Class InitHandler
#  A handler give initial parameters to the browser
#  Unherited cyclone.web.RequestHandler
class InitHandler(RequestHandler):

    ## initialize method
    #  Initialize the handler for the init parameter
    #  @override cyclone.web.RequestHandler
    def initialize(self):
        logging.getLogger('Vizitown').info("Initialize init message")
        self.scene = core.Scene.instance()

    ## set_default_headers method
    #  Define the headers for the default handler
    #  @override cyclone.web.RequestHandler
    def set_default_headers(self):
        self.set_header('Access-Control-Allow-Origin', '*')
        self.set_header('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
        self.set_header('Access-Control-Allow-Headers', 'X-Requested-With')

    ## get method
    #  Handle GET HTTP
    #  @override cyclone.web.RequestHandler
    def get(self):
        self.write(json.dumps(self.scene.get_viewer_param(), separators=(',', ':')))


## Class Data Handler
#  Use to handle the transmission of the data
#  retreived from postgis to the web browser
#  Unherited cyclone.websocket.WebSocketHandler
class DataHandler(WebSocketHandler):
    UUID = "uuid"

    ## connectionMade method
    #  Method call when the websocket is opened
    #  @override cyclone.websocket.WebSocketHandler
    def connectionMade(self):
        self.logger = logging.getLogger('Vizitown')
        self.scene = core.Scene.instance()
        self.logger.info("WebSocket data opened")

    ## messageReceived method
    #  Method call when a message is received
    #  Request all content in the extent specified in the message
    #  @param message in JSON format like:
    #   '{"Xmin": 0, "Ymin": 0, "Xmax": 50, "Ymax": 50}' for request all vectors
    #   '{"Xmin": 0, "Ymin": 0, "Xmax": 50, "Ymax": 50, uuid: "my_uuid"}' for a request only a specific vector
    #  @override cyclone.websocket.WebSocketHandler
    def messageReceived(self, message):
        self.logger.debug("Received message -> " + message)

        # Keep alive connection
        if message == "ping":
            self.sendMessage("pong")
            self.logger.debug("Send pong to keep alive connection")
            return

        json_tile = json.loads(message)
        dictionary = dict(**json_tile)
        if self.UUID in dictionary:
            uuid = dictionary[self.UUID]
            del dictionary[self.UUID]
        else:
            uuid = None

        tile = core.Tile(**dictionary)
        provider_manager = self.scene.providerManager
        tiles = provider_manager.request_tile(tile, uuid)

        for tile in tiles:
            for part in tile:
                self.sendMessage(json.dumps(part, separators=(',', ': ')))

    ## connectionLost method
    #  Method call when the websocket is closed
    #  @param reason to indicate the reason of the closed instance
    #  @override cyclone.websocket.WebSocketHandler
    def connectionLost(self, reason):
        self.logger.info("WebSocket data closed")


## Synchronisation Handler
#  Use to handle the synchronisation of the view
#  from QGIS to the web browser
#  Unherited cyclone.websocket.WebSocketHandler
class SyncHandler(WebSocketHandler):

    ## initialize method
    #  Method to initialize the handler
    #  @override cyclone.websocket.WebSocketHandler
    def initialize(self):
        self.logger = logging.getLogger('Vizitown')
        self.logger.info("Initialize websocket sync")
        SyncManager.instance().add_listener(self)

    ## connectionMade method
    #  Method call when the websocket is opened
    #  @override cyclone.websocket.WebSocketHandler
    def connectionMade(self):
        self.logger.info("WebSocket sync opened")

    ## meassageReceived method
    #  Method call when a message is received
    #  @param message received
    #  @override cyclone.websocket.WebSocketHandler
    def messageReceived(self, message):
        self.logger.debug("Received message -> " + message)
        # Keep alive connection
        if message == "ping":
            self.sendMessage("pong")
            return
        pass  # Do nothing, simplex communication

    ## connectionLost method
    #  Method call when the websocket is closed
    #  @param reason to indicate the reason of the closed instance
    #  @override cyclone.websocket.WebSocketHandler
    def connectionLost(self, reason):
        self.logger.info("WebSocket sync closed")

    ## on_finish method
    #  Method remove the listener
    #  @override cyclone.websocket.WebSocketHandler
    def on_finish(self):
        self.logger.info("WebSocket finished")
        SyncManager.instance().remove_listener(self)


## Tiles information handler
#  Use to give the information related to the tiles generated
#  when the GDAL tiling is finished
#  Unherited cyclone.websocket.WebSocketHandler
class TilesInfoHandler(WebSocketHandler):

    ## initialize method
    #  Method to initialize the handler
    #  @override cyclone.websocket.WebSocketHandler
    def initialize(self):
        self.logger = logging.getLogger('Vizitown')
        self.logger.info("Initialize Tiles Info WebSocket")
        self.scene = core.Scene.instance()
        self.result = ResultVTTiler.instance()

    ## connectionMade method
    #  Method call when the websocket is opened
    #  @override cyclone.websocket.WebSocketHandler
    def connectionMade(self):
        self.logger.info("WebSocket tiles_info opened")

        if not self.result.is_define():
            self.result.set_result(self.scene.GDALqueue.get())
            self.scene.GDALqueue.close()
            self.scene.GDALprocess.terminate()

        if self.scene.GDALprocess and self.scene.GDALprocess.is_alive():
            self.logger.info("Wait GDAL tiling ...")
            self.scene.GDALprocess.join()
            self.logger.info("Send tiles info ...")

        tilesInfo = self.scene.get_tiling_param()
        # Add pixel Size in JSON and Min/Max height if have dem
        if self.result.is_define():
            tilesInfo['pixelSize'] = self.result.pixelSize
            if self.result.is_dem():
                tilesInfo['minHeight'] = self.result.minHeight
                tilesInfo['maxHeight'] = self.result.maxHeight

        js = json.dumps(tilesInfo, separators=(',', ':'))
        self.logger.debug("Send message tilesInfo -> " + js)
        self.sendMessage(js)

    ## connectionLost method
    #  Method call when the websocket is closed
    #  @param reason to indicate the reason of the closed instance
    #  @override cyclone.websocket.WebSocketHandler
    def connectionLost(self, reason):
        self.logger.info("WebSocket tiles_info closed")
