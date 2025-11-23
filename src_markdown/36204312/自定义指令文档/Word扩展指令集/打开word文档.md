# 一.功能描述
打开word文件，并返回该word文件对应的word对象。

![](https://cdn.nlark.com/yuque/0/2023/jpeg/1675452/1677572286846-aa39ba56-d853-4f09-96f3-311a2f212b06.jpeg)



# 二.<font style="color:rgb(51, 51, 51);">配置项说明</font>
### 输入
**<font style="color:rgb(51, 51, 51);">文件路径：</font>**

传入目标word文件的全路径，输入为字符串，只支持docx文件， 也可点击文件夹图标进行选择。

**<font style="color:rgb(51, 51, 51);">访问密码：</font>**

访问密码默认值为空，当文档有访问密码，没有输入密码或密码错误，抛出异常。

**编辑密码：**

编辑密码默认值为空，当文档有编辑密码，没有输入密码或密码错误，抛出异常。

**是否可见：**

默认“是”，通过office的Word文档打开word文件；“否”不可见时，通过office的Word文档在后台打开文件。

### <font style="color:rgb(51, 51, 51);">输出</font>
返回word对象**<font style="color:rgb(51, 51, 51);">：</font>**

返回生成的此word文档的对象。

例：如下图 返回word对象。

![](https://cdn.nlark.com/yuque/0/2023/jpeg/1675452/1677652475180-6d0a00c7-2e32-4c09-ab35-dc615785a0c0.jpeg)







