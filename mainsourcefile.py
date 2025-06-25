import qrcode 
from pyzbar.pyzbar import decode
from PIL import Image, ImageDraw,ImageFilter

import qrcode.constants
# Input link to generate QR Code
myqr = qrcode.make("https://dcsa.puchd.ac.in/show-biodata.php?qstrempid=2819&qstrempdesigcode=10")
# Replace with your desired URL
myqr.save("myqr.png", scale = 6) #qr code 1 genrated

myqr2 = qrcode.make("https://www.artofliving.org/programs")
myqr2.save("myqr2.png" , scale = 8) #qr code 2 genrated

qr = qrcode.QRCode(version =1,  # Size of the QR Code
                     error_correction = qrcode.constants.ERROR_CORRECT_H, # Error correction
                     box_size = 10, #each boc in 10*10 pixels
                     border = 4)
qr.add_data("https://puchd.ac.in/") # Add the link to the QR Code
qr.make(fit=True)# optimize QR Code size

# Generate the QR Code image
img = qr.make_image(fill_color="red", back_color ="white") # qr with red color
img.save("qr.png")# Save the QR Code image
print("QR Code generated")




#decoding qr into link
b = decode(Image.open("myqr2.png"))
print(b[0].data.decode("ascii"))

def designed_qrCode(data,filemane):
    qr = qrcode.QRCode(
             version=1,
             error_correction= qrcode.constants.ERROR_CORRECT_H,
             box_size = 10,
             border=2
    )
    qr.add_data(data)
    qr.make(fit = True)


data = "https://puchd.ac.in/"
filename = "designed_qrCode.png"
qr_image = qr.make_image(fill_color="white", back_color="black" ).convert("RGBA")
   
  #create a circular grtadient overlay
overlay = Image.new ("RGBA", qr_image.size)
draw = ImageDraw.Draw(overlay)
center_x, center_y = qr_image.width //2, qr_image.height // 2
radius = min(qr_image.width, qr_image.height) //2

for r in range(radius,0,-1):
    alpha = int(255 * (1 - r / radius))
    color = (247,212,54,alpha)
    draw.ellipse(
        (center_x - r, center_y - r, center_x + r, center_y + r),
        fill = color, 
        outline =  None
    )
qr_image = Image.alpha_composite(qr_image,overlay)
qr_image.save(filename)

designed_qrCode(data, filename)