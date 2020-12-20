import qrcode


qr = qrcode.QRCode(version = 1 , box_size=15 , border=5)

# The version parameter is an integer from 1 to 40 that controls the size of the QR Code 
#(the smallest, version 1, is a 21x21 matrix).

#Set to None and use the fit parameter when making the code to determine this automatically.

#The box_size parameter controls how many pixels each “box” of the QR code is.

#The border parameter controls how many boxes thick the border should be 
#(the default is 4, which is the minimum according to the specs).

#fill_color and back_color can change the background and the painting color of the QR, 
#when using the default image factory.

# img.save is for saving the qrcode made inside a png.


data =  ""
qr.add_data(data)
qr.make (fit = True) ## makes the size changable
img = qr.make_image(fill = 'black' , back_color= 'white' )## making the qr code
img.save("pcme.png")
