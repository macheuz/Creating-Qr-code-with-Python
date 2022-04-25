import qrcode

data = input('Write the site you need to create a Qr code: ')
img = qrcode.make(data)
img.save('/Users/mazo/Vianna/google')
