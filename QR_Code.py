#Steps to buils this project 
# ==> 1- (Import) 
# ==> 2- (Configuration) 
# ==> 3- (Add Data) 
# ==> 4- (Build) 
# ==> 5- (Save)


# import the (qrcode) library to generate the QRCode images (Import)
import qrcode

# list of emails which i want to create qrcode images for them
list_of_emails = ["https://www.kaggle.com/youssefayman22","https://www.linkedin.com/in/youssef-ayman11/?skipRedirect=true","https://github.com/youssefayman55"]

# create the QRCode object with 4 attributes (Configuration)
qr = qrcode.QRCode(version = 2 , # size of code of qrcode
                   error_correction = qrcode.constants.ERROR_CORRECT_H, #highest error correction علشان دا احسن حاجه بيصحح الاخطاء
                   box_size = 5 , # size of box of qrcode
                   border  = 2) # the space around the qrcode


for i , url in enumerate(list_of_emails):

    # make sure that is not any qrcode images
    qr.clear()


    # qrcode object will generate qrcode image for this channel (Add Data)
    qr.add_data(url)

    # qrcode will generate the  image (Build)
    qr.make( fit = True )

    # setting the image color (style)
    img = qr.make_image( fill_color = "red" , back_color = "white")

    # save the qrcode inmage (Save)
    img.save(f"QRCode_Image_{i+1}.png")


