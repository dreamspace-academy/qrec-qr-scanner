
import pyqrcode
import png
from pyqrcode import QRCode

msg=("SWL - 04")

url = pyqrcode.create(msg)
 
url.png('myqr2.png', scale = 6)

