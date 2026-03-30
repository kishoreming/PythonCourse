from PyQt5.QtWidgets import QApplication, QWidget, QPushButton

app = QApplication([])

window = QWidget()
window.setWindowTitle("Signal Slot Simple")

button = QPushButton("Click Me", window)
button.move(80, 50)

# SLOT (function)
def say_hello():
    print("Hello! Button Clicked")

# SIGNAL → SLOT connection
button.clicked.connect(say_hello)

window.show()
app.exec_()