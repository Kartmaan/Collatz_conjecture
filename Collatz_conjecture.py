# -*- coding: utf-8 -*-

import sys
import random
from statistics import mean, median

from PyQt5 import QtWidgets
import pyqtgraph.exporters
import pyqtgraph as pg
import numpy as np
import pyperclip # Copy to clipboard

from window import Ui_MainWindow

__author__ = "Kartmaan"
__version__ = "0.5"

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        # Link widgets to their functions
        self.checkBox_nb2.stateChanged.connect(self.checkBox)
        self.button_look.clicked.connect(self.look)
        self.button_save.clicked.connect(self.export)
        self.button_copy.clicked.connect(self.copy)
        self.button_lucky.clicked.connect(self.lucky)

        # Initial state of widgets
        self.button_save.setEnabled(False)
        self.button_copy.setEnabled(False)
        self.label_status.setText(". . .")

        self.list_1 = []
        self.list_2 = []
        """ self.number1 = ""
        self.number2 = "" """
        
    def checkBox(self) :
        # QCheckbox behaviour
        if self.checkBox_nb2.isChecked() :
            self.input_2.setEnabled(True) #QLineEdit_2 enable
        else :
            self.input_2.setEnabled(False) #QLineEdit_2 disable
    
    def collatz(self, x): # <int>
        # Function that return a Collatz sequence from int value
        x = int(x)
        i = 0 # Security cursor 
        wd = 50000 # Watchdog limit
        L = [] # List containing Collatz sequence
    
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

    def collatzStats(self, value, syra_list) : # <int>, <list>
        # Function that return statistics from a Collatz sequence
        value = int(value)

        # Time in flight
        tif = len(syra_list)

        alt = []
        even = 0
        odd = 0
        for i in syra_list:
            # odd / even
            if i % 2 == 0 :
                even += 1
            if i % 2 != 0 :
                odd += 1

            # On altitude :
            # number of values in the sequence greater than the initial value
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

        # Median altitude (not used)
        md = int(median(syra_list))

        # Index tuple :
        # {0:Time in flight, 1:on altitude, 2:alt max, 3:mean alt, 4:median alt, 5:evens, 6:odds}
        return tif, alt, max, mn, md, even, odd # <tuple>

    def graph(self, syraList_1 = [], syraList_2 = []) :
        # Graphic representation of Collatz sequences
        self.graphWidget.clear()
        self.graphWidget.addLegend()

        # Only one sequence to represent
        if self.checkBox_nb2.isChecked() == False :
            x1 = list(range(1, len(syraList_1) + 1))
            x1 = np.array(x1)
            y1 = np.array(syraList_1)
            num_1 = self.input_1.text()
            self.graphWidget.plot(x1, y1, pen = self.red_pen, name = num_1)

        # Two sequences to represent
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
        # Export the graph as .png at the current directory
        nb_1 = self.input_1.text()
        exporter = pg.exporters.ImageExporter(self.graphWidget.plotItem)

        if self.checkBox_nb2.isChecked() == False:
            exporter.export('{}.png'.format(nb_1))

        else :
            nb_2 = self.input_2.text()
            exporter = pg.exporters.ImageExporter(self.graphWidget.plotItem)
            exporter.export('{}-{}.png'.format(nb_1, nb_2))

        self.label_status.setText("Graph saved successfully")

    def copy(self):
        # Copy sequence(s) in clipboard
        if self.checkBox_nb2.isChecked() == False : # One sequence
            output = "--- Number {} ---\n{}".format(self.input_1.text(), self.list_1)
            pyperclip.copy(output)

        if self.checkBox_nb2.isChecked() : # Two sequences
            output1 = "--- Number {} ---\n{}\n".format(self.input_1.text(), self.list_1)
            output2 = "\n--- Number {} ---\n{}".format(self.input_2.text(), self.list_2)
            output = (output1 + output2)
            output = str(output)
            pyperclip.copy(output)
        
        self.label_status.setText("Copied to clipboard")

    def lucky(self):
        # Rondomize the inputs
        max = 50000 # max interval
        if self.checkBox_nb2.isChecked() == False : # 1 input
            x = random.randint(1,max)
            x = str(x)
            self.input_1.setText(x)
            self.look() # Automatic generation

        if self.checkBox_nb2.isChecked(): # 2 inputs
            x = random.randint(1,max)
            y = random.randint(1,max)
            x = str(x)
            y = str(y)

            self.input_1.setText(x)
            self.input_2.setText(y)

            self.look() # Automatic generation

    def stat_display(self, nb, syraList) :
        # Display stats from collatzStats
        tif, alt, alt_max, alt_mean, alt_median, even, odd = self.collatzStats(nb, syraList)
        line1 = "Number {} : \n".format(nb)
        line2 = "Flight time = {} | On altitude = {} | Max altitude = {} | Avrg altitude = {}\n".format(tif, alt, alt_max, alt_mean)
        line3 = "Even numbers = {} | Odd numbers = {}".format(even, odd)
        stat = line2 + line3

        return stat

    def look(self):
        # Run all the generation process

        # ------------ TREATMENT OF NB1 ------------
        # NB1 EXTRACTION --------------------------
        nb_1 = self.input_1.text()

        if len(nb_1) == 0 :
            self.label_status.setText("Empty input")
            return None

        nb_1 = int(nb_1)
        
        if nb_1 <= 0 :
            self.label_status.setText("The number must be greater than zero")
            return None
        
        if self.checkBox_nb2.isChecked():
            if len(self.input_2.text()) > 0:
                if int(self.input_2.text()) < 0 :
                    self.label_status.setText("The number must be greater than zero")
                    return None

        # NB1 CALCULATION --------------------------
        syra_list = self.collatz(nb_1)
        self.list_1 = syra_list

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

            if nb_2 <= 0 :
                self.label_status.setText("The number must be greater than zero")
                return None

            # NB2 CALCULATION --------------------------
            syra_list2 = self.collatz(nb_2)
            self.list_2 = syra_list2

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