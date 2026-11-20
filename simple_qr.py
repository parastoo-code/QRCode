import qrcode

img = qrcode.make('https://www.google.com')

img.save('simple_qr.png')
