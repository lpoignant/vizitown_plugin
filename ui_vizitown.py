# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_vizitown.ui'
#
# Created: Tue Apr 22 11:26:28 2014
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Vizitown(object):
    def setupUi(self, Vizitown):
        Vizitown.setObjectName(_fromUtf8("Vizitown"))
        Vizitown.setEnabled(True)
        Vizitown.resize(482, 555)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("vt.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Vizitown.setWindowIcon(icon)
        self.verticalLayout_2 = QtGui.QVBoxLayout(Vizitown)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.tabWidget = QtGui.QTabWidget(Vizitown)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.Layers = QtGui.QWidget()
        self.Layers.setObjectName(_fromUtf8("Layers"))
        self.gridLayout_2 = QtGui.QGridLayout(self.Layers)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.groupBox_3 = QtGui.QGroupBox(self.Layers)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox_3)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tw_layers = QtGui.QTableWidget(self.groupBox_3)
        self.tw_layers.setAlternatingRowColors(True)
        self.tw_layers.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tw_layers.setColumnCount(3)
        self.tw_layers.setObjectName(_fromUtf8("tw_layers"))
        self.tw_layers.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tw_layers.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tw_layers.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tw_layers.setHorizontalHeaderItem(2, item)
        self.tw_layers.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout.addWidget(self.tw_layers)
        self.gridLayout_3.addLayout(self.verticalLayout, 0, 2, 1, 2)
        self.gridLayout_2.addWidget(self.groupBox_3, 2, 0, 1, 1)
        self.groupBox = QtGui.QGroupBox(self.Layers)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.cb_dem = QtGui.QComboBox(self.groupBox)
        self.cb_dem.setObjectName(_fromUtf8("cb_dem"))
        self.horizontalLayout.addWidget(self.cb_dem)
        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)
        self.groupBox_2 = QtGui.QGroupBox(self.Layers)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.cb_texture = QtGui.QComboBox(self.groupBox_2)
        self.cb_texture.setObjectName(_fromUtf8("cb_texture"))
        self.horizontalLayout_2.addWidget(self.cb_texture)
        self.gridLayout_2.addWidget(self.groupBox_2, 1, 0, 1, 1)
        self.tabWidget.addTab(self.Layers, _fromUtf8(""))
        self.Opt = QtGui.QWidget()
        self.Opt.setObjectName(_fromUtf8("Opt"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.Opt)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.groupBox_4 = QtGui.QGroupBox(self.Opt)
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_7 = QtGui.QLabel(self.groupBox_4)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_3.addWidget(self.label_7)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.sb_port = QtGui.QSpinBox(self.groupBox_4)
        self.sb_port.setMinimum(1024)
        self.sb_port.setMaximum(65536)
        self.sb_port.setObjectName(_fromUtf8("sb_port"))
        self.horizontalLayout_3.addWidget(self.sb_port)
        self.verticalLayout_3.addWidget(self.groupBox_4)
        self.groupBox_5 = QtGui.QGroupBox(self.Opt)
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox_5)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_8 = QtGui.QLabel(self.groupBox_5)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout.addWidget(self.label_8, 0, 0, 1, 1)
        self.cb_tile = QtGui.QComboBox(self.groupBox_5)
        self.cb_tile.setObjectName(_fromUtf8("cb_tile"))
        self.gridLayout.addWidget(self.cb_tile, 0, 1, 1, 1)
        self.verticalLayout_3.addWidget(self.groupBox_5)
        self.btn_default = QtGui.QPushButton(self.Opt)
        self.btn_default.setObjectName(_fromUtf8("btn_default"))
        self.verticalLayout_3.addWidget(self.btn_default)
        self.tabWidget.addTab(self.Opt, _fromUtf8(""))
        self.extent = QtGui.QWidget()
        self.extent.setMinimumSize(QtCore.QSize(452, 0))
        self.extent.setObjectName(_fromUtf8("extent"))
        self.gridLayout_4 = QtGui.QGridLayout(self.extent)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.label_14 = QtGui.QLabel(self.extent)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.gridLayout_4.addWidget(self.label_14, 2, 2, 1, 1)
        self.lb_width = QtGui.QSpinBox(self.extent)
        self.lb_width.setReadOnly(True)
        self.lb_width.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.lb_width.setMinimum(-999999999)
        self.lb_width.setMaximum(999999999)
        self.lb_width.setObjectName(_fromUtf8("lb_width"))
        self.gridLayout_4.addWidget(self.lb_width, 14, 4, 1, 1)
        self.label = QtGui.QLabel(self.extent)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_4.addWidget(self.label, 13, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem1, 15, 2, 1, 1)
        self.le_ymax = QtGui.QDoubleSpinBox(self.extent)
        self.le_ymax.setObjectName(_fromUtf8("le_ymax"))
        self.gridLayout_4.addWidget(self.le_ymax, 3, 2, 1, 1)
        self.label_2 = QtGui.QLabel(self.extent)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_4.addWidget(self.label_2, 14, 0, 1, 1)
        self.lb_height = QtGui.QSpinBox(self.extent)
        self.lb_height.setReadOnly(True)
        self.lb_height.setButtonSymbols(QtGui.QAbstractSpinBox.NoButtons)
        self.lb_height.setMinimum(-999999999)
        self.lb_height.setMaximum(999999999)
        self.lb_height.setObjectName(_fromUtf8("lb_height"))
        self.gridLayout_4.addWidget(self.lb_height, 13, 4, 1, 1)
        self.le_xmin = QtGui.QDoubleSpinBox(self.extent)
        self.le_xmin.setObjectName(_fromUtf8("le_xmin"))
        self.gridLayout_4.addWidget(self.le_xmin, 5, 0, 1, 1)
        self.le_xmax = QtGui.QDoubleSpinBox(self.extent)
        self.le_xmax.setObjectName(_fromUtf8("le_xmax"))
        self.gridLayout_4.addWidget(self.le_xmax, 5, 4, 1, 1)
        self.label_12 = QtGui.QLabel(self.extent)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.gridLayout_4.addWidget(self.label_12, 6, 2, 1, 1)
        self.le_ymin = QtGui.QDoubleSpinBox(self.extent)
        self.le_ymin.setObjectName(_fromUtf8("le_ymin"))
        self.gridLayout_4.addWidget(self.le_ymin, 7, 2, 1, 1)
        self.label_11 = QtGui.QLabel(self.extent)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.gridLayout_4.addWidget(self.label_11, 4, 0, 1, 1)
        self.label_13 = QtGui.QLabel(self.extent)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.gridLayout_4.addWidget(self.label_13, 4, 4, 1, 1)
        self.line = QtGui.QFrame(self.extent)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.gridLayout_4.addWidget(self.line, 10, 2, 1, 1)
        self.tabWidget.addTab(self.extent, _fromUtf8(""))
        self.verticalLayout_2.addWidget(self.tabWidget)
        self.pb_loading = QtGui.QProgressBar(Vizitown)
        self.pb_loading.setMaximum(0)
        self.pb_loading.setProperty("value", -1)
        self.pb_loading.setTextVisible(False)
        self.pb_loading.setObjectName(_fromUtf8("pb_loading"))
        self.verticalLayout_2.addWidget(self.pb_loading)
        spacerItem2 = QtGui.QSpacerItem(20, 55, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.btn_generate = QtGui.QPushButton(Vizitown)
        self.btn_generate.setObjectName(_fromUtf8("btn_generate"))
        self.verticalLayout_2.addWidget(self.btn_generate)

        self.retranslateUi(Vizitown)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Vizitown)

    def retranslateUi(self, Vizitown):
        Vizitown.setWindowTitle(_translate("Vizitown", "Vizitown", None))
        self.groupBox_3.setTitle(_translate("Vizitown", "Vector", None))
        self.tw_layers.setSortingEnabled(True)
        item = self.tw_layers.horizontalHeaderItem(0)
        item.setText(_translate("Vizitown", "Display", None))
        item = self.tw_layers.horizontalHeaderItem(1)
        item.setText(_translate("Vizitown", "Layer", None))
        item = self.tw_layers.horizontalHeaderItem(2)
        item.setText(_translate("Vizitown", "Field", None))
        self.groupBox.setTitle(_translate("Vizitown", "DEM", None))
        self.groupBox_2.setTitle(_translate("Vizitown", "Texture", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Layers), _translate("Vizitown", "Layers", None))
        self.groupBox_4.setTitle(_translate("Vizitown", "Server", None))
        self.label_7.setText(_translate("Vizitown", "Port number", None))
        self.groupBox_5.setTitle(_translate("Vizitown", "Scene", None))
        self.label_8.setText(_translate("Vizitown", "Tile size", None))
        self.btn_default.setText(_translate("Vizitown", "By default", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Opt), _translate("Vizitown", "Preferences", None))
        self.label_14.setText(_translate("Vizitown", "Ymax", None))
        self.lb_width.setSuffix(_translate("Vizitown", " km", None))
        self.label.setText(_translate("Vizitown", "Height :", None))
        self.label_2.setText(_translate("Vizitown", "Width :", None))
        self.lb_height.setSuffix(_translate("Vizitown", " km", None))
        self.label_12.setText(_translate("Vizitown", "Ymin", None))
        self.label_11.setText(_translate("Vizitown", "Xmin", None))
        self.label_13.setText(_translate("Vizitown", "Xmax", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.extent), _translate("Vizitown", "Extent", None))
        self.btn_generate.setText(_translate("Vizitown", "Generate", None))

