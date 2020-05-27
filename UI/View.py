import os
import sys

import numpy as np
from PyQt5 import QtWidgets
from PyQt5.QtCore import QDir

from UI.UI import Ui_MainWindow

class View(object):
    
    def __init__(self):

        # value
        self.nowPath = str(os.getcwd()).replace("\\", "/")
        self.filter = ".mp4;;.mov;;.avi;;.wmv"
        self.videoDir = ""
        self.outputDir = ""
        self.outputName = "out.mp4"
        self.confirm = QtWidgets.QMessageBox.Save
        # value

        # form set
        self.app = QtWidgets.QApplication(sys.argv)
        self.MainWindow = QtWidgets.QMainWindow()
        self.form = Ui_MainWindow()
        self.form.setupUi(self.MainWindow)
        # form set

        # combobox setting
        self.comboBoxInit()
        self.form.comboBox.activated.connect(self.activated_comboBox_1)
        self.form.comboBox_2.activated.connect(self.activated_comboBox_2)
        # combobox setting

        # tool button
        self.form.toolButton.clicked.connect(self.clicked_toolbutton_1)
        self.form.toolButton_2.clicked.connect(self.clicked_toolbutton_2)
        # tool button

        # button
        self.form.pushButton.clicked.connect(self.clicked_pushbutton)
        # button

    # function
    def combine(self):
        pass
    # function

    # button
    def clicked_pushbutton(self):
        dialog = QtWidgets.QMessageBox(None)
        dialog.setText("From :"+self.videoDir+"/*\n"+"Combine as :"+self.outputName)
        dialog.setStandardButtons(QtWidgets.QMessageBox.Save | QtWidgets.QMessageBox.Cancel)
        receive = dialog.exec()
        if(receive==self.confirm):
            self.combine()
    # button

    # tool button
    def clicked_toolbutton_1(self):
        temp = self.videoDir
        try:
            self.videoDir = QtWidgets.QFileDialog.getExistingDirectory(None, "影片資料夾", self.nowPath)
            if(self.videoDir[-1]!="/"):
                self.videoDir = self.videoDir+"/"
            path = [self.videoDir+p+"/" for p in os.listdir(self.videoDir) if(os.path.isdir(self.videoDir+p))]
            path.insert(0, self.videoDir)
            self.comboboxRefresh(0, path)
            print("video dir:", self.videoDir)
        except:
            self.videoDir = temp
            print("video dir:", self.videoDir)

    def clicked_toolbutton_2(self):
        dialog = QtWidgets.QFileDialog(None)
        output = dialog.getSaveFileName(None, "輸出資料夾", self.nowPath, filter=self.filter)
        self.outputDir = output[0]+output[1]
        self.comboboxRefresh(1, self.outputDir)
        self.outputName = self.outputDir
        print("target :",self.outputName)
    # tool button

    # combobox setting
    def comboboxRefresh(self, index, path):
        if(index==0):
            self.form.comboBox.clear()
            self.form.comboBox.addItems(path)
            print("combobox refresh")
        elif(index==1):
            self.form.comboBox_2.clear()
            self.form.comboBox_2.addItem(path)
            print("combobox_2 refresh")
        else:
            pass

    def activated_comboBox_1(self):
        self.videoDir = self.form.comboBox.currentText()
        print("video dir:", self.videoDir)

    def activated_comboBox_2(self):
        self.outputDir = self.form.comboBox_2.currentText()
        print("target dir:", self.outputDir)
        
    def comboBoxInit(self):
        path = [self.nowPath+"/"+p for p in os.listdir(self.nowPath) if(os.path.isdir(p))]
        
        self.form.comboBox.clear()
        self.form.comboBox.addItems(path)
        self.videoDir = self.form.comboBox.currentText()

        self.form.comboBox_2.clear()
        self.form.comboBox_2.addItem(path[0]+"/"+self.outputName)
        self.outputDir = self.form.comboBox_2.currentText()
        print("combobox initialized")
    # combobox setting

    # form
    def show(self):
        self.MainWindow.show()
        sys.exit(self.app.exec_())
    # form