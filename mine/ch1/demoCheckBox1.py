# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ch1\demoCheckBox1.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(397, 218)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(240, 30, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 50, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.labelAmount = QtWidgets.QLabel(Dialog)
        self.labelAmount.setGeometry(QtCore.QRect(20, 170, 351, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelAmount.setFont(font)
        self.labelAmount.setText("")
        self.labelAmount.setAlignment(QtCore.Qt.AlignCenter)
        self.labelAmount.setObjectName("labelAmount")
        self.checkBoxCheese = QtWidgets.QCheckBox(Dialog)
        self.checkBoxCheese.setGeometry(QtCore.QRect(230, 60, 161, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBoxCheese.setFont(font)
        self.checkBoxCheese.setObjectName("checkBoxCheese")
        self.checkBoxOlive = QtWidgets.QCheckBox(Dialog)
        self.checkBoxOlive.setGeometry(QtCore.QRect(230, 90, 161, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBoxOlive.setFont(font)
        self.checkBoxOlive.setObjectName("checkBoxOlive")
        self.checkBoxSausage = QtWidgets.QCheckBox(Dialog)
        self.checkBoxSausage.setGeometry(QtCore.QRect(230, 120, 161, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBoxSausage.setFont(font)
        self.checkBoxSausage.setObjectName("checkBoxSausage")
        self.checkBoxRegularPizza = QtWidgets.QCheckBox(Dialog)
        self.checkBoxRegularPizza.setEnabled(False)
        self.checkBoxRegularPizza.setGeometry(QtCore.QRect(230, 30, 16, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBoxRegularPizza.setFont(font)
        self.checkBoxRegularPizza.setText("")
        self.checkBoxRegularPizza.setCheckable(True)
        self.checkBoxRegularPizza.setChecked(True)
        self.checkBoxRegularPizza.setTristate(False)
        self.checkBoxRegularPizza.setObjectName("checkBoxRegularPizza")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 30, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Regular Pizza $10"))
        self.label_2.setText(_translate("Dialog", "Select your extra toppings"))
        self.checkBoxCheese.setText(_translate("Dialog", "Extra Cheese $1"))
        self.checkBoxOlive.setText(_translate("Dialog", "Extra Olives $1"))
        self.checkBoxSausage.setText(_translate("Dialog", "Extra Sausage $2"))
        self.label_3.setText(_translate("Dialog", "Pizza"))
