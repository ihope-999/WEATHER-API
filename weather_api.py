from info_file import api_key
import requests
import json

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QApplication, QLineEdit, QPushButton, QLabel, QVBoxLayout, QHBoxLayout


class WeatherForecast(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Weather App')
        self.line_edit = QLineEdit(self)
        self.button = QPushButton('Enter',self)
        self.baseurl = 'weather_icon/'
        self.label = QLabel(self)
        self.label1 = QLabel(self)
        self.label2 = QLabel(self)
        self.label3 = QLabel(self)
        self.label4 = QLabel(self)

        self.initIU()

    def initIU(self):
        self.vbox = QVBoxLayout()
        self.hbox = QHBoxLayout()
        self.vbox.addWidget(self.label1)
        self.vbox.addWidget(self.label2)
        self.vbox.addWidget(self.label3)
        self.vbox.addWidget(self.label4)
        self.setLayout(self.vbox)

        self.hbox.addWidget(self.line_edit)
        self.hbox.addWidget(self.button)
        self.hbox.addWidget(self.label)


        self.vbox.addLayout(self.hbox)
        self.label.setStyleSheet('background-color: hsl(264, 46%, 10%)')

        self.line_edit.setPlaceholderText('Enter the city: ')

        self.button.clicked.connect(self.clicked_on)
    def temp_converter(self,data,kelvin):
        celcius = ( int( data['main']['temp'] )- 273 )
        return celcius
    def clicked_on(self):
        self.get_data(self.line_edit.text())
    def get_info(self,city_name):
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}'
        response = requests.get(url)
        response = response.json()
        return response
    def create_pixmap(self,url):
        whole_url = f'weather_icon/{url}'
        self.pixmap = QPixmap(whole_url)
        self.label.setPixmap(self.pixmap)

    def weather_image(self,description):
        data = self.get_info(self.line_edit.text())
        match(data['weather'][0]['icon']):
            case '01d':
                url = '01d.png'
                self.create_pixmap(url)
            case '01n':
                url = '01d.png'
                self.create_pixmap(url)
            case '02d':
                url = '02d.png'
                self.create_pixmap(url)
            case '02n':
                url = '02n.png'
                self.create_pixmap(url)
            case '03d':
                url = '03d.png'
                self.create_pixmap(url)
            case '03n':
                url = '03n.png'
                self.create_pixmap(url)
            case '04d':
                url = '04d.png'
                self.create_pixmap(url)
            case '04n':
                url = '04n.png'
                self.create_pixmap(url)
            case '10d':
                url = '10d.png'
                self.create_pixmap(url)
            case '50d':
                url = '50d.png'
                self.create_pixmap(url)
            case '50n':
                url = '50n.png'
                self.create_pixmap(url)
            case '50n':
                url = '50n.png'
                self.create_pixmap(url)



    def get_data(self,city_name):
        data = self.get_info(city_name)
        if data:
            self.label1.setText(f'The weather in {city_name} is {data['weather'][0]['main']}')
            self.label2.setText(f'How it seems like: {data['weather'][0]['description']}')
            self.label3.setText(f'The icon is: {data['weather'][0]['icon']}')
            self.label4.setText(f'The temperature is:  {self.temp_converter(data,data['main']['temp'] )} C ')
            self.weather_image(data['weather'][0]['description'])



def main():
    app  = QApplication(sys.argv)
    window = WeatherForecast()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
