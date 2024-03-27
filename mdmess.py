import defqq

url = "https://goss.veer.com/creative/vcg/veer/800water/veer-307487922.jpg"

pic = "[图片 #" +str(defqq.get_pic_width(url)) +"px#"+str(defqq.get_pic_heigth(url))+"]("+url+")"


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


defqq.grmd(grid = 829296181 , mdmessages = mdmessage , port = 1436)

print(pic)