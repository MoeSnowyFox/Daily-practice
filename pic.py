from flask import Flask, request 
import defqq
 
#写着玩玩~




app = Flask(__name__)

 
 
@app.route('/',methods=['post'])#指定端口的地址以及通信方式
def add_post():
        #print(request.json)   
        data=request.json   
        mess = ' '.join([item['data']['text'] for item in data['message'] if item['type'] == 'text'])
        print(mess)
        sender_user_id = data.get('sender', {}).get('user_id')
        if data.get('message_type', {}) == "private" :
           print(sender_user_id)
           if mess[:2] == "图片":
               picurl = mess[2:]
               print(picurl)
               pic = "[图片 #" +str(defqq.get_pic_width(picurl)) +"px#"+str(defqq.get_pic_heigth(picurl))+"]("+picurl+")"


               mdmessage = [{
                "type": "node",
                "data": {
                  "name": "testbot",
                  "uin": "10001",
                  "content": [{
                    "type": "markdown",
                    "data": {
                      "content": "{\"content\":\" \\n!" +pic +" \"}"
                        }
                    }]
                    }
                  }]
               defqq.prmd(prid = sender_user_id , mdmessages = mdmessage , port = 1436)

           else:
            picurl = "null"
            defqq.prpostmess(prid = sender_user_id , messages = "嗯哼~" , port = 1436)

        return('404')    



if __name__ == '__main__':
    app.run(host='127.0.0.1',port=8082)
    #指定地址和端口号   当前为127.0.0.1:8090/onebot/post  请在onebot配置中输入此项以接受消息