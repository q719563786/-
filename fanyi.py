import pyperclip,requests,json
shuru = pyperclip.paste()
url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
data = {'i': shuru,'from': 'AUTO','to': 'AUTO','smartresult': 'dict','client': 'fanyideskweb','salt': '15445136920078','sign': '5243255304e7f840eb331ffb854e2be1','ts': '1544513692007','bv': 'b33a2f3f9d09bde064c9275bcb33d94e','doctype': 'json','version': '2.1','keyfrom': 'fanyi.web','action': 'FY_BY_REALTIME','typoResult': 'false'}
r = requests.get(url,data)
a = json.loads(r.text)
print(a['translateResult'][0][0]['tgt'])
pyperclip.copy(a['translateResult'][0][0]['tgt'])
input('翻译结果已复制至剪切板，点击enter退出')
