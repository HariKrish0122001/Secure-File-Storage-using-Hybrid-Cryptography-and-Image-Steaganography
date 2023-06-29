from email.message import EmailMessage
import ssl
import smtplib
import os
import base64
from PIL import Image

def mail(img,options,filename):
    path = '/Users/hari-pt6161/Downloads/appengine/uploads/images/steganographed_img'


    file_data=os.path.join(path,img)




    sender="123@gmail.com"
    send_password="passkey"

    eamil_rec=options

    sub="From secure Storage"
    print("pathhh ====",file_data)
    em=EmailMessage()
    em['From']=sender
    em['To']=eamil_rec
    em['Subject']=sub
    em.set_content(" Your're encrypted image for this :"+filename)

    with open(file_data,'rb') as f:
        img_data=f.read()
    em.add_attachment(img_data,maintype="image",subtype="png",filename=img)



    context=ssl.create_default_context()
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE

    with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
        smtp.login(sender,send_password)
        smtp.sendmail(sender,eamil_rec,em.as_string())
        print("successfully Sent")

