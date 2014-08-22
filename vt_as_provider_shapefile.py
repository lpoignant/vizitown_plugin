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
import json

from qgis.core import QgsRectangle, QgsFeatureRequest

## Postgis provider
#  Stock the attribute to use a postgis resource
class ShapefileProvider:

    ## Constructor
    #  @param _layer
    def __init__(self, layer):
        self._layer = layer
        self.geometry1 = None
        self.geometry2 = None
        self.retGeometry = layer.qgisLayer.geometryType() # Point, Line or Polygon
        self.hasH = False

        if self._layer._column2 is not None:
            self.hasH = True
        else:
            self.hasH = False

    ## request_tile method
    #  Return all the result contains in the extent in param
    #  @param Xmin
    #  @param Ymin
    #  @param Xmax
    #  @param Ymax
    #  @return the tile
    def request_tile(self, Xmin, Ymin, Xmax, Ymax):
        # j = 0
        rect = QgsRectangle(Xmin, Ymin, Xmax, Ymax)
        features = self._layer.qgisLayer.getFeatures(QgsFeatureRequest().setFilterRect(rect))

        colors = self._color_array()

        results = self._sort_result(features)

        #for feature in features:
        #    print feature.geometry().exportToWkt()
        #    if self.hasH :
        #        print feature.attribute(self._layer._column2)
        #return None
        return {'results': results, 'geom': self.retGeometry, 'hasH': self.hasH, 'color': colors, 'uuid': self._layer._uuid}

    ## sort_result method
    #  Sort the request result in function of the type of symbology apply on the data
    #  @param iterator
    #  @return the table with the data and associated symbol
    def _sort_result(self, fiterator):
        colorType = self._layer.get_color_type()
        if (colorType == "singleSymbol"):
            return self._get_result_single_symbol(fiterator)

        elif (colorType == "graduatedSymbol"):
            return self._get_result_graduated_symbol(fiterator)

        elif (colorType == "categorizedSymbol"):
            return self._get_result_categorized_symbol(fiterator)

## _get_result_single_symbol method
    #  Run through the iterator to check the associated symbol
    #  @param iterator
    #  @return the table with the data and associated symbol
    def _get_result_single_symbol(self, fiterator):
        array = [[]]
        print "Single Symbol"

        for f in fiterator:
            if self.hasH:
                print f.geometry().exportToGeoJSON()
                _json = json.loads(f.geometry().exportToGeoJSON())
                print _json
                print f.attribute(self._layer._column2)
                return
                #array[0].append([f.geometry().exportToWkt(), f.attribute(self._layer._column2)])
            else:
                print f.geometry().exportToWkt()
                #array[0].append(f.geometry.exportToWkt())
        return array

    ## _get_result_graduated_symbol method
    #  Run through the iterator to check the associated symbol and sorted it
    #  @param iterator
    #  @return the table with the data and associated symbol
    def _get_result_graduated_symbol(self, fiterator):
        nbColor = len(self._layer._color)
        array = [[] for i in range(nbColor)]

        while iterator.next():
            for i in range(nbColor):
                if self.hasH:
                    if (iterator.value(2) > self._layer._color[i]['min'] and
                            iterator.value(2) <= self._layer._color[i]['max']):
                        array[i].append([iterator.value(0), iterator.value(1)])
                else:
                    if (iterator.value(1) > self._layer._color[i]['min'] and
                            iterator.value(1) <= self._layer._color[i]['max']):
                        array[i].append(iterator.value(0))
        return array

    ## _get_result_categorized_symbol method
    #  Run through the iterator to check the associated symbol and sorted it
    #  @param iterator
    #  @return the table with the data and associated symbol
    def _get_result_categorized_symbol(self, iterator):
        nbColor = len(self._layer._color)
        array = [[] for i in range(nbColor)]

        while iterator.next():
            for i in range(nbColor):
                if self.hasH:
                    if iterator.value(2) == self._layer._color[i]['value']:
                        array[i].append([iterator.value(0), iterator.value(1)])
                else:
                    if iterator.value(1) == self._layer._color[i]['value']:
                        array[i].append(iterator.value(0))
        return array

    ## _get_request method
    #  Send a request to catch the type of the data
    #  @return the request
    def _get_request(self, pExtent):
        return None

    ## _request_point_line method
    #  Request point or line data
    #  @return the request for data point or line
    def _request_point_line(self, pExtent):
        return None

    ## _request_polygon method
    #  Request polygon data
    #  @return the request for data polygon
    def _request_polygon(self, pExtent):
        return None

    ## _request_polyh method
    #  Request polyhedral data
    #  @return the request for data polyhedral
    def _request_polyh(self, pExtent):
        return None

    ## _request_tin
    #  Request tin data
    #  @return the request for data tin
    def _request_tin(self, pExtent):
        return None

    ## _color_array method
    #  Create an arry with all color of the layer
    #  @return the array
    def _color_array(self):
        array = []
        nbColor = len(self._layer._color)
        if nbColor == 1:
            array.append(self._layer._color[0]['color'])
            return array
        else:
            for i in range(nbColor):
                array.append(self._layer._color[i]['color'])
            return array

    ## get_columns_info_table static method
    #  Return columns and types of a specific table
    #  @param layer to access at the table
    #  @return the result of the request
    @staticmethod
    def get_columns_info_table(layer):
        attributes = layer.qgisLayer.pendingFields().toList()
        result = {}
        for a in attributes:
            result[a.name()] = a.typeName()
        return result