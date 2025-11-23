import requests
import json
import urllib
import re

def text_req(id):
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
    json_data = {
        'fileName': f'{id}_draft',
        'fileType': 'doc',
        'productCode': 'test',
    }
    response = requests.post('https://boss-api.shadow-rpa.net/boss/api/v3/helpdoc/oss/getUploadUrl', headers=headers,
                             json=json_data)
    return response.json()['data']

def img_req(id):
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
    json_data = {
        'fileName': '测试.png',
        'fileSize': 150624,
        'fileType': 'doc_asset',
        'productCode': 'test',
        'menuId': id,
    }
    response = requests.post('https://boss-api.shadow-rpa.net/boss/api/v3/cornerstone/helpdoc/oss/getUploadUrl', headers=headers,
                             json=json_data)
    return response.json()['data']

def summit_img(uploadurl):
    filepath = r"C:\Users\11758\Desktop\download_image\测试.png"
    with open(filepath, 'rb') as f:
        image_data = f.read()
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Connection': 'keep-alive',
        'Origin': 'https://www.yingdao.com',
        'Referer': 'https://www.yingdao.com/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
        'Content-Type': 'image/png',  # 这里指定图片格式
        'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"'
        }
    response = requests.put(uploadurl, headers=headers, data=image_data)
    if response.status_code == 200:
        print("图片上传成功")

def get_data(id, line):
    data = {}
    # 如果是line是图片行，进行如下操作
    if "![image.png]" in line or '![]' in line or 'g]' in line :
        pattern = r'\!\[.*?\]\((.*?)\)'
        matches = re.findall(pattern, line)
        filepath = r"C:\Users\11758\Desktop\download_image\测试.png"
        response = requests.get(matches[0])
        with open(filepath, 'wb') as f:
            f.write(response.content)
        urls = img_req(id)
        #上传图片
        summit_img(urls['uploadUrl'])
        read_url = urls['readUrl']
        key = urls['key']
        data = {
            "type":"image",
            "attrs": {
                "src": read_url,
                "alt": None,
                "title": None,
                "width": None,
                "height": None
            },
            "src": key
        }
        return data

    elif '**' in line and  2< line.count('*') < 5:
        bold_text = re.findall(r'\*\*(.*?)\*\*', line)[0]
        rest_text = line.split("**")[-1].replace('\n','')
        if rest_text == '':
            data = {
                "type": "paragraph",
                "content": [
                    {
                        "type": "text",
                        "marks": [
                            {
                                "type": "bold"
                            }
                        ],
                        "text": bold_text
                    }
                ]
            }
            return data
        data = {
                "type": "paragraph",
                "content": [
                    {
                        "type": "text",
                        "marks": [
                            {
                                "type": "bold"
                            }
                        ],
                        "text": bold_text
                    },
                    {
                        "type": "text",
                        "text": rest_text
                    }
                ]
            }
        return data
    if line.count('*') > 5:
        line = line.replace('*','')
        data = {
            "type": "paragraph",
            "content": [
                {
                    "type": "text",
                    "text": line
                }
            ]
        }
        return data

    elif "#" in line:
        print(line)
        content = line.split(' ')[1].replace('*','')
        size = line.count("#")
        if content != '':
            data = {
            "type": "heading",
            "attrs": {
                "level": size,
                "id": f"h{size}_10d2d4c3-21e6-4d93-b63d-26f3bd1c196e"
            },
            "content": [
                {
                    "type": "text",
                    "text": content
                }
            ]
        }
            return data
        else:
            return None

    else:
        line = line.replace('*','')
        data = {
            "type": "paragraph",
            "content": [
                {
                    "type": "text",
                    "text": line
                }
            ]
        }
        return data

def get_total_data(path, id):
    total_data = {
        "type": "doc",
        "content":[]
    }
    path = path
    line_list = []
    with open(path, 'r', encoding='utf-8') as file:
        for line in file:
            if '<a' not in line:
                if '<br />' in line:
                    temp_list = line.split('<br />')
                    line_list.extend(temp_list)
                else:
                    line_list.append(line)

    for line in line_list:
        if line != '\n':
            line = line.replace('\n','')
            data = get_data(id,line)
            if data != None:
                total_data['content'].append(data)
    return total_data

def add(id):
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

    json_data = {
        'menuId': id,
        'contentType': 'oss',
        'content': f'/yddoc/test/doc/{id}_draft',
    }

    response = requests.post('https://boss-api.shadow-rpa.net/boss/api/v3/helpdoc/draft/add', headers=headers,
                             json=json_data)

def summit(id ,sign, data):
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Content-Type': 'text/plain;charset=UTF-8',
        'Origin': 'https://www.yingdao.com',
        'Referer': 'https://www.yingdao.com/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
        'contentType': '',
        'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }
    params = {
        'sign': sign,
    }
    data = json.dumps(data)
    response = requests.put(
        f'https://xybot-oss-1302949341.cos.ap-shanghai.myqcloud.com/yddoc/test/doc/{id}_draft',
        params=params,
        headers=headers,
        data=data,
    )


def run(path, id):
    data = get_total_data(path, id)
    add(id)
    print(data)
    urls = text_req(id)
    ori_sign = urls['uploadUrl'].split('sign=')[1]
    sign = urllib.parse.unquote(ori_sign)
    print(sign)
    print(id)
    summit(id, sign, data)


if __name__ == '__main__':
    path = r"C:\Users\11758\PycharmProjects\pythonProject\test\download\36204312\自定义指令文档\个人微信\微信发送消息&表情包.md"
    id = '719466845367566336'
    run(path, id)
    # total_data = get_total_data(path, id)
    # print(total_data)
