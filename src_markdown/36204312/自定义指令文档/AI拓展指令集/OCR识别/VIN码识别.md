# 描述
调用[翔云VIN码识别接口](http://www.netocr.com/VIN.html)，对图片进行OCR识别。

![](https://cdn.nlark.com/yuque/0/2023/png/33628300/1676959408947-34a2c51a-241b-4d97-bba6-0f9105c5f932.png)



# **输入**
### **key：**
[翔云](http://www.netocr.com/user/index.html?sul=users_order)账号的OCR key

### secret：
翔云账号的OCR secret



![](https://cdn.nlark.com/yuque/0/2023/png/33628300/1676893020440-89f3590a-b091-4069-9714-bb289fec9625.png)

### 图片：
证件图片的路径，字符串

若批量识别，请传入一维列表 ["path1", "path2", ···  ]

# 输出
### invoke_result：
**单个**图片识别的结果，返回**一维列表**，列表中的第一项是识别状态 ，内容都是**字典形式**

**批量**图片识别，一次性返回**二维列表**。

[错误码](http://www.netocr.com/apiCenter/index.html)参考



# 使用示例
![](https://cdn.nlark.com/yuque/0/2023/png/33628300/1676959480453-59e85643-ec03-4a34-b665-5c488a68a945.png)

![](https://cdn.nlark.com/yuque/0/2023/png/33628300/1676959575404-26a3a138-ae81-4b88-be38-992bfe1d3e67.png)



**执行结果：**

![](https://cdn.nlark.com/yuque/0/2023/png/33628300/1676959527240-9553f081-ea43-4421-8395-b8555498d0b9.png)

