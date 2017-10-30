# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1827, 1030)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(10, 60, 1801, 961))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(11)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, item)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(1340, 20, 112, 34))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(1580, 20, 112, 34))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(1460, 20, 112, 34))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(1700, 20, 112, 34))
        self.pushButton_4.setObjectName("pushButton_4")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "eShop 游戏信息汇总  @哆啦C梦幸福"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "游戏名称"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "中文名称"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "发售时间"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "发售状态"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "公布状态"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "最新上线"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Form", "试玩版本"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("Form", "图标地址"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("Form", "最优价格"))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("Form", "最优价格转换"))
        item = self.tableWidget.horizontalHeaderItem(10)
        item.setText(_translate("Form", "价格最优区域"))
        self.pushButton.setText(_translate("Form", "首页"))
        self.pushButton_3.setText(_translate("Form", "下一页"))
        self.pushButton_2.setText(_translate("Form", "上一页"))
        self.pushButton_4.setText(_translate("Form", "尾页"))

