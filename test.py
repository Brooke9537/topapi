# -*- coding: utf-8 -*-
import top.api
import json


appkey = "32488920"
secret = "53de51672c79931c7a4532a44310ff94"

url = "gw.api.taobao.com"
port = 80


req=top.api.TbkTpwdCreateRequest(url,port)
req.set_app_info(top.appinfo(appkey,secret))

req.user_id="tb13768892"
req.text="长度大于5个字符"
req.url="https://uland.taobao.com/coupon/edetail?e=5EYqsIUaWC0NfLV8niU3R5TgU2jJNKOfNNtsjZw%2F%2FoK1xDL41poCtNfqjmtRhz5EoKVRM%2FavVYPGxG5SHxtRw8uRTiT9oEhVZV8pr6FWc0Mht39dJDxTAbqZWWHOyn2wmMHpNfYdHdDhXGGZ5OhHfsny8taLQtbvkl%2F8pKt86iJaQQ9BOCyCkQGzEeDoP8E9l44T7Eu%2BIPBVbrKqp4Yn8g%3D%3D&&app_pvid=59590_11.20.254.91_629_1614153593949&ptl=floorId:4094;app_pvid:59590_11.20.254.91_629_1614153593949;tpp_pvid:319eb1fc-8371-4a7e-bdb1-a278150e2c11&union_lens=lensId%3AMAPI%401614153594%400b14fe5b_11f6_177d30d34ab_a04b%4001"
req.logo="https://uland.taobao.com/"
req.ext="{}"
try:
	resp= req.getResponse()
	print(json.dumps(resp, encoding="UTF-8", ensure_ascii=False, sort_keys=True, indent=2))
	#print(resp)
except Exception,e:
	print(e)
