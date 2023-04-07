import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QLineEdit, QMessageBox
import joblib
from joblib import load
from sklearn.ensemble import RandomForestClassifier


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Classification Model Predictor')
        self.setGeometry(300, 300, 300, 150)
        self.initUI()
        self.model = self.load_model()

    def initUI(self):
        self.label1 = QLabel(self)
        self.label1.setText('age:')
        self.label1.move(50, 50)
        self.textbox1 = QLineEdit(self)
        self.textbox1.move(150, 50)
        self.textbox1.resize(200, 20)

        self.label2 = QLabel(self)
        self.label2.setText('gendera:')
        self.label2.move(50, 80)
        self.textbox2 = QLineEdit(self)
        self.textbox2.move(150, 80)
        self.textbox2.resize(200, 20)

        self.label3 = QLabel(self)
        self.label3.setText('BMI:')
        self.label3.move(50, 110)
        self.textbox3 = QLineEdit(self)
        self.textbox3.move(150, 110)
        self.textbox3.resize(200, 20)       

        self.label4 = QLabel(self)
        self.label4.setText('depression:')
        self.label4.move(50, 140)
        self.textbox4 = QLineEdit(self)
        self.textbox4.move(150, 140)
        self.textbox4.resize(200, 20)

        self.label5 = QLabel(self)
        self.label5.setText('temperature:')
        self.label5.move(50, 170)
        self.textbox5 = QLineEdit(self)
        self.textbox5.move(150, 170)
        self.textbox5.resize(200, 20)

        ########################################

        self.button = QPushButton('Predict', self)
        self.button.move(150, 300)
        self.button.clicked.connect(self.on_button_click)

        self.show()

    def load_model(self):
        with open('diab.pkl', 'rb') as f:
            model = joblib.load(f)
        return model

    def on_button_click(self):
        var1 = float(self.textbox1.text())
        var2 = int(self.textbox2.text() )       
        var3 = int(self.textbox3.text())
        var4 = float(self.textbox4.text())
        var5 = int(self.textbox5.text())       


        prediction = self.model.predict([[var1, var2, var3, var4, var5]])
        
        if prediction[0]==0:
            pred = "No diabete"
        else:
            pred = "Diabete"        
        QMessageBox.information(self, 'Prediction', pred)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    #♂window.show()
    sys.exit(app.exec_())
