# This Python file uses the following encoding: utf-8
import sys
import cv2
from PySide6.QtWidgets import QApplication, QWidget, QFileDialog, QLabel
from PySide6.QtGui import QPixmap, Qt, QImage, QColor, qRgb
from matplotlib import pyplot
import numpy as np

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Widget

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.Read)
        self.ui.btn_color.clicked.connect(self.Color_RGB)
        self.ui.btn_gray.clicked.connect(self.Gray)
        self.ui.btn_blur.clicked.connect(self.Blur)
        self.ui.btn_size.clicked.connect(self.Size)
        self.ui.btn_save.clicked.connect(self.Save)
        self.picture = QPixmap
        self.file = QFileDialog

    def Read(self):
         file, _ = QFileDialog.getOpenFileName(None, "Select image file", "", "Image Files (*.jpg);;Image Files (*.png);;All Files (*)")
         if file:
             pixmap = QPixmap(file)
             self.picture = pixmap
             self.file = file

             width = pixmap.width()
             height = pixmap.height()
             self.ui.label_2.setText(f'Width: {width}, Height: {height}')
             self.ui.label.setPixmap(pixmap)
             self.ui.label.setScaledContents(True)
             self.ui.label.setAspectRatioMode(Qt.IgnoreAspectRatio)

    def Color_RGB(self):
        img = cv2.imread(self.file)
        if img is not None:
            channels = cv2.split(img)
            colors = ('b', 'g', 'r')

            fig, axes = pyplot.subplots(3, 1, figsize=(8, 6))

            for i, channel in enumerate(channels):
                hist = cv2.calcHist([channel], [0], None, [256], [0, 256])
                axes[i].plot(hist, color=colors[i])
                axes[i].set_xlim([0, 256])
                axes[i].set_ylim([0, hist.max()])

            pyplot.tight_layout()
            pyplot.show()

    def Gray(self):
        image = self.picture.toImage()
        gray_image = image.convertToFormat(QImage.Format_Grayscale8)
        grayscale_pixmap = QPixmap.fromImage(gray_image)
        self.ui.label.setPixmap(grayscale_pixmap) 
        self.picture = grayscale_pixmap

    def Blur(self):
        image = self.picture.toImage()
        width = image.width()
        height = image.height()
        buffer = image.bits().tobytes()
        image_np = np.frombuffer(buffer, dtype=np.uint8).reshape((height, width, 4))

        image_bgr = cv2.cvtColor(image_np, cv2.COLOR_RGBA2RGB)
        blue_channel, green_channel, red_channel = cv2.split(image_bgr)

        filter_matrix = np.array([[1, 0, 1], [0, 1, 0], [1, 0, 1]], dtype=np.float32) / 5
        filtered_blue_channel = cv2.filter2D(blue_channel, -1, kernel=filter_matrix)
        filtered_green_channel = cv2.filter2D(green_channel, -1, kernel=filter_matrix)
        filtered_red_channel = cv2.filter2D(red_channel, -1, kernel=filter_matrix)

        filtered_image_bgr = cv2.merge([filtered_blue_channel, filtered_green_channel, filtered_red_channel])
        filtered_image = QImage(filtered_image_bgr.data, filtered_image_bgr.shape[1], filtered_image_bgr.shape[0], QImage.Format_BGR888)
        filtered_pixmap = QPixmap.fromImage(filtered_image)

        self.ui.label.setPixmap(filtered_pixmap) 
        self.picture = filtered_pixmap
        

    def Size(self):
        user_width = int(self.ui.lineEdit.text())
        user_height = int(self.ui.lineEdit_2.text())

        resized_image = self.picture.scaled(user_width, user_height)
        width = resized_image.width()
        height = resized_image.height()
        self.ui.label_2.setText(f'Width: {width}, Height: {height}')
        self.ui.label.setPixmap(resized_image) 
        self.picture = resized_image

    def Save(self):
        file_path = "E:\p.jpg"
        self.picture.save(file_path, "JPG")




if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
