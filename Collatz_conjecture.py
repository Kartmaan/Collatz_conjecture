from PyQt5 import QtWidgets
from window_collatz import Ui_MainWindow
import pyqtgraph.exporters
import pyqtgraph as pg

import sys
import random
import numpy as np
import pyperclip
from statistics import mean, median

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        self.checkBox_nb2.stateChanged.connect(self.checkBox)
        self.button_look.clicked.connect(self.look)
        self.button_save.clicked.connect(self.export)
        self.button_copy.clicked.connect(self.copy)
        self.button_lucky.clicked.connect(self.lucky)

        self.button_save.setEnabled(False)
        self.button_copy.setEnabled(False)
        self.label_status.setText(". . .")

        self.list_1 = []
        self.list_2 = []
        self.number1 = ""
        self.number2 = ""
        
    def checkBox(self) :
        # Checkbox behaviour
        if self.checkBox_nb2.isChecked() :
            self.input_2.setEnabled(True) #LineEdit_2 enable
        else :
            self.input_2.setEnabled(False)
    
    def syra(self, x): # <int>
        # Renvoie une liste contenant la suite de Syracuse du nombre x
        x = int(x)
        i = 0 # Security cursor 
        wd = 50000 # Watchdog limit
        L = [] # List containing Syracuse numbers
    
        while True:
            # Even number
            if x % 2 == 0:
                x = x / 2
                L.append(int(x))
                i += 1
                if i > wd : # Watchdog activated
                    self.label_status.setText("STOP : Watchdog activated")
                    raise OverflowError
                if L.count(1) :
                    break
            # Odd number
            else :
                x = x*3 + 1
                L.append(int(x))
                i += 1
                if i > wd : # Watchdog activated
                    self.label_status.setText("STOP : Watchdog activated")
                    raise OverflowError
                if L.count(1) :
                    break
        return L # <list>

    def syraStats(self, value, syra_list) : # <int>, <list>
        value = int(value)

        # Time in flight
        tif = len(syra_list)

        # Time in altitude
        alt = []
        even = 0
        odd = 0
        for i in syra_list:
            #odd / even
            if i % 2 == 0 :
                even += 1
            if i % 2 != 0 :
                odd += 1

            # On altitude
            if i > value :
                alt.append(i)
            else :
                continue
        alt = len(alt)
        
        # Max altitude
        max = sorted(syra_list)
        max = max[len(max)-1]

        # Average altitude
        mn = int(mean(syra_list))

        # Median altitude
        md = int(median(syra_list))

        # Time in flight, on altitude, alt max, mean alt, median alt,
        # evens, odds
        return tif, alt, max, mn, md, even, odd # <tuple>

    def graph(self, syraList_1 = [], syraList_2 = []) :
        self.graphWidget.clear()
        self.graphWidget.addLegend()

        if len(syraList_2) == 0 :
            x1 = list(range(1, len(syraList_1) + 1))
            x1 = np.array(x1)
            y1 = np.array(syraList_1)
            num_1 = self.input_1.text()
            self.graphWidget.plot(x1, y1, pen = self.red_pen, name = num_1)

        else :
            x1 = list(range(1, len(syraList_1) + 1))
            x1 = np.array(x1)
            y1 = np.array(syraList_1)
            num_1 = self.input_1.text()
            self.graphWidget.plot(x1, y1, pen = self.red_pen, name = num_1)

            x2 = list(range(1, len(syraList_2) + 1))
            x2 = np.array(x2)
            y2 = np.array(syraList_2)
            num_2 = self.input_2.text()
            self.graphWidget.plot(x2, y2, pen = self.blue_pen, name = num_2)

        self.button_save.setEnabled(True)

    def export(self) :
        nb_1 = self.input_1.text()
        exporter = pg.exporters.ImageExporter(self.graphWidget.plotItem)
        if self.checkBox_nb2.isChecked() == False:
            exporter.export('{}.png'.format(nb_1))
        else :
            nb_2 = self.input_2.text()
            exporter = pg.exporters.ImageExporter(self.graphWidget.plotItem)
            exporter.export('{}-{}.png'.format(nb_1, nb_2))

        self.label_status.setText("Image saved successfully")

    def copy(self):
        # Button copy behaviour
        if self.checkBox_nb2.isChecked() == False :
            output = "--- Number {} ---\n{}".format(self.input_1.text(), self.list_1)
            pyperclip.copy(output)

        if self.checkBox_nb2.isChecked() :
            output1 = "--- Number {} ---\n{}\n".format(self.input_1.text(), self.list_1)
            output2 = "\n--- Number {} ---\n{}".format(self.input_2.text(), self.list_2)
            output = (output1 + output2)
            output = str(output)
            pyperclip.copy(output)
        
        self.label_status.setText("Copied to clipboard")

    def lucky(self):
        max = 500000
        if self.checkBox_nb2.isChecked() == False :
            x = random.randint(1,max)
            x = str(x)
            self.input_1.setText(x)
            self.look()

        if self.checkBox_nb2.isChecked():
            x = random.randint(1,max)
            y = random.randint(1,max)
            x = str(x)
            y = str(y)

            self.input_1.setText(x)
            self.input_2.setText(y)

            self.look()

    def stat_display(self, nb, syraList) :
        # Display stats of syraStats
        tif, alt, alt_max, alt_mean, alt_median, even, odd = self.syraStats(nb, syraList)
        line1 = "Number {} : \n".format(nb)
        line2 = "Flight time = {} | On altitude = {} | Max altitude = {} | Average altitude = {}\n".format(tif, alt, alt_max, alt_mean)
        line3 = "Even numbers = {} | Odd numbers = {}".format(even, odd)
        stat = line1 + line2 + line3

        return stat

    def look(self):
        # Button "Have a look" behaviour
        # ------------ TREATMENT OF NB1 ------------
        # NB1 EXTRACTION --------------------------
        nb_1 = self.input_1.text()

        if len(nb_1) == 0 :
            self.label_status.setText("Empty input")
            return None

        nb_1 = int(nb_1)
        #print(nb_1)
        
        if nb_1 <= 0 :
            self.label_status.setText("The number must be greater than zero")
            return None
        
        if self.checkBox_nb2.isChecked():
            if len(self.input_2.text()) > 0:
                if int(self.input_2.text()) < 0 :
                    self.label_status.setText("The number must be greater than zero")
                    return None

        # NB1 CALCULATION --------------------------
        syra_list = self.syra(nb_1)
        self.list_1 = syra_list
        #print(self.list_1)

        # NB1 STATS --------------------------
        self.text_nb1.setText(self.stat_display(nb_1, syra_list))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_nb1),(str(nb_1)))
        if self.checkBox_nb2.isChecked() == False :
                self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_nb2),("nb2"))
                self.text_nb2.setText("")

        # NB1 GRAPH --------------------------
        if self.checkBox_nb2.isChecked() == False :
            self.graphWidget.setTitle("Number {}".format(nb_1))
            self.graph(syraList_1= syra_list)
            self.button_copy.setText("Copy list")

        # ------------ TREATMENT OF NB2 ------------
        # NB2 EXTRACTION --------------------------
        if self.checkBox_nb2.isChecked():
            nb_2 = self.input_2.text()

            if len(nb_2) == 0 :
                self.label_status.setText("Empty input")
                return None

            nb_2 = int(nb_2)
            #print(nb_2)

            if nb_2 <= 0 :
                self.label_status.setText("The number must be greater than zero")
                return None

            # NB2 CALCULATION --------------------------
            syra_list2 = self.syra(nb_2)
            self.list_2 = syra_list2
            #print(self.list_2)

            # NB2 STATS --------------------------
            self.text_nb2.setText(self.stat_display(nb_2, syra_list2))
            self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_nb2),(str(nb_2)))

            # NB2 GRAPH --------------------------
            self.graphWidget.setTitle("Numbers {} / {}".format(nb_1, nb_2))
            self.graph(syraList_1= syra_list, syraList_2= syra_list2)
            self.button_copy.setText("Copy lists")

        self.button_copy.setEnabled(True)

if __name__ == "__main__" :
    app = QtWidgets.QApplication(sys.argv) # []
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_()) # app.exec()