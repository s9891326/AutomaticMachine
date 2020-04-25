# import sys
# from PyQt5.QtWidgets import QApplication, QWidget, QLabel
# from PyQt5.QtGui import QIcon, QPixmap
#
#
# class MainWindow(QWidget):
#     def __init__(self, image):
#         self.app = QApplication(sys.argv)
#         super().__init__()
#         self.image = image
#         self.title = 'hancock'
#         self.left = 1000
#         self.top = 100
#         self.width = 640
#         self.height = 480
#
#     def setupUi(self):
#         self.setWindowTitle(self.title)
#         self.setGeometry(self.left, self.top, self.width, self.height)
#
#         label = QLabel(self)
#         pixmap = QPixmap(self.image)
#         label.setPixmap(pixmap)
#         self.resize(pixmap.width(), pixmap.height())
#         self.show()
#         sys.exit(self.app.exec_())
#
#
# # if __name__ == "__main__":
#     # print("22")
#     # app = QApplication(sys.argv)
#     # MainWindow = MainWindow(image="../Hancock.jpg")
#     # sys.exit(app.exec_())