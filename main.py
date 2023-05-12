from controller import *


def main():
    app = QApplication([])
    window = Controller()
    window.setWindowTitle('Bear Quiz')
    window.setWindowIcon(QtGui.QIcon('bear.png'))
    window.setFixedSize(890,852)
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
