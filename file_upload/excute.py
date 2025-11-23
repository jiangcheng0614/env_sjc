import requests
import json

url = "https://boss-api.shadow-rpa.net/boss/api/v3/helpdoc/menu/add"
headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9',
    'authorization': 'Bearer 2683b56a-c8cd-4435-b17c-c384dca2eac2',
    'content-type': 'application/json',
    'origin': 'https://www.yingdao.com',
    'priority': 'u=1, i',
    'referer': 'https://www.yingdao.com/',
    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
}
def excute_filed(name, id):
    dict = {}
    payload = json.dumps({
        "productCode": "test",
        "type": "folder",
        "name": name,
        "iconUrl": "",
        "scope": "all",
        "previousId": 0,
        "parentId": id
    })
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.json())
    filed_id = response.json()['data']['id']
    dict[name] = filed_id
    return dict

def excute_md(name, id):
    payload = json.dumps({
        "productCode": "test",
        "type": "doc",
        "name": name,
        "seoKey": "",
        "iconUrl": "",
        "pathKey": "",
        "scope": "all",
        "previousId": 0,
        "parentId": id
    })
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.json()['data']['id']


if __name__ == '__main__':
    pass
