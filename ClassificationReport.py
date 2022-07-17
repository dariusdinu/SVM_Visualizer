# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ClassificationReport.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import *


class Ui_ClassificationReportWindow(object):
    def setupUi(self, ClassificationReportWindow):
        ClassificationReportWindow.setObjectName("ClassificationReportWindow")
        ClassificationReportWindow.resize(983, 680)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Facultate/Licenta/dot-crossed_icon-icons.com_68558.ico"), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        ClassificationReportWindow.setWindowIcon(icon)
        with open('ClassificationReportWindow.qss', 'r') as f:
            style = f.read()
            ClassificationReportWindow.setStyleSheet(style)

        self.classificationReport = None
        self.completeClassReport = None
        self.fileName = None

        self.centralwidget = QtWidgets.QWidget(ClassificationReportWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.mainFrame = QtWidgets.QFrame(self.centralwidget)
        self.mainFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mainFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainFrame.setObjectName("mainFrame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.mainFrame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.titleFrame = QtWidgets.QFrame(self.mainFrame)
        self.titleFrame.setMaximumSize(QtCore.QSize(16777215, 100))
        self.titleFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.titleFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.titleFrame.setObjectName("titleFrame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.titleFrame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.titleLabel = QtWidgets.QLabel(self.titleFrame)
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLabel.setObjectName("titleLabel")
        self.horizontalLayout_2.addWidget(self.titleLabel)
        self.verticalLayout.addWidget(self.titleFrame)
        self.tableFrame = QtWidgets.QFrame(self.mainFrame)
        self.tableFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tableFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tableFrame.setObjectName("tableFrame")
        self.gridLayout = QtWidgets.QGridLayout(self.tableFrame)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.tableFrame)
        self.label_2.setText("")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.innerLabel14 = QtWidgets.QLabel(self.tableFrame)
        self.innerLabel14.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.innerLabel14.setObjectName("innerLabel14")
        self.gridLayout.addWidget(self.innerLabel14, 10, 3, 1, 1)
        self.innerLabel15 = QtWidgets.QLabel(self.tableFrame)
        self.innerLabel15.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.innerLabel15.setObjectName("innerLabel15")
        self.gridLayout.addWidget(self.innerLabel15, 10, 4, 1, 1)
        self.innerLabel13 = QtWidgets.QLabel(self.tableFrame)
        self.innerLabel13.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.innerLabel13.setObjectName("innerLabel13")
        self.gridLayout.addWidget(self.innerLabel13, 10, 1, 1, 1)
        self.innerLabel2 = QtWidgets.QLabel(self.tableFrame)
        self.innerLabel2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.innerLabel2.setObjectName("innerLabel2")
        self.gridLayout.addWidget(self.innerLabel2, 4, 3, 1, 1)
        self.innerLabel7 = QtWidgets.QLabel(self.tableFrame)
        self.innerLabel7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.innerLabel7.setObjectName("innerLabel7")
        self.gridLayout.addWidget(self.innerLabel7, 6, 4, 1, 1)
        self.innerLabel5 = QtWidgets.QLabel(self.tableFrame)
        self.innerLabel5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.innerLabel5.setObjectName("innerLabel5")
        self.gridLayout.addWidget(self.innerLabel5, 6, 1, 1, 1)
        self.SupportVectorsLabel = QtWidgets.QLabel(self.tableFrame)
        self.SupportVectorsLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.SupportVectorsLabel.setObjectName("SupportVectorsLabel")
        self.gridLayout.addWidget(self.SupportVectorsLabel, 0, 5, 1, 1)
        self.accuracyLabel = QtWidgets.QLabel(self.tableFrame)
        self.accuracyLabel.setObjectName("accuracyLabel")
        self.gridLayout.addWidget(self.accuracyLabel, 8, 0, 1, 1)
        self.precisionLabel = QtWidgets.QLabel(self.tableFrame)
        self.precisionLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.precisionLabel.setObjectName("precisionLabel")
        self.gridLayout.addWidget(self.precisionLabel, 0, 1, 1, 1)
        self.innerLabel17 = QtWidgets.QLabel(self.tableFrame)
        self.innerLabel17.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.innerLabel17.setObjectName("innerLabel17")
        self.gridLayout.addWidget(self.innerLabel17, 11, 1, 1, 1)
        self.innerLabel19 = QtWidgets.QLabel(self.tableFrame)
        self.innerLabel19.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.innerLabel19.setObjectName("innerLabel19")
        self.gridLayout.addWidget(self.innerLabel19, 11, 4, 1, 1)
        self.innerLabel10 = QtWidgets.QLabel(self.tableFrame)
        self.innerLabel10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.innerLabel10.setObjectName("innerLabel10")
        self.gridLayout.addWidget(self.innerLabel10, 8, 3, 1, 1)
        self.innerLabel18 = QtWidgets.QLabel(self.tableFrame)
        self.innerLabel18.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.innerLabel18.setObjectName("innerLabel18")
        self.gridLayout.addWidget(self.innerLabel18, 11, 3, 1, 1)
        self.innerLabel11 = QtWidgets.QLabel(self.tableFrame)
        self.innerLabel11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.innerLabel11.setObjectName("innerLabel11")
        self.gridLayout.addWidget(self.innerLabel11, 8, 4, 1, 1)
        self.innerLabel4 = QtWidgets.QLabel(self.tableFrame)
        self.innerLabel4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.innerLabel4.setObjectName("innerLabel4")
        self.gridLayout.addWidget(self.innerLabel4, 4, 5, 1, 1)
        self.secondClassLabel = QtWidgets.QLabel(self.tableFrame)
        self.secondClassLabel.setObjectName("secondClassLabel")
        self.gridLayout.addWidget(self.secondClassLabel, 6, 0, 1, 1)
        self.innerLabel3 = QtWidgets.QLabel(self.tableFrame)
        self.innerLabel3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.innerLabel3.setObjectName("innerLabel3")
        self.gridLayout.addWidget(self.innerLabel3, 4, 4, 1, 1)
        self.innerLabel20 = QtWidgets.QLabel(self.tableFrame)
        self.innerLabel20.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.innerLabel20.setObjectName("innerLabel20")
        self.gridLayout.addWidget(self.innerLabel20, 11, 5, 1, 1)
        self.innerLabel16 = QtWidgets.QLabel(self.tableFrame)
        self.innerLabel16.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.innerLabel16.setObjectName("innerLabel16")
        self.gridLayout.addWidget(self.innerLabel16, 10, 5, 1, 1)
        self.innerLabel12 = QtWidgets.QLabel(self.tableFrame)
        self.innerLabel12.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.innerLabel12.setObjectName("innerLabel12")
        self.gridLayout.addWidget(self.innerLabel12, 8, 5, 1, 1)
        self.firstClassLabel = QtWidgets.QLabel(self.tableFrame)
        self.firstClassLabel.setObjectName("firstClassLabel")
        self.gridLayout.addWidget(self.firstClassLabel, 4, 0, 1, 1)
        self.macroAverageLabel = QtWidgets.QLabel(self.tableFrame)
        self.macroAverageLabel.setObjectName("macroAverageLabel")
        self.gridLayout.addWidget(self.macroAverageLabel, 10, 0, 1, 1)
        self.innerLabel6 = QtWidgets.QLabel(self.tableFrame)
        self.innerLabel6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.innerLabel6.setObjectName("innerLabel6")
        self.gridLayout.addWidget(self.innerLabel6, 6, 3, 1, 1)
        self.innerLabel1 = QtWidgets.QLabel(self.tableFrame)
        self.innerLabel1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.innerLabel1.setObjectName("innerLabel1")
        self.gridLayout.addWidget(self.innerLabel1, 4, 1, 1, 1)
        self.innerLabel9 = QtWidgets.QLabel(self.tableFrame)
        self.innerLabel9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.innerLabel9.setObjectName("innerLabel9")
        self.gridLayout.addWidget(self.innerLabel9, 8, 1, 1, 1)
        self.F1ScoreLabel = QtWidgets.QLabel(self.tableFrame)
        self.F1ScoreLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.F1ScoreLabel.setObjectName("F1ScoreLabel")
        self.gridLayout.addWidget(self.F1ScoreLabel, 0, 4, 1, 1)
        self.recallLabel = QtWidgets.QLabel(self.tableFrame)
        self.recallLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.recallLabel.setObjectName("recallLabel")
        self.gridLayout.addWidget(self.recallLabel, 0, 3, 1, 1)
        self.innerLabel8 = QtWidgets.QLabel(self.tableFrame)
        self.innerLabel8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.innerLabel8.setObjectName("innerLabel8")
        self.gridLayout.addWidget(self.innerLabel8, 6, 5, 1, 1)
        self.weightedAverageLabel = QtWidgets.QLabel(self.tableFrame)
        self.weightedAverageLabel.setToolTipDuration(4)
        self.weightedAverageLabel.setObjectName("weightedAverageLabel")
        self.gridLayout.addWidget(self.weightedAverageLabel, 11, 0, 1, 1)
        self.verticalLayout.addWidget(self.tableFrame)
        self.LoadTextButton = QtWidgets.QPushButton(self.mainFrame, clicked=lambda: self.load())
        self.LoadTextButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.LoadTextButton.setObjectName("LoadTextButton")
        self.verticalLayout.addWidget(self.LoadTextButton)
        self.saveFrame = QtWidgets.QFrame(self.mainFrame)
        self.saveFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.saveFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.saveFrame.setObjectName("saveFrame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.saveFrame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEdit = QtWidgets.QLineEdit(self.saveFrame)
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_2.addWidget(self.lineEdit)
        self.saveButton = QtWidgets.QPushButton(self.saveFrame, clicked=lambda: self.saveToTextFile())
        self.saveButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.saveButton.setObjectName("saveButton")
        self.verticalLayout_2.addWidget(self.saveButton)
        self.verticalLayout.addWidget(self.saveFrame)
        self.horizontalLayout.addWidget(self.mainFrame)
        ClassificationReportWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(ClassificationReportWindow)
        QtCore.QMetaObject.connectSlotsByName(ClassificationReportWindow)

    def retranslateUi(self, ClassificationReportWindow):
        _translate = QtCore.QCoreApplication.translate
        ClassificationReportWindow.setWindowTitle(_translate("ClassificationReportWindow", "Classification Report"))
        self.mainFrame.setAccessibleName(_translate("ClassificationReportWindow", "mainFrame"))
        self.titleFrame.setAccessibleName(_translate("ClassificationReportWindow", "titleFrame"))
        self.titleLabel.setAccessibleName(_translate("ClassificationReportWindow", "titleLabel"))
        self.titleLabel.setText(_translate("ClassificationReportWindow", "SVM Visualizer"))
        self.tableFrame.setAccessibleName(_translate("ClassificationReportWindow", "tableFrame"))
        self.innerLabel14.setAccessibleName(_translate("ClassificationReportWindow", "innerLabel"))
        self.innerLabel14.setText(_translate("ClassificationReportWindow", ""))
        self.innerLabel15.setAccessibleName(_translate("ClassificationReportWindow", "innerLabel"))
        self.innerLabel15.setText(_translate("ClassificationReportWindow", ""))
        self.innerLabel13.setAccessibleName(_translate("ClassificationReportWindow", "innerLabel"))
        self.innerLabel13.setText(_translate("ClassificationReportWindow", ""))
        self.innerLabel2.setAccessibleName(_translate("ClassificationReportWindow", "innerLabel"))
        self.innerLabel2.setText(_translate("ClassificationReportWindow", ""))
        self.innerLabel7.setAccessibleName(_translate("ClassificationReportWindow", "innerLabel"))
        self.innerLabel7.setText(_translate("ClassificationReportWindow", ""))
        self.innerLabel5.setAccessibleName(_translate("ClassificationReportWindow", "innerLabel"))
        self.innerLabel5.setText(_translate("ClassificationReportWindow", ""))
        self.SupportVectorsLabel.setAccessibleName(_translate("ClassificationReportWindow", "outerLabel"))
        self.SupportVectorsLabel.setText(_translate("ClassificationReportWindow", "Support Vectors"))
        self.accuracyLabel.setAccessibleName(_translate("ClassificationReportWindow", "outerLabel"))
        self.accuracyLabel.setText(_translate("ClassificationReportWindow", "Accuracy"))
        self.precisionLabel.setAccessibleName(_translate("ClassificationReportWindow", "outerLabel"))
        self.precisionLabel.setText(_translate("ClassificationReportWindow", "Precision"))
        self.innerLabel17.setAccessibleName(_translate("ClassificationReportWindow", "innerLabel"))
        self.innerLabel17.setText(_translate("ClassificationReportWindow", ""))
        self.innerLabel19.setAccessibleName(_translate("ClassificationReportWindow", "innerLabel"))
        self.innerLabel19.setText(_translate("ClassificationReportWindow", ""))
        self.innerLabel10.setAccessibleName(_translate("ClassificationReportWindow", "innerLabel"))
        self.innerLabel10.setText(_translate("ClassificationReportWindow", ""))
        self.innerLabel18.setAccessibleName(_translate("ClassificationReportWindow", "innerLabel"))
        self.innerLabel18.setText(_translate("ClassificationReportWindow", ""))
        self.innerLabel11.setAccessibleName(_translate("ClassificationReportWindow", "innerLabel"))
        self.innerLabel11.setText(_translate("ClassificationReportWindow", ""))
        self.innerLabel4.setAccessibleName(_translate("ClassificationReportWindow", "innerLabel"))
        self.innerLabel4.setText(_translate("ClassificationReportWindow", ""))
        self.secondClassLabel.setAccessibleName(_translate("ClassificationReportWindow", "outerLabel"))
        self.secondClassLabel.setText(_translate("ClassificationReportWindow", "Second Label Name"))
        self.innerLabel3.setAccessibleName(_translate("ClassificationReportWindow", "innerLabel"))
        self.innerLabel3.setText(_translate("ClassificationReportWindow", ""))
        self.innerLabel20.setAccessibleName(_translate("ClassificationReportWindow", "innerLabel"))
        self.innerLabel20.setText(_translate("ClassificationReportWindow", ""))
        self.innerLabel16.setAccessibleName(_translate("ClassificationReportWindow", "innerLabel"))
        self.innerLabel16.setText(_translate("ClassificationReportWindow", ""))
        self.innerLabel12.setAccessibleName(_translate("ClassificationReportWindow", "innerLabel"))
        self.innerLabel12.setText(_translate("ClassificationReportWindow", ""))
        self.firstClassLabel.setAccessibleName(_translate("ClassificationReportWindow", "outerLabel"))
        self.firstClassLabel.setText(_translate("ClassificationReportWindow", "First Label Name"))
        self.macroAverageLabel.setAccessibleName(_translate("ClassificationReportWindow", "outerLabel"))
        self.macroAverageLabel.setText(_translate("ClassificationReportWindow", "Macro Average"))
        self.innerLabel6.setAccessibleName(_translate("ClassificationReportWindow", "innerLabel"))
        self.innerLabel6.setText(_translate("ClassificationReportWindow", ""))
        self.innerLabel1.setAccessibleName(_translate("ClassificationReportWindow", "innerLabel"))
        self.innerLabel1.setText(_translate("ClassificationReportWindow", ""))
        self.innerLabel9.setAccessibleName(_translate("ClassificationReportWindow", "innerLabel"))
        self.innerLabel9.setText(_translate("ClassificationReportWindow", ""))
        self.F1ScoreLabel.setAccessibleName(_translate("ClassificationReportWindow", "outerLabel"))
        self.F1ScoreLabel.setText(_translate("ClassificationReportWindow", "F1-score"))
        self.recallLabel.setAccessibleName(_translate("ClassificationReportWindow", "outerLabel"))
        self.recallLabel.setText(_translate("ClassificationReportWindow", "Recall"))
        self.innerLabel8.setAccessibleName(_translate("ClassificationReportWindow", "innerLabel"))
        self.innerLabel8.setText(_translate("ClassificationReportWindow", ""))
        self.weightedAverageLabel.setAccessibleName(_translate("ClassificationReportWindow", "outerLabel"))
        self.weightedAverageLabel.setText(_translate("ClassificationReportWindow", "Weighted Average"))
        self.LoadTextButton.setAccessibleName(_translate("ClassificationReportWindow", "LoadTextButton"))
        self.LoadTextButton.setText(_translate("ClassificationReportWindow", "Load"))
        self.saveFrame.setAccessibleName(_translate("ClassificationReportWindow", "saveFrame"))
        self.lineEdit.setPlaceholderText(_translate("ClassificationReportWindow", "Type here the name of the file in which you want to save the result"))
        self.saveButton.setAccessibleName(_translate("ClassificationReportWindow", "saveButton"))
        self.saveButton.setText(_translate("ClassificationReportWindow", "Save"))

    def load(self):
        self.innerLabel1.setText(self.classificationReport[5])
        self.innerLabel2.setText(self.classificationReport[6])
        self.innerLabel3.setText(self.classificationReport[7])
        self.innerLabel4.setText(self.classificationReport[8])

        self.firstClassLabel.setText(self.classificationReport[4])
        self.secondClassLabel.setText(self.classificationReport[9])

        self.innerLabel5.setText(self.classificationReport[10])
        self.innerLabel6.setText(self.classificationReport[11])
        self.innerLabel7.setText(self.classificationReport[12])
        self.innerLabel8.setText(self.classificationReport[13])

        self.innerLabel11.setText(self.classificationReport[15])
        self.innerLabel12.setText(self.classificationReport[16])
        self.innerLabel12.setText(self.classificationReport[16])

        self.innerLabel13.setText(self.classificationReport[19])
        self.innerLabel14.setText(self.classificationReport[20])
        self.innerLabel15.setText(self.classificationReport[21])
        self.innerLabel16.setText(self.classificationReport[22])

        self.innerLabel17.setText(self.classificationReport[25])
        self.innerLabel18.setText(self.classificationReport[26])
        self.innerLabel19.setText(self.classificationReport[27])
        self.innerLabel20.setText(self.classificationReport[28])

        self.innerLabel9.setText('')
        self.innerLabel10.setText('')

    def saveToTextFile(self):
        self.fileName = self.lineEdit.text()
        if self.fileName != '':
            f = open(f'{self.fileName}.txt', 'w+')
            f.write(self.completeClassReport)
            self.textFileCreated()
        else:
            self.noFilePopUp()

    def textFileCreated(self):
        msg = QMessageBox()
        msg.setWindowTitle("Info")
        msg.setText(f"Data saved to the {self.fileName}.txt file")
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok)
        x = msg.exec_()

    def noFilePopUp(self):
        msg = QMessageBox()
        msg.setWindowTitle("Error")
        msg.setText(f"Choose the name of the file in order to proceed!")
        msg.setIcon(QMessageBox.Critical)
        msg.setStandardButtons(QMessageBox.Ok)
        x = msg.exec_()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ClassificationReportWindow = QtWidgets.QMainWindow()
    ui = Ui_ClassificationReportWindow()
    ui.setupUi(ClassificationReportWindow)
    ClassificationReportWindow.show()
    sys.exit(app.exec_())
