# -*- coding: utf-8 -*-
import top.api
import json

appkey = "32488920"
secret = "53de51672c79931c7a4532a44310ff94"
url = "gw.api.taobao.com"
port = 80

# 推荐商品物料 物料列表：https://market.m.taobao.com/app/qn/toutiao-new/index-pc.html#/detail/10628875?_k=gpov9a
def get_resp_list():
	req=top.api.TbkDgOptimusMaterialRequest(url,port)
	req.set_app_info(top.appinfo(appkey,secret))

	req.page_size=3
	req.adzone_id=111202950268
	req.page_no=3
	req.material_id=4094
	try:
		resp = req.getResponse()
		#print(json.dumps(resp, encoding="UTF-8", ensure_ascii=False, sort_keys=True, indent=2))
		print(resp['tbk_dg_optimus_material_response'])
		return resp
	except Exception,e:
		print(e)
		return 1

one = json.dumps(get_resp_list()['tbk_dg_optimus_material_response']['result_list']['map_data'][0], encoding="UTF-8", ensure_ascii=False, sort_keys=True, indent=2)

print(one)