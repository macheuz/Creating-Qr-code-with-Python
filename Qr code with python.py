import qrcode

data = 'www.google.com'
img = qrcode.make(data)
img.save('/Users/mazo/Vianna/google')