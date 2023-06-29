import json

from flask import Flask, request, render_template, jsonify, send_file, make_response

import os
import enc
from stegano import lsb
from stegano.lsb import generators
import Mail
import dec
import Catalyst.app as catalyst

app = Flask(__name__)

#interceptor
@app.before_request
def before_request_func():

    if(  request.path=="/download" or request.path=="/upload"):
        cookie=request.cookies.get('Auth')
        if(cookie!= None and catalyst.checkAuth(cookie)):
            pass
        else:
            return render_template('main.html', flash_message="False")


#####Home Page#######
@app.route('/')
def index():
    return render_template('main.html', flash_message="False")


### Back To Choice#####
@app.route('/back2choice', methods=["POST", "GET"])
def back2choice():
    return render_template('choice.html', flash_message="False")


###Encryption Page###
@app.route('/upload', methods=["GET", 'POST'])
def upload():
    return render_template("encrypt.html")


### BACK TO LOGIN PAGE###
@app.route('/log_out', methods=["POST", "GET"])
def logout():
    basepath = os.path.dirname(__file__)
    filepath1 = os.path.join(basepath, 'uploads/files')
    filepath2 = os.path.join(basepath, 'uploads/images/steganographed_img')
    filepath3 = os.path.join(basepath, 'Download/files')
    filepath4 = os.path.join(basepath, 'Download/images')

    catalyst.clearFolders(filepath1)
    catalyst.clearFolders(filepath2)
    catalyst.clearFolders(filepath3)
    catalyst.clearFolders(filepath4)
    return render_template("main.html", flash_message="False")


### DECRYPTION PAGE###
@app.route('/download', methods=["POST", "GET"])
def download():
    return render_template("decrypt.html")


### Login form authentication #####
@app.route("/login_form", methods=["GET", "POST"])
def login():
    flag = True
    if request.method == "POST":
        mailid = request.form["mailid"]  ## mail id
        password = request.form["password"]  ## password

        data = {'Mail_id':mailid,'Password':password}### Json data of login details
        flag = catalyst.loginCheck(data)
        if flag == True:  ## Function call
            resp = make_response(render_template("choice.html", flash_message="False"))

            resp.set_cookie('Auth', catalyst.setCookie(mailid,password))
            return resp


        else:
            # error = "Invalid username or password. Please try again."
            print("login details worng")
            return render_template('main.html', flash_message="True") #error


#### sign in form registration ####
@app.route("/sign_form", methods=["POST"])
def sign():
    flag = True
    if request.method == "POST":
        ### Getting the sign in details as {mail: gmail,name:hhh,pass:123}
        data = request.json #get json in data variable

        flag=catalyst.Signup(data)
        if flag == True:

            return json.dumps({'success':True}), 200, {'ContentType':'application/json'}  #render_template('main.html')

        else:

            error = "User details already existing "
            return False
            # return render_template("main.html", error=error)
            # return "Sign in Fail!!!"


### Sending files and getting inputs from the webpage  decryption ####
@app.route('/decrypt_json', methods=['POST', 'GET'])
def receiverroute():
    cookie = request.cookies.get('Auth')
    if request.method == 'GET':
        files = catalyst.FileList(cookie) #[{'name':'hk.pdf','id':1},{'name':"Harish.pdf",'id':2},{'name':"enc.py",'id':3}]###need files with name and id
        receivers=[]
        for i in files:
            receivers.append(i['name'])
        return jsonify(receivers)
    else:

        files = catalyst.FileList(cookie) # [{'name': 'hk.pdf', 'id': 1}, {'name': "Harish.pdf", 'id': 2}, {'name': "enc.py", 'id': 3}]### need function call
        image = request.files['image-upload']
        file_recv = request.form['dropdown_receiver']

        basepath = os.path.dirname(__file__)
        imagepath = os.path.join(basepath, 'Download/images', image.filename)
        image.save(imagepath)

        file_data = lsb.reveal(imagepath, generators.eratosthenes())

        print("steganogrpahd",file_data)

        key=dec.main(file_data)
        print("key",key)

        for i in files:#### retreiving the id and sending the key and id in json
            if i['name']==file_recv:
                data={'key':key,'id':i['id'],'file_name':file_recv}
                print(data)
                if(catalyst.downloadFile(data)):
                    filepath = os.path.join(basepath, 'Download', 'files', file_recv)
                    print(filepath)

                    return send_file(filepath, as_attachment=True)

                #return data you can get the json file here
        return "<h1> Invalid data</h1>"



@app.route('/upload1', methods=['GET'])
def upload21():
    if request.method == 'GET':
        ###Sending the existing user to dropdown #####
        existing_users = catalyst.Userlist()#{'user': ['harikrish0122001@gmail.com', "harishrethinam@gmail.com", 'hariprabhu2323@gmail.com','ok@gmail.com']}
        return jsonify(existing_users)


### getting inputs from  encryption page ####
@app.route('/upload1', methods=['POST'])
def upload1():
    if request.method == 'POST':
        options=request.form.getlist('options')
        file = request.files['file--upload']
        image = request.files['img--upload']
        key = request.form['key']
        print("options ---",options)

        ##encrypting the entered key by passing the key encryption module
        encrypted_key = enc.main(key)

        ## obtaining the basepath or directory
        basepath = os.path.dirname(__file__)
        # print(basepath)

        ## saving the file
        filepath = os.path.join(basepath, 'uploads/files', file.filename)
        file.save(filepath)

        # saving the image and steganography process
        imagepath = os.path.join(basepath, 'uploads/images', image.filename)
        image.save(imagepath)
        catalyst.renaming_format(imagepath)
        file_name= image.filename.split(".")[0]+".png"
        print(file_name,"---------")
        imagepath=imagepath.split(".")[0]+".png"
        hide = lsb.hide(imagepath, encrypted_key, generators.eratosthenes())
        imagepath1 = os.path.join(basepath, 'uploads/images/steganographed_img', 'steganographed_' + file_name) #renaming the file name as steganographed_file name in order to differntitate the normal image and steg image
        hide.save(imagepath1)

        ## setting path

        #path = 'C:/Users/harik/Secure-File-Storage-On-Cloud-Using-Hybrid-Cryptography/Final Yr/uploads/images/steganographed_img'
        path=os.path.join(basepath,'uploads/images/steganographed_img')
        for filename in os.listdir(path):
            if filename == ("steganographed_" + file_name):
                # checking the file name
                Mail.mail(filename,options,file.filename)
                break

        data = {'key': key, 'receivers': options, 'file_name':file.filename}
        cookie = request.cookies.get('Auth')
        flag=catalyst.uploadFile(data,cookie)
        if flag==True:

            return render_template('choice.html', flash_message="True"),"<script> alert('mail sent successfully ') </script>"
        

        return "<script> alert('error ') </script>"



if __name__ == '__main__':
    app.run(port=os.getenv('X_ZOHO_CATALYST_LISTEN_PORT'),host="0.0.0.0")
    #port=9000,host=0.0.0.0