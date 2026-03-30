from PyQt5.QtWidgets import QApplication, QWidget, QLabel

app = QApplication([])

window = QWidget()
window.setWindowTitle("Label Example")
window.setGeometry(100, 100, 300, 200)

label = QLabel("Hello Student!", window)
label.move(80, 80)   # position set pannum

window.show()
app.exec_()
