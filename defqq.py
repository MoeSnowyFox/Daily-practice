import requests
import json
from io import BytesIO
from PIL import Image

def grpostmess( grid , messages , port ):
   messages =  messages

   url = "http://127.0.0.1:"+str(port)+"/send_group_msg"                      

   headers = {"content-type":"application/json",'Connection':'close'}

   mess = {"group_id":grid ,"message":messages}


   res = requests.post(url, json = mess,headers=headers)


   print (res.text)
   return(res.text)

def prpostmess( prid , messages , port ):
   messages =  messages

   url = "http://127.0.0.1:"+str(port)+"/send_private_msg"                      

   headers = {"content-type":"application/json",'Connection':'close'}

   mess = {"user_id":prid ,"message":messages}


   res = requests.post(url, json = mess,headers=headers)


   print (res.text)
   return(res.text)

def grmd(grid , mdmessages , port):
   mdmessages = mdmessages

   url = "http://127.0.0.1:"+str(port)+"/send_forward_msg"                            

   headers = {"content-type":"application/json"}

   mess = {"messages":mdmessages}

   res = requests.post(url, json = mess,headers=headers)

   #print(res.text) 

   json_message = json.loads(res.text)["data"]

   grpostmess ( grid=grid, messages= [{"type": "longmsg","data": { "id": json_message}}], port = port )

def prmd(prid , mdmessages , port):
   mdmessages = mdmessages

   url = "http://127.0.0.1:"+str(port)+"/send_forward_msg"                            

   headers = {"content-type":"application/json"}

   mess = {"messages":mdmessages}

   res = requests.post(url, json = mess,headers=headers)

   #print(res.text) 

   json_message = json.loads(res.text)["data"]

   prpostmess ( prid=prid, messages= [{"type": "longmsg","data": { "id": json_message}}], port = port )



def get_pic_width(url):
    response = requests.get(url)
    image = Image.open(BytesIO(response.content), 'r')
    return image.width

def get_pic_heigth(url):
    response = requests.get(url)
    image = Image.open(BytesIO(response.content), 'r')
    return image.height








#json_message = "RhLA\u002BIdqpnbjHd3m33jHFJDWiscmmnv7wd94awvzqm46pemvVPSdRlSUQDROMPYA"

#message = [{"type": "longmsg","data": { "id": json_message}}]

