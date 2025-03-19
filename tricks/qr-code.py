# pip install pyqrcode
# pip install pypng
import pyqrcode
import png
from pyqrcode import QRcode

s = "www.someurl.com"
url = pyqrcode.create(s)
url.svg("myqr.svg", scale = 8)
url.png("myqr.png", scale = 6)