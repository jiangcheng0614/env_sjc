# 描述
调用[翔云车架号VIN查询接口](http://www.netocr.com/VIN_car.html)，返回车架号包含的厂商、车系、车型、发动机类型、排量等信息

![](https://cdn.nlark.com/yuque/0/2023/png/33628300/1676964199427-824031c8-4f57-41d4-8e5c-96f9ddc30f03.png)



# **输入**
### **key：**
[翔云](http://www.netocr.com/user/index.html?sul=users_order)账号的OCR key

### secret：
翔云账号的OCR secret



![](https://cdn.nlark.com/yuque/0/2023/png/33628300/1676893020440-89f3590a-b091-4069-9714-bb289fec9625.png)

### 数据类型：
下拉框可选项

+ <font style="color:rgb(50, 50, 50);">标准数据</font>
+ 全部数据

### VIN号：
字符串

若批量识别，请传入一维列表 ["VIN1", "VIN2", ···  ]

# 输出
### invoke_result：
**单个**查询的结果，返回**一维列表**，列表中的第一项是识别状态 ，内容都是**字典形式**

**批量**查询，一次性返回**二维列表**。

[错误码](http://www.netocr.com/apiCenter/index.html)参考



# 使用示例
![](https://cdn.nlark.com/yuque/0/2023/png/33628300/1676965827801-d9008b1b-35ca-4d40-8b53-273e4269808c.png)

![](https://cdn.nlark.com/yuque/0/2023/png/33628300/1676965864946-d8f2fd40-e7d7-45f3-b448-4e1e3ebfdb93.png)



**执行结果：**

![](https://cdn.nlark.com/yuque/0/2023/png/33628300/1676965815070-039cbd08-93d2-43e2-99d4-2e94ce955420.png)

