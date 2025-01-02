#install the labires needed 
# caete a  fubnvtuin thst colleccrrrt= the rtexta and converts it to ar cide
#save the qr code as an image 
#run fi=unction
#import qrcode.constants
import qrcode
import qrcode.constants

def generate_qrcode(text):
#configure the QRcode
    qr=qrcode.QRCode(
        version=7,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=15,
        border=5,

    )
#adding the data to the QRcode
    qr.add_data(text)
    qr.make(fit=True)
#genrating & saving the qr image
    img=qr.make_image(fill_color="black",back_color="white")
    img.save("img01.png")
data=input("enter the data to the QRcode")
generate_qrcode(data)

