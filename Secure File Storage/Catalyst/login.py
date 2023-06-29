#user login check
mail_id='hp@gmail.com'
password='123'
user_details=datastore_service.get_table_details("UserDetails").get_paged_rows()['data']
# print(user_details)
for i in user_details:
    if(i["Mail_id"]==mail_id and i['Password']==password):
        print("success")
else:
    print("Invalid details")


#signup
mail_id='hp123@gmail.com'
password='123'
user_id='1'
name='hari'
data={ 'Mail_id': mail_id,  'User_id': user_id, 'Name': name, 'Password': password}
response=datastore_service.get_table_details("UserDetails").insert_row(data)
print(response)