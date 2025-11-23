import uuid
import requests
import json
import re
import urllib
import urllib3
import os

# 禁用SSL警告（仅在开发环境中使用）
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class YDAdd:
    def __init__(self, token, id):
        self.token = token
        self.id = id
        self.headers = {
            'Connection': 'keep-alive',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'sec-ch-ua-platform': 'Windows',
            'Authorization': f'Bearer {self.token}',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36',
            'Accept': 'application/json, text/plain, */*',
            'sec-ch-ua': '"Chromium";v="142", "Google Chrome";v="142", "Not_A Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'Origin': 'https://www.yingdao.com',
            'Sec-Fetch-Site': 'cross-site',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://www.yingdao.com/',
            'Accept-Encoding': 'gzip, deflate, br, zstd',
            'Accept-Language': 'zh-CN,zh;q=0.9',
        }
    def get_menu_tree(self):
        ''' 获取结构树，用于获取父级id
        '''
        headers = self.headers
        response = requests.get('https://boss-api.shadow-rpa.net/boss/api/v3/cornerstone/helpdoc/menu/getAdminMenuTreeByBrandCode?brandCode=flow&languageCode=zh-CN', headers=headers, verify=False)
        with open('menu_tree.json', 'w', encoding='utf-8') as f:
            json.dump(response.json(), f, ensure_ascii=False, indent=4)
        print("菜单树已保存到 menu_tree.json")
        return response.json()

    def add_folder(self, name, id):
        ''' 添加文件夹
        '''
        headers = self.headers
        payload = {
            "brandCode": "flow",
            "languageCode": "zh-CN",
            "type": "folder",
            "name": name,
            "iconUrl": "",
            "scope": "all",
            "parentId": id,
        }
        response = requests.post('https://boss-api.shadow-rpa.net/boss/api/v3/cornerstone/helpdoc/menu/add', headers=headers, json=payload, verify=False)
        print(response.json())
        return response.json()

    def add_doc(self, name, id):
        ''' 添加文档
        '''
        headers = self.headers
        payload = {
            "languageCode": "zh-CN",
            "brandCode": "flow",
            "type": "doc",
            "name": name,
            "seoKey": "",
            "iconUrl": "",
            "scope": "all",
            "parentId": id,
            "previousId": 0,
        }
        response = requests.post('https://boss-api.shadow-rpa.net/boss/api/v3/cornerstone/helpdoc/menu/add', headers=headers, json=payload, verify=False)
        return response.json()

    def save_content(self, id, content):
        ''' 保存内容
        '''
        headers = self.headers
        payload = {
            "content": f"/yddoc/flow_zh-CN/doc/{id}",
            "contentType": "oss",
            "menuId": id,
            "plainTextContent": content,
        }
        response = requests.post('https://boss-api.shadow-rpa.net/boss/api/v3/cornerstone/helpdoc/menu/save', headers=headers, json=payload, verify=False)
        print(response.status_code)
        print(response.text)

    def put_content(self, id, sign, data):
        ''' 上传内容
        '''
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
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Chromium";v="142", "Google Chrome";v="142", "Not_A Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }
        params = {
            'sign': sign,
        }
        data = json.dumps(data)
        response = requests.put(
            f'https://xybot-oss-1302949341.cos.ap-shanghai.myqcloud.com/yddoc/flow_zh-CN/doc/{id}_draft',
            params=params,
            headers=headers,
            data=data,
            verify=False,
        )
        print(response.status_code)
        print(response.text)

    def summit_content(self, id, sign, data):
        ''' 上传内容
        '''
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
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36',
            'sec-ch-ua': '"Chromium";v="142", "Google Chrome";v="142", "Not_A Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }
        params = {
            'sign': sign,
        }
        data = json.dumps(data)
        response = requests.put(
            f'https://xybot-oss-1302949341.cos.ap-shanghai.myqcloud.com/yddoc/flow_zh-CN/doc/{id}',
            params=params,
            headers=headers,
            data=data,
            verify=False,
        )
        print(response.status_code)
        
    def clean_font_tags(self, text):
        ''' 清理所有 font 标签，移除标签但保留内容
        '''
        import re
        if not text:
            return text
        
        # 移除所有包含内容的 font 标签，保留标签内的内容
        # 匹配 <font 任意属性>内容</font> 并替换为 内容
        text = re.sub(r'<font[^>]*>(.*?)</font>', r'\1', text, flags=re.IGNORECASE | re.DOTALL)
        
        # 移除所有空的 font 标签（包括各种变体）
        text = re.sub(r'<font[^>]*>\s*</font>', '', text, flags=re.IGNORECASE)
        
        return text

    def get_md_content(self, id, path):
        ''' 获取md内容
        '''
        total_data = {
            "type": "doc",
            "content":[]
        }
        path = path
        line_list = []
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                if '<a' not in line:
                    # 清理 font 标签
                    line = self.clean_font_tags(line)
                    if '<br />' in line:
                        temp_list = line.split('<br />')
                        line_list.extend(temp_list)
                    else:
                        line_list.append(line)

        for line in line_list:
            if line != '\n':
                line = line.replace('\n','')
                # 再次清理，确保没有遗漏
                line = self.clean_font_tags(line)
                data = self.get_data(id,line)
                if data != None:
                    total_data['content'].append(data)
        return total_data

    def get_data(self, id, line):
        ''' 获取数据
        '''
        data = {}
        # 如果是line是图片行，进行如下操作
        if "![image.png]" in line or '![]' in line or 'g]' in line :
            pattern = r'\!\[.*?\]\((.*?)\)'
            matches = re.findall(pattern, line)
            
            # 图片保存目录为当前运行目录下的 "images" 文件夹
            img_dir = os.path.join(os.getcwd(), "images")
            if not os.path.exists(img_dir):
                os.makedirs(img_dir)
            filepath = os.path.join(img_dir, "测试.png")

            response = requests.get(matches[0], verify=False)
            with open(filepath, 'wb') as f:
                f.write(response.content)
            urls = self.img_req(id)
            # 上传图片
            self.summit_img(urls['uploadUrl'], filepath)
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
            content = line.split('# ')[1].replace('*','')
            print(content)
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
    
    def img_req(self, id):
        headers = self.headers
        json_data = {
            'fileName': '5.1.png',
            'fileSize': 150624,
            'fileType': 'doc_asset',
            'menuId': id,
            "envCode": "flow_zh-CN"
        }
        response = requests.post('https://boss-api.shadow-rpa.net/boss/api/v3/cornerstone/helpdoc/oss/getUploadUrl', headers=headers,
                                json=json_data, verify=False)
        return response.json()['data']
    
    def text_req(self, id):
        ''' 获取文本
        '''
        headers = self.headers
        json_data = {
            'fileName': f'{id}_draft',
            'fileType': 'doc',
            'envCode': 'flow_zh-CN',
            'menuId': id,
        }
        response = requests.post('https://boss-api.shadow-rpa.net/boss/api/v3/cornerstone/helpdoc/oss/getUploadUrl', headers=headers, json=json_data, verify=False)
        return response.json()['data']
    
    def end_req(self, id):
        ''' 获取结束请求
        '''
        headers = self.headers
        json_data = {
            'fileName': f'{id}',
            'fileType': 'doc',
            'envCode': 'flow_zh-CN',
            'menuId': id,
        }
        response = requests.post('https://boss-api.shadow-rpa.net/boss/api/v3/cornerstone/helpdoc/oss/getUploadUrl', headers=headers, json=json_data, verify=False)
        return response.json()['data']

    def summit_img(self, uploadurl, filepath):
        ''' 上传图片
        '''
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
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36',
            'Content-Type': 'image/png',
            'sec-ch-ua': '"Chromium";v="142", "Google Chrome";v="142", "Not_A Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
        }
        response = requests.put(uploadurl, headers=headers, data=image_data, verify=False)
        if response.status_code == 200:
            print("图片上传成功")

    def add(self, id):
        ''' 添加文档
        '''
        headers = self.headers
        payload = {
            "content": f"/yddoc/flow_zh-CN/doc/{id}_draft",
            "contentType": "oss",
            "menuId": id,
        }
        response = requests.post('https://boss-api.shadow-rpa.net/boss/api/v3/cornerstone/helpdoc/draft/add', headers=headers, json=payload, verify=False)
        return response.json()

    def report_api(self, id):
        ''' 上报api
        '''
        headers = self.headers
        payload = {
            "buryId": str(uuid.uuid4()),
            "buttonText": "发 布",
            "enterpriseName": "",
            "href": f"https://www.yingdao.com/yddoc/flow/zh-CN/{id}?from=boss",
            "level": "info",
            "pathname": f"/yddoc/flow/zh-CN/{id}",
            "referrer": "web",
            "search": "?from=boss",
            "span": "user-event",
            "user": "",
            "userName": "",
            "uuid": "",
        }
        response = requests.post('https://console.yingdao.com/report-api', headers=headers, json=payload, verify=False)

    def run(self, path):
        ''' 运行
        '''
        # 获取md内容
        total_data = self.get_md_content(self.id, path)
        urls = self.text_req(self.id)
        ori_sign = urls['uploadUrl'].split('sign=')[1]
        sign = urllib.parse.unquote(ori_sign)
        # 开始添加草稿
        self.add(self.id)
        self.put_content(self.id, sign, total_data)
        # 上报api
        self.report_api(self.id)
        urls_1 = self.end_req(self.id)
        ori_sign_1 = urls_1['uploadUrl'].split('sign=')[1]
        sign_1 = urllib.parse.unquote(ori_sign_1)
        # 提交内容
        self.summit_content(self.id, sign_1, total_data)
    
if __name__ == "__main__":
    yd_add = YDAdd("ae53f180-7a8a-41d5-ac38-e410b02a4508", "887626928975187968")
    path = r"D:\env_text\doc_md\src_markdown\36204312\自定义指令文档\飞书多维表格\添加字段.md"
    yd_add.run(path)
    # folder_path = r"D:\env_text\doc_md\src_markdown\36204312\自定义指令文档"

    # # 获取folder_path文件夹下所有文件不包括文件夹名称
    # file_names = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    # print(file_names)
    # # 根据文件名称找到folder_path文件夹下对应的文件夹并生成映射表