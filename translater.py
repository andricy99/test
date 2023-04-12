# Author:xueling
import requests
import json
# 1.基于控制台输入-待翻译的词语
while True:
    content = input('待翻译词语:')
    if content in 'exit()':
        print('bye!')
        break

    # 2.设定待请求的url
    url = 'https://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'

    # 3.建立post表单
    post_form = {
        'i': content,
        'from': 'AUTO',
        'to': 'AUTO',
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'salt': '16289098623791',
        'sign': '03e2161bb596c659c680bd79b473fb1e',
        'lts': '1628909862379',
        'bv': '4f7ca50d9eda878f3f40fb696cce4d6d',
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_REALTlME'
    }
    # 4.提交post请求
    response = requests.post(url,data=post_form,timeout=5)

    # 5.接收响应结果，解析提取
    trans_json = response.text
    trans_dict = json.loads(trans_json)
    result = trans_dict['translateResult'][0][0]['tgt']
    # 6.打印翻译结果
    print(result)
