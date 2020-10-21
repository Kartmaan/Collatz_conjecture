# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import QFrame
import pyqtgraph as pg

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.setWindowTitle("Collatz conjecture")

        MainWindow.resize(1060, 535)
        MainWindow.setMinimumSize(QtCore.QSize(1060, 535))
        MainWindow.setMaximumSize(QtCore.QSize(1060, 535))

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Graphic frame
        self.frame_graph = QtWidgets.QFrame(self.centralwidget)
        self.frame_graph.setGeometry(QtCore.QRect(450, 10, 591, 421))
        self.frame_graph.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_graph.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_graph.setObjectName("frame_graph")
        
        # Graphic
        self.graphWidget = pg.PlotWidget(self.frame_graph)
        self.graphWidget.setGeometry(QtCore.QRect(0,0,591,421))
        self.graphWidget.setBackground('w')
        self.graphWidget.showGrid(x=True, y=True)
        self.graphWidget.setTitle("", bold=True)
        self.graphWidget.setLabel('left', 'Altitude')
        self.graphWidget.setLabel('bottom', 'Flight time')

        # Pens
        self.red_pen = pg.mkPen(color=(255,0,0), width = 1)
        self.blue_pen = pg.mkPen(color=(0,0,255), width = 1)

        # Button save
        self.button_save = QtWidgets.QPushButton(self.centralwidget)
        self.button_save.setGeometry(QtCore.QRect(930, 440, 111, 28))
        self.button_save.setText("Save the graph")
        self.button_save.setObjectName("save_graph")

        # Button copy
        self.button_copy = QtWidgets.QPushButton(self.centralwidget)
        self.button_copy.setGeometry(QtCore.QRect(930, 470, 111, 28))
        self.button_copy.setText("Copy list")

        # Vertical line
        self.vertical_line = QtWidgets.QFrame(self.centralwidget)
        self.vertical_line.setGeometry(QtCore.QRect(425, 0, 21, 541))
        self.vertical_line.setFrameShape(QtWidgets.QFrame.VLine)
        self.vertical_line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.vertical_line.setObjectName("vertical_line")

        # Groupbox status
        font = QtGui.QFont()
        font.setPointSize(9)
        self.status_groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.status_groupBox.setGeometry(QtCore.QRect(9, 419, 411, 101))
        self.status_groupBox.setFont(font)
        self.status_groupBox.setFlat(False)
        self.status_groupBox.setObjectName("status_groupBox")

        # Label status
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_status = QtWidgets.QLabel(self.status_groupBox)
        self.label_status.setGeometry(QtCore.QRect(0, 32, 411, 51))
        self.label_status.setFont(font)
        self.label_status.setAlignment(QtCore.Qt.AlignCenter)
        self.label_status.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label_status.setObjectName("label_status")

        # Button look
        font = QtGui.QFont()
        font.setFamily("Lucida Console")
        font.setPointSize(11)
        self.button_look = QtWidgets.QPushButton(self.centralwidget)
        self.button_look.setGeometry(QtCore.QRect(70, 310, 131, 61)) # 150, 310, 131, 61
        self.button_look.setFont(font)
        self.button_look.setObjectName("button_look")

        # Button lucky
        self.button_lucky = QtWidgets.QPushButton(self.centralwidget)
        self.button_lucky.setGeometry(QtCore.QRect(230, 310, 131, 61)) # 150, 310, 131, 61
        self.button_lucky.setFont(font)
        self.button_lucky.setText("Feeling lucky")
        self.button_lucky.setObjectName("button_lucky")

        # Label number 1
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_nb1 = QtWidgets.QLabel(self.centralwidget)
        self.label_nb1.setGeometry(QtCore.QRect(10, 145, 181, 31))
        self.label_nb1.setFont(font)
        self.label_nb1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_nb1.setObjectName("label_nb1")

        # Label number 2
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_nb2 = QtWidgets.QLabel(self.centralwidget)
        self.label_nb2.setGeometry(QtCore.QRect(240, 145, 181, 31))
        self.label_nb2.setFont(font)
        self.label_nb2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_nb2.setObjectName("label_nb2")

        # Label title
        font = QtGui.QFont()
        font.setFamily("Perpetua Titling MT")
        font.setPointSize(14)
        self.label_title = QtWidgets.QLabel(self.centralwidget)
        self.label_title.setGeometry(QtCore.QRect(10, 10, 411, 51))
        self.label_title.setFont(font)
        self.label_title.setText("Collatz conjecture")
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title.setObjectName("label_title")

        # Label info
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        self.label_info = QtWidgets.QLabel(self.centralwidget)
        self.label_info.setGeometry(QtCore.QRect(10, 70, 411, 51))
        self.label_info.setFrameShape(QFrame.StyledPanel)
        self.label_info.setFont(font)
        text1 = "- Start with any positive integer n\n"
        text2 = "- If the previous terme is even, the next term is n/2\n"
        text3 = "- If the previous term is odd, the next term is n*3 + 1"
        self.label_info.setText(text1 + text2 + text3)
        self.label_info.setAlignment(QtCore.Qt.AlignCenter)
        self.label_info.setObjectName("label_title")

        # Label version
        self.label_version = QtWidgets.QLabel(self.centralwidget)
        self.label_version.setGeometry(QtCore.QRect(930, 510, 111, 20))
        self.label_version.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_version.setObjectName("label_version")
        
        # Inputs validators
        self.onlyInt = QIntValidator() # Only int validator

        # LineEdit input_1
        font = QtGui.QFont()
        font.setPointSize(25)
        self.input_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.input_1.setGeometry(QtCore.QRect(10, 180, 181, 71))
        self.input_1.setFont(font)
        self.input_1.setValidator(self.onlyInt) # set validator
        self.input_1.setObjectName("input_1")

        # LineEdit input_2
        self.input_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.input_2.setEnabled(False)
        self.input_2.setGeometry(QtCore.QRect(240, 180, 181, 71))
        self.input_2.setFont(font)
        self.input_2.setValidator(self.onlyInt)
        self.input_2.setObjectName("input_2")

        # Checkbox
        self.checkBox_nb2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_nb2.setGeometry(QtCore.QRect(240, 151, 21, 20))
        self.checkBox_nb2.setText("")
        self.checkBox_nb2.setObjectName("checkBox_nb2")

        # Tab -----------------------------------------------
        # TabWidget creation
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(450, 440, 471, 80))
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.South)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setObjectName("tabWidget")

        # Tab 1 creation
        self.tab_nb1 = QtWidgets.QWidget()
        self.tab_nb1.setObjectName("tab_nb1")

        # TextBrowser tab1
        self.text_nb1 = QtWidgets.QTextBrowser(self.tab_nb1)
        self.text_nb1.setGeometry(QtCore.QRect(-1, -1, 469, 58))
        self.text_nb1.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.text_nb1.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.text_nb1.setReadOnly(True)
        self.text_nb1.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.text_nb1.setText("")
        self.text_nb1.setObjectName("text_nb1")

        # Adding tab1
        self.tabWidget.addTab(self.tab_nb1, "")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_nb1),("nb1"))

        # Tab 2 creation
        self.tab_nb2 = QtWidgets.QWidget()
        self.tab_nb2.setObjectName("tab_nb2")

        # TextBrowser tab2
        self.text_nb2 = QtWidgets.QTextBrowser(self.tab_nb2)
        self.text_nb2.setGeometry(QtCore.QRect(-1, -1, 469, 58))
        self.text_nb2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.text_nb2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.text_nb2.setReadOnly(True)
        self.text_nb2.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.text_nb2.setText("")
        self.text_nb2.setObjectName("text_nb2")

        # Adding tab2
        self.tabWidget.addTab(self.tab_nb2, "")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_nb2),("nb2"))
        # Tab -----------------------------------------------

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        #MainWindow.setWindowTitle(_translate("MainWindow", "Syracuse generator"))
        #self.button_save.setText(_translate("MainWindow", "Save the graph ..."))
        self.status_groupBox.setTitle(_translate("MainWindow", "Status message"))
        self.label_status.setText(_translate("MainWindow", "Status message"))
        self.button_look.setText(_translate("MainWindow", "Have a look"))
        self.label_nb1.setText(_translate("MainWindow", "Number 1"))
        self.label_nb2.setText(_translate("MainWindow", "Number 2"))
        #self.label_title.setText(_translate("MainWindow", "Syracuse generator"))
        self.label_version.setText(_translate("MainWindow", "V. 0.5"))
        #self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_nb1), _translate("MainWindow", "nb1"))
        #self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_nb2), _translate("MainWindow", "nb2"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())