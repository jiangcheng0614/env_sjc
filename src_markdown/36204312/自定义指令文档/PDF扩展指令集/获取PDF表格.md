# 一.功能描述
<font style="color:rgb(51, 51, 51);">获取目标PDF文件指定页中的表格，并返回指定页面表格元素的列表。</font>

![](https://cdn.nlark.com/yuque/0/2023/jpeg/1675452/1676877075663-9964757f-6a33-4848-81f3-72848f3a97e2.jpeg)



# 二.<font style="color:rgb(51, 51, 51);">配置项说明</font>
### 输入
**<font style="color:rgb(51, 51, 51);">PDF文件路径：</font>**

传入目标PDF文件的全路径，输入为字符串，也可点击输入框右侧的选择文件进行选择。

**<font style="color:rgb(51, 51, 51);">提取模式：</font>**

下拉选项：0：提取 所有页数  

                 1：提取 指定页

**PDF密码：**

输入PDF密码，若PDF未设置密码则无需输入<font style="color:rgb(51, 51, 51);">。</font>

**指定页范围：**

选填，如提取模式选择1 指定页模式，<font style="color:rgb(51, 51, 51);">此时“指定页”参数必须填入指定的页码，输入为字符串，内容为页码数，多个页码之间用英文的逗号</font><font style="color:rgb(221, 17, 68);background-color:rgb(246, 246, 246);">,</font><font style="color:rgb(51, 51, 51);">隔开，例如</font><font style="color:rgb(221, 17, 68);background-color:rgb(246, 246, 246);">'1,3'</font><font style="color:rgb(51, 51, 51);">，连续的页码也可以短横线</font><font style="color:rgb(221, 17, 68);background-color:rgb(246, 246, 246);">'-'</font><font style="color:rgb(51, 51, 51);">，例如</font><font style="color:rgb(221, 17, 68);background-color:rgb(246, 246, 246);">'1,3,5-7'</font><font style="color:rgb(51, 51, 51);">表示的是第1、3以及5、6、7页。</font>

示例： '1'  '1,2,3'    '1,3,5-7'

### <font style="color:rgb(51, 51, 51);">输出</font>
返回PDF表格list**<font style="color:rgb(51, 51, 51);">：</font>**

返回指定页面元素的列表

例如：列表 [df1, df2, df3···]

![](https://cdn.nlark.com/yuque/0/2023/png/1675452/1676880197125-96960e44-704b-4402-8ed4-1b2c5779824a.png)



