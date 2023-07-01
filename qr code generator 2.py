import qrcode  #qrcode is a module
from PIL import Image  #PIl is Python Imaging Library with Image as its module

#this line generates qrcode object 'qr' with settings specified
qr=qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=10,border=5)
#QRCode is used to change functionality of qr code

#data is then added to that object
qr.add_data("https://www.w3schools.com")

#only if data is present in qr then only qrcode will be generated
qr.make(fit=True)

#with qr object containing data to be converted to qrcode make_image function takes parameters for the image and stores it in img
img=qr.make_image(fill_color='red',back_color='white')

#img is then saved
img.save('w3schools_qr.png')


