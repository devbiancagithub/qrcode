import qrcode

attributes = qrcode.QRCode(version=1,box_size=30, border=5)
attributes.add_data('https://www.youtube.com/watch?v=REyv4cblksI')
attributes.make(fit=True)

qrcode_image = attributes.make_image(fill_color="black", back_color="white")
qrcode_image.save('SongQRCode.png')