from PyQt5.QtWidgets import *
from view import *

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


class Controller(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        # Default button selection
        self.red_radioButton.setChecked(True)
        self.hiphop_radioButton.setChecked(True)
        self.taco_radioButton.setChecked(True)
        self.coffee_radioButton.setChecked(True)

        # submit and reset buttons
        self.submit_pushButton.clicked.connect(lambda: self.submit())
        self.reset_pushButton.clicked.connect(lambda: self.reset())

    # when submit button is called
    def submit(self):
        # different bears
        garden = 0
        cowgirl = 0
        sk8 = 0
        swag = 0

        # color selection group
        if self.red_radioButton.isChecked():
            cowgirl = cowgirl + 1
        elif self.yellow_radioButton.isChecked():
            swag = swag + 1
        elif self.blue_radioButton.isChecked():
            sk8 = sk8 + 1
        else:
            garden = garden + 1

        # music selection genre group
        if self.country_radioButton.isChecked():
            cowgirl = cowgirl + 1
        elif self.hiphop_radioButton.isChecked():
            swag = swag + 1
        elif self.rock_radioButton.isChecked():
            sk8 = sk8 + 1
        else:
            garden = garden + 1

        # food selection group
        if self.taco_radioButton.isChecked():
            cowgirl = cowgirl + 1
        elif self.ramen_radioButton.isChecked():
            swag = swag + 1
        elif self.curry_radioButton.isChecked():
            sk8 = sk8 + 1
        else:
            garden = garden + 1

        # drink selection group
        if self.icedtea_radioButton.isChecked():
            cowgirl = cowgirl + 1
        elif self.coffee_radioButton.isChecked():
            swag = swag + 1
        elif self.soda_radioButton.isChecked():
            sk8 = sk8 + 1
        else:
            garden = garden + 1

        # Deciding what bear to output onto the window.
        # Output is cowgirl
        if (cowgirl > swag) and (cowgirl > sk8) and (cowgirl > garden):
            self.outtieImage_label.setPixmap(QtGui.QPixmap('cowgirlBear.jpg'))
            self.outtieText_label.setText('You are Yeehaw Bear!')
        # Output is swag
        elif (swag > cowgirl) and (swag > sk8) and (swag > garden):
            self.outtieImage_label.setPixmap(QtGui.QPixmap('swagBear.jpg'))
            self.outtieText_label.setText('You are Swag Bear!')
        # Output is sk8
        elif (sk8 > cowgirl) and (sk8 > swag) and (sk8 > garden):
            self.outtieImage_label.setPixmap(QtGui.QPixmap('sk8Bear.jpg'))
            self.outtieText_label.setText('You are Sk8r Bear!')
        # Output is garden
        elif (garden > cowgirl) and (garden > swag) and (garden > sk8):
            self.outtieImage_label.setPixmap(QtGui.QPixmap('gardenBear.jpg'))
            self.outtieText_label.setText('You are Green Thumb Bear!')
        # Output if all are equal
        elif (cowgirl == swag) and (cowgirl == sk8) and (cowgirl == garden):
            self.outtieImage_label.setPixmap(QtGui.QPixmap('divaBear.jpg'))
            self.outtieText_label.setText('You are Diva Bear!')
        # Outputs if attribute is equal to cowgirl
        # Truck bear
        elif (cowgirl == garden) and (swag == 0) and (sk8 == 0):
            self.outtieImage_label.setPixmap(QtGui.QPixmap('truckBear.jpg'))
            self.outtieText_label.setText('You are Trucker Bear!')
        # Gamble bear
        elif (cowgirl == swag) and (garden == 0) and (sk8 == 0):
            self.outtieImage_label.setPixmap(QtGui.QPixmap('vegasBear.jpg'))
            self.outtieText_label.setText('You are Gamble Bear!')
        # Berry bear
        elif (cowgirl == sk8) and (garden == 0) and (swag ==0):
            self.outtieImage_label.setPixmap(QtGui.QPixmap('strawberryBear.jpg'))
            self.outtieText_label.setText('You are Berry Bear!')
        # Output if attribute is equal to garden
        # Fashion bear
        elif (garden == swag) and (sk8 == 0) and (cowgirl == 0):
            self.outtieImage_label.setPixmap(QtGui.QPixmap('fashionBear.jpg'))
            self.outtieText_label.setText('You are Fashion Bear!')
        # Hipster bear
        elif (garden == sk8) and (cowgirl == 0) and (swag == 0):
            self.outtieImage_label.setPixmap(QtGui.QPixmap('hipsterBear.jpg'))
            self.outtieText_label.setText('You are Hipster Bear!')
        # Output if attribute is equal to swag
        # Biker bear
        elif (swag == sk8) and (cowgirl == 0) and (garden == 0) :
            self.outtieImage_label.setPixmap(QtGui.QPixmap('rockerBear.jpg'))
            self.outtieText_label.setText('You are Biker Bear!')
        # Output for just in case I missed a probability
        else:
            self.outtieImage_label.setPixmap(QtGui.QPixmap('clownBear.jpg'))
            self.outtieText_label.setText('You are Clown Bear!')

    # Resetting the screen
    def reset(self):
        self.outtieImage_label.setPixmap(QtGui.QPixmap('questions.jpg'))
        self.outtieText_label.setText('Click "Submit" to see what bear you are!')
        self.red_radioButton.setChecked(True)
        self.hiphop_radioButton.setChecked(True)
        self.taco_radioButton.setChecked(True)
        self.coffee_radioButton.setChecked(True)
