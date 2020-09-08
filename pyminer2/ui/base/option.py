# -*- coding: utf-8 -*-

# 不要再通过pyuic生成了，因为已经过人工的整理。
import qdarkstyle
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFileDialog, QWidget, QDesktopWidget

from pyminer2.pmutil import get_application, get_root_dir


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(705, 515)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.splitter = QtWidgets.QSplitter(Form)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.listWidget = QtWidgets.QListWidget(self.splitter)
        self.listWidget.setMaximumSize(QtCore.QSize(200, 16777215))
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.stackedWidget = QtWidgets.QStackedWidget(self.splitter)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_general = QtWidgets.QWidget()
        self.page_general.setObjectName("page_general")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.page_general)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.tabWidget = QtWidgets.QTabWidget(self.page_general)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setObjectName("tabWidget")
        self.tabBase = QtWidgets.QWidget()
        self.tabBase.setObjectName("tabBase")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.tabBase)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.label = QtWidgets.QLabel(self.tabBase)
        self.label.setObjectName("label")
        self.formLayout_2.setWidget(
            1, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_15 = QtWidgets.QLabel(self.tabBase)
        self.label_15.setObjectName("label_15")
        self.formLayout_2.setWidget(
            2, QtWidgets.QFormLayout.LabelRole, self.label_15)
        self.checkBox = QtWidgets.QCheckBox(self.tabBase)
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName("checkBox")
        self.formLayout_2.setWidget(
            5, QtWidgets.QFormLayout.LabelRole, self.checkBox)
        self.checkBox_2 = QtWidgets.QCheckBox(self.tabBase)
        self.checkBox_2.setObjectName("checkBox_2")
        self.formLayout_2.setWidget(
            7, QtWidgets.QFormLayout.LabelRole, self.checkBox_2)
        self.label_16 = QtWidgets.QLabel(self.tabBase)
        self.label_16.setObjectName("label_16")
        self.formLayout_2.setWidget(
            3, QtWidgets.QFormLayout.LabelRole, self.label_16)
        self.comboBox_9 = QtWidgets.QComboBox(self.tabBase)
        self.comboBox_9.setObjectName("comboBox_9")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.formLayout_2.setWidget(
            3, QtWidgets.QFormLayout.FieldRole, self.comboBox_9)
        self.label_11 = QtWidgets.QLabel(self.tabBase)
        self.label_11.setObjectName("label_11")
        self.formLayout_2.setWidget(
            4, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.comboBox_8 = QtWidgets.QComboBox(self.tabBase)
        self.comboBox_8.setObjectName("comboBox_8")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.formLayout_2.setWidget(
            4, QtWidgets.QFormLayout.FieldRole, self.comboBox_8)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.lineEdit_workspace = QtWidgets.QLineEdit(self.tabBase)
        self.lineEdit_workspace.setObjectName("lineEdit_workspace")
        self.horizontalLayout_14.addWidget(self.lineEdit_workspace)
        self.toolButton_workspace = QtWidgets.QToolButton(self.tabBase)
        self.toolButton_workspace.setObjectName("toolButton_workspace")
        self.horizontalLayout_14.addWidget(self.toolButton_workspace)
        self.formLayout_2.setLayout(
            1,
            QtWidgets.QFormLayout.FieldRole,
            self.horizontalLayout_14)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.lineEdit_output = QtWidgets.QLineEdit(self.tabBase)
        self.lineEdit_output.setObjectName("lineEdit_output")
        self.horizontalLayout_15.addWidget(self.lineEdit_output)
        self.toolButton_output = QtWidgets.QToolButton(self.tabBase)
        self.toolButton_output.setObjectName("toolButton_output")
        self.horizontalLayout_15.addWidget(self.toolButton_output)
        self.formLayout_2.setLayout(
            2,
            QtWidgets.QFormLayout.FieldRole,
            self.horizontalLayout_15)
        self.label_theme = QtWidgets.QLabel(self.tabBase)
        self.label_theme.setObjectName("label_theme")
        self.formLayout_2.setWidget(
            0, QtWidgets.QFormLayout.LabelRole, self.label_theme)
        self.comboBox_theme = QtWidgets.QComboBox(self.tabBase)
        self.comboBox_theme.setObjectName("comboBox_theme")
        self.comboBox_theme.addItem("")
        self.comboBox_theme.addItem("")
        self.comboBox_theme.addItem("")
        self.comboBox_theme.addItem("")
        self.formLayout_2.setWidget(
            0, QtWidgets.QFormLayout.FieldRole, self.comboBox_theme)
        self.checkBox_minitray = QtWidgets.QCheckBox(self.tabBase)
        self.checkBox_minitray.setChecked(True)
        self.checkBox_minitray.setObjectName("checkBox_minitray")
        self.formLayout_2.setWidget(
            6,
            QtWidgets.QFormLayout.LabelRole,
            self.checkBox_minitray)
        self.verticalLayout_8.addLayout(self.formLayout_2)
        spacerItem = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem)
        self.tabWidget.addTab(self.tabBase, "")
        self.horizontalLayout_3.addWidget(self.tabWidget)
        self.stackedWidget.addWidget(self.page_general)
        self.page_appearance = QtWidgets.QWidget()
        self.page_appearance.setObjectName("page_appearance")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.page_appearance)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.checkBox_3 = QtWidgets.QCheckBox(self.page_appearance)
        self.checkBox_3.setChecked(True)
        self.checkBox_3.setObjectName("checkBox_3")
        self.verticalLayout_5.addWidget(self.checkBox_3)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_10 = QtWidgets.QLabel(self.page_appearance)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_11.addWidget(self.label_10)
        self.pushButton = QtWidgets.QPushButton(self.page_appearance)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_11.addWidget(self.pushButton)
        spacerItem1 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem1)
        self.verticalLayout_5.addLayout(self.horizontalLayout_11)
        self.verticalLayout_6.addLayout(self.verticalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_6.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_3 = QtWidgets.QLabel(self.page_appearance)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_5.addWidget(self.label_3)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.page_appearance)
        self.lineEdit_2.setMaximumSize(QtCore.QSize(60, 16777215))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_5.addWidget(self.lineEdit_2)
        spacerItem2 = QtWidgets.QSpacerItem(
            120, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.verticalLayout_6.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.page_appearance)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.comboBox = QtWidgets.QComboBox(self.page_appearance)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.horizontalLayout_4.addWidget(self.comboBox)
        spacerItem3 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.verticalLayout_6.addLayout(self.horizontalLayout_4)
        self.textEdit = QtWidgets.QTextEdit(self.page_appearance)
        self.textEdit.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_6.addWidget(self.textEdit)
        self.stackedWidget.addWidget(self.page_appearance)
        self.page_interpreter = QtWidgets.QWidget()
        self.page_interpreter.setObjectName("page_interpreter")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.page_interpreter)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.page_interpreter)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.tab)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.tableWidget = QtWidgets.QTableWidget(self.tab)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.horizontalLayout_10.addWidget(self.tableWidget)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.pushButton_new = QtWidgets.QPushButton(self.tab)
        self.pushButton_new.setObjectName("pushButton_new")
        self.verticalLayout_4.addWidget(self.pushButton_new)
        self.pushButton_alter = QtWidgets.QPushButton(self.tab)
        self.pushButton_alter.setObjectName("pushButton_alter")
        self.verticalLayout_4.addWidget(self.pushButton_alter)
        self.pushButton_delete = QtWidgets.QPushButton(self.tab)
        self.pushButton_delete.setObjectName("pushButton_delete")
        self.verticalLayout_4.addWidget(self.pushButton_delete)
        spacerItem4 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem4)
        self.horizontalLayout_10.addLayout(self.verticalLayout_4)
        self.tabWidget_2.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_14 = QtWidgets.QLabel(self.tab_2)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_2.addWidget(self.label_14)
        self.comboBox_source = QtWidgets.QComboBox(self.tab_2)
        self.comboBox_source.setEnabled(True)
        self.comboBox_source.setMinimumSize(QtCore.QSize(100, 0))
        self.comboBox_source.setMaximumSize(QtCore.QSize(100, 16777215))
        self.comboBox_source.setObjectName("comboBox_source")
        self.comboBox_source.addItem("")
        self.comboBox_source.addItem("")
        self.comboBox_source.addItem("")
        self.comboBox_source.addItem("")
        self.comboBox_source.addItem("")
        self.comboBox_source.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox_source)
        self.lineEdit_source = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_source.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.lineEdit_source.setReadOnly(True)
        self.lineEdit_source.setObjectName("lineEdit_source")
        self.horizontalLayout_2.addWidget(self.lineEdit_source)
        self.verticalLayout_7.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_13 = QtWidgets.QLabel(self.tab_2)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_13.addWidget(self.label_13)
        self.comboBox_dir_2 = QtWidgets.QComboBox(self.tab_2)
        self.comboBox_dir_2.setMinimumSize(QtCore.QSize(100, 0))
        self.comboBox_dir_2.setMaximumSize(QtCore.QSize(100, 16777215))
        self.comboBox_dir_2.setObjectName("comboBox_dir_2")
        self.comboBox_dir_2.addItem("")
        self.comboBox_dir_2.addItem("")
        self.comboBox_dir_2.addItem("")
        self.comboBox_dir_2.addItem("")
        self.horizontalLayout_13.addWidget(self.comboBox_dir_2)
        self.lineEdit_dir_2 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_dir_2.setReadOnly(True)
        self.lineEdit_dir_2.setObjectName("lineEdit_dir_2")
        self.horizontalLayout_13.addWidget(self.lineEdit_dir_2)
        self.toolButton_3 = QtWidgets.QToolButton(self.tab_2)
        self.toolButton_3.setObjectName("toolButton_3")
        self.horizontalLayout_13.addWidget(self.toolButton_3)
        self.verticalLayout_7.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_12 = QtWidgets.QLabel(self.tab_2)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_12.addWidget(self.label_12)
        self.comboBox_dir = QtWidgets.QComboBox(self.tab_2)
        self.comboBox_dir.setMinimumSize(QtCore.QSize(100, 0))
        self.comboBox_dir.setMaximumSize(QtCore.QSize(100, 16777215))
        self.comboBox_dir.setObjectName("comboBox_dir")
        self.comboBox_dir.addItem("")
        self.comboBox_dir.addItem("")
        self.comboBox_dir.addItem("")
        self.comboBox_dir.addItem("")
        self.horizontalLayout_12.addWidget(self.comboBox_dir)
        self.lineEdit_dir = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_dir.setReadOnly(True)
        self.lineEdit_dir.setObjectName("lineEdit_dir")
        self.horizontalLayout_12.addWidget(self.lineEdit_dir)
        self.toolButton_2 = QtWidgets.QToolButton(self.tab_2)
        self.toolButton_2.setObjectName("toolButton_2")
        self.horizontalLayout_12.addWidget(self.toolButton_2)
        self.verticalLayout_7.addLayout(self.horizontalLayout_12)
        spacerItem5 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem5)
        self.tabWidget_2.addTab(self.tab_2, "")
        self.horizontalLayout_9.addWidget(self.tabWidget_2)
        self.stackedWidget.addWidget(self.page_interpreter)
        self.page_format = QtWidgets.QWidget()
        self.page_format.setObjectName("page_format")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.page_format)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_4 = QtWidgets.QLabel(self.page_format)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(
            0, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.comboBox_2 = QtWidgets.QComboBox(self.page_format)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setItemText(2, "")
        self.formLayout.setWidget(
            0, QtWidgets.QFormLayout.FieldRole, self.comboBox_2)
        self.comboBox_3 = QtWidgets.QComboBox(self.page_format)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setItemText(2, "")
        self.formLayout.setWidget(
            1, QtWidgets.QFormLayout.FieldRole, self.comboBox_3)
        self.label_5 = QtWidgets.QLabel(self.page_format)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(
            1, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.comboBox_4 = QtWidgets.QComboBox(self.page_format)
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.setItemText(2, "")
        self.formLayout.setWidget(
            2, QtWidgets.QFormLayout.FieldRole, self.comboBox_4)
        self.label_6 = QtWidgets.QLabel(self.page_format)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(
            2, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.comboBox_5 = QtWidgets.QComboBox(self.page_format)
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.formLayout.setWidget(
            3, QtWidgets.QFormLayout.FieldRole, self.comboBox_5)
        self.label_7 = QtWidgets.QLabel(self.page_format)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(
            3, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.comboBox_6 = QtWidgets.QComboBox(self.page_format)
        self.comboBox_6.setObjectName("comboBox_6")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.formLayout.setWidget(
            4, QtWidgets.QFormLayout.FieldRole, self.comboBox_6)
        self.label_8 = QtWidgets.QLabel(self.page_format)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(
            4, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.verticalLayout_3.addLayout(self.formLayout)
        self.stackedWidget.addWidget(self.page_format)
        self.verticalLayout_2.addWidget(self.splitter)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setMaximumSize(QtCore.QSize(16777215, 50))
        self.widget.setObjectName("widget")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_help = QtWidgets.QPushButton(self.widget)
        self.pushButton_help.setObjectName("pushButton_help")
        self.horizontalLayout.addWidget(self.pushButton_help)
        spacerItem6 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.pushButton_ok = QtWidgets.QPushButton(self.widget)
        self.pushButton_ok.setObjectName("pushButton_ok")
        self.horizontalLayout.addWidget(self.pushButton_ok)
        self.pushButton_cancel = QtWidgets.QPushButton(self.widget)
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.horizontalLayout.addWidget(self.pushButton_cancel)
        self.horizontalLayout_7.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addWidget(self.widget)

        self.retranslateUi(Form)
        self.stackedWidget.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "选项"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("Form", "常规"))
        item = self.listWidget.item(1)
        item.setText(_translate("Form", "外观"))
        item = self.listWidget.item(2)
        item.setText(_translate("Form", "解释器"))
        item = self.listWidget.item(3)
        item.setText(_translate("Form", "格式化"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.label.setText(_translate("Form", "默认工作路径:"))
        self.label_15.setText(_translate("Form", "默认输出路径:"))
        self.checkBox.setText(_translate("Form", "启动时检查更新"))
        self.checkBox_2.setText(_translate("Form", "跟随系统启动"))
        self.label_16.setText(_translate("Form", "语言"))
        self.comboBox_9.setItemText(0, _translate("Form", "简体中文"))
        self.comboBox_9.setItemText(1, _translate("Form", "英文"))
        self.label_11.setText(_translate("Form", "编码:"))
        self.comboBox_8.setItemText(0, _translate("Form", "utf-8"))
        self.comboBox_8.setItemText(1, _translate("Form", "gb2312"))
        self.toolButton_workspace.setText(_translate("Form", "..."))
        self.toolButton_output.setText(_translate("Form", "..."))
        self.label_theme.setText(_translate("Form", "主题"))
        self.comboBox_theme.setItemText(0, _translate("Form", "Fusion"))
        self.comboBox_theme.setItemText(1, _translate("Form", "Qdarkstyle"))
        self.comboBox_theme.setItemText(2, _translate("Form", "windowsvista"))
        self.comboBox_theme.setItemText(3, _translate("Form", "Windows"))
        self.checkBox_minitray.setText(_translate("Form", "最小化到托盘"))
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(
                self.tabBase), _translate(
                "Form", "基本"))
        self.checkBox_3.setText(_translate("Form", "是否隔行着色"))
        self.label_10.setText(_translate("Form", "表头背景颜色:"))
        self.pushButton.setText(_translate("Form", "颜色"))
        self.label_3.setText(_translate("Form", "字体大小："))
        self.lineEdit_2.setText(_translate("Form", "15"))
        self.label_2.setText(_translate("Form", "字体："))
        self.comboBox.setItemText(0, _translate("Form", "Source Code Pro"))
        self.textEdit.setHtml(_translate("Form",
                                         "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                         "p, li { white-space: pre-wrap; }\n"
                                         "</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; "
                                         "font-weight:400; font-style:normal;\">\n "
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; "
                                         "margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Patata is a "
                                         "full-featured IDE</p>\n "
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; "
                                         "margin-right:0px; -qt-block-indent:0; text-indent:0px;\">with a high level "
                                         "of usability and outstanding</p>\n "
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; "
                                         "margin-right:0px; -qt-block-indent:0; text-indent:0px;\">advanced code "
                                         "editing and refactoring support.</p>\n "
                                         "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; "
                                         "margin-left:0px; margin-right:0px; -qt-block-indent:0; "
                                         "text-indent:0px;\"><br /></p>\n "
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; "
                                         "margin-right:0px; -qt-block-indent:0; "
                                         "text-indent:0px;\">abcdefghijklmnopqrstuvwxyz 0123456789 (){}[]</p>\n "
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; "
                                         "margin-right:0px; -qt-block-indent:0; "
                                         "text-indent:0px;\">ABCDEFGHIJKLMNOPQRSTUVWXYZ +-*/= .,"
                                         ";:!? #&amp;$%@|^</p></body></html>"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "名称"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "版本"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "路径"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "默认"))
        self.pushButton_new.setText(_translate("Form", "新增"))
        self.pushButton_alter.setText(_translate("Form", "修改"))
        self.pushButton_delete.setText(_translate("Form", "删除"))
        self.tabWidget_2.setTabText(
            self.tabWidget_2.indexOf(
                self.tab), _translate(
                "Form", "基本"))
        self.label_14.setText(_translate("Form", "下 载 源:"))
        self.comboBox_source.setItemText(0, _translate("Form", "腾讯(推荐)"))
        self.comboBox_source.setItemText(1, _translate("Form", "官方"))
        self.comboBox_source.setItemText(2, _translate("Form", "清华大学"))
        self.comboBox_source.setItemText(3, _translate("Form", "阿里"))
        self.comboBox_source.setItemText(4, _translate("Form", "豆瓣"))
        self.comboBox_source.setItemText(5, _translate("Form", "自定义"))
        self.lineEdit_source.setText(
            _translate(
                "Form",
                "https://mirrors.cloud.tencent.com/pypi/simple"))
        self.lineEdit_source.setPlaceholderText(_translate("Form", "腾讯镜像源"))
        self.label_13.setText(_translate("Form", "默认路径:"))
        self.comboBox_dir_2.setItemText(0, _translate("Form", "默认位置"))
        self.comboBox_dir_2.setItemText(1, _translate("Form", "用户目录"))
        self.comboBox_dir_2.setItemText(2, _translate("Form", "仅下载"))
        self.comboBox_dir_2.setItemText(3, _translate("Form", "自定义"))
        self.lineEdit_dir_2.setPlaceholderText(_translate("Form", "默认"))
        self.toolButton_3.setText(_translate("Form", "..."))
        self.label_12.setText(_translate("Form", "安装选项:"))
        self.comboBox_dir.setItemText(0, _translate("Form", "默认位置"))
        self.comboBox_dir.setItemText(1, _translate("Form", "用户目录"))
        self.comboBox_dir.setItemText(2, _translate("Form", "仅下载"))
        self.comboBox_dir.setItemText(3, _translate("Form", "自定义"))
        self.lineEdit_dir.setPlaceholderText(_translate("Form", "默认"))
        self.toolButton_2.setText(_translate("Form", "..."))
        self.tabWidget_2.setTabText(
            self.tabWidget_2.indexOf(
                self.tab_2), _translate(
                "Form", "高级"))
        self.label_4.setText(_translate("Form", "日期格式:"))
        self.comboBox_2.setItemText(0, _translate("Form", "2020-01-01"))
        self.comboBox_2.setItemText(1, _translate("Form", "2020/01/01"))
        self.comboBox_3.setItemText(0, _translate("Form", "15:30:01(24-小时制)"))
        self.comboBox_3.setItemText(
            1, _translate(
                "Form", "3:30:01 PM(12-小时制)"))
        self.label_5.setText(_translate("Form", "时间格式:"))
        self.comboBox_4.setItemText(0, _translate("Form", "美元US Dollar"))
        self.comboBox_4.setItemText(1, _translate("Form", "人民币Chinese Yuan"))
        self.label_6.setText(_translate("Form", "货币单位:"))
        self.comboBox_5.setItemText(0, _translate("Form", "￥"))
        self.comboBox_5.setItemText(1, _translate("Form", "CNY"))
        self.comboBox_5.setItemText(2, _translate("Form", "$"))
        self.comboBox_5.setItemText(3, _translate("Form", "USD"))
        self.label_7.setText(_translate("Form", "货币符号:"))
        self.comboBox_6.setItemText(0, _translate("Form", "列标题内"))
        self.comboBox_6.setItemText(1, _translate("Form", "单元格内"))
        self.label_8.setText(_translate("Form", "货币符号位于:"))
        self.pushButton_help.setText(_translate("Form", "帮助"))
        self.pushButton_ok.setText(_translate("Form", "确定"))
        self.pushButton_cancel.setText(_translate("Form", "取消"))


class OptionForm(QWidget, Ui_Form):
    """
    打开"选项"窗口
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.center()
        # QssTools.set_qss_to_obj(root_dir + "/ui/source/qss/pyminer2.qss", self)

        # 通过combobox控件选择窗口风格
        self.comboBox_theme.activated[str].connect(self.theme_change)

        self.setting = dict()

        self.listWidget.currentRowChanged.connect(self.option_change)
        self.toolButton_workspace.clicked.connect(self.slot_change_workspace)
        self.toolButton_output.clicked.connect(self.slot_change_output)
        self.pushButton_cancel.clicked.connect(self.close)
        self.pushButton_ok.clicked.connect(self.close)

    def keyPressEvent(self, e):
        """
        按键盘Escape退出当前窗口
        @param e:
        """
        if e.key() == Qt.Key_Escape:
            self.close()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def option_change(self, i):
        self.stackedWidget.setCurrentIndex(i)

    def theme_change(self, style):
        app = get_application()
        app.setStyleSheet('')
        if style == 'Fusion':
            app.setStyle('Fusion')
        elif style == 'Qdarkstyle':
            app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
        elif style.lower() == 'windowsvista':
            app.setStyle("windowsvista")
        elif style.lower() == 'windows':
            app.setStyle("Windows")

    def slot_change_workspace(self):

        directory = QFileDialog.getExistingDirectory(
            self, "选择工作区间位置", get_root_dir())
        self.lineEdit_workspace.setText(directory)

    def slot_change_output(self):
        directory = QFileDialog.getExistingDirectory(
            self, "选择输出文件夹位置", get_root_dir())
        self.lineEdit_output.setText(directory)


if __name__ == '__main__':
    from pyminer2.pmutil import test_widget_run

    test_widget_run(OptionForm)  # 控件的测试函数，可以比主界面更快地启动，方便页面样式调试等。