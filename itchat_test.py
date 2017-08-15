# -*- coding:utf-8 -*-
import itchat
itchat.auto_login(hotReload=True)   # 可以暂存登陆状态
friend = itchat.search_friends(u"爱自由")[0]     # 搜索内容的字符串格式需要是unicode
print friend["UserName"]

# 发送内容需要是unicode，发送人也要是unicode
# itchat.send_msg("nihao", friend["UserName"])
# 发送路径需要是unicode,发送人需要是unicode，文件名不可以是中文（如果使用fields.py替换requests包中的文件，可以增加中文支持）
# itchat.send_image("xiaoqiao.jpeg", friend["UserName"])
# 发送路径需要是unicode,发送人需要是unicode，文件名不可以是中文（如果使用fields.py替换requests包中的文件，可以增加中文支持）
# itchat.send_file("xiaoqiao.jpeg", friend["UserName"])
# 发送路径unicode，发送人unicode，文件名不可以是中文，网页版发送大小不能超过20M
# itchat.send_video("你好.mp4".decode("utf-8"), friend["UserName"])
"""
    如果单纯的使用send函数，需要对发送内容进行标注。
    @fil@：在发送内容前添加，表明是发送文件
    @img@：在发送内容前添加，表明是图片文件
    @msg@：在发送内容前添加，表明是消息
    @vid@：在发送内容前添加，表明是视频文件，视频文件要小于20M
    如果什么都没有添加，默认是消息

"""
# itchat.send("nihao", friend["UserName"])
# chatrooms = itchat.get_chatrooms()
# contact = itchat.get_contact()
# mps = itchat.get_mps()
# msg = itchat.get_msg()
# itchat.get_head_img(friend["UserName"], picDir="1.jpg")
itchat.get_QR(enableCmdQR=True)




# import io
#
# import requests, itchat
#
# url = 'https://avatars3.githubusercontent.com/u/13028340'
# r = requests.get(url, stream=True)
# imageStorage = io.BytesIO()
# for block in r.iter_content(1024):
#     imageStorage.write(block)
# imageStorage.seek(0)
#
# itchat.auto_login(True)
# friend = itchat.search_friends(u"爱自由")[0]     # 搜索内容的字符串格式需要是unicode
# r = itchat.send_image(imageStorage, friend["UserName"])
# print(r)
# itchat.run()
