# pip install wifi_qrcode_generator
import wifi_qrcode_generator as qr

qrCode = qr.wifi_qrcode('название WIFI', False, 'WPA', 'пароль')  
qrCode.show()

qrCode.save("my_wifi_qr.png")
