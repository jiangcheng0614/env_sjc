# 一.功能描述
<font style="color:rgb(51, 51, 51);">读取指定表格文件中的数据，并将读取到的内容进行返回。</font>

![](https://cdn.nlark.com/yuque/0/2023/jpeg/1675452/1693214003987-7a86d6cf-ff0d-49a8-8de5-a0cd589bf65d.jpeg)





# 二.**<font style="color:rgb(51, 51, 51);">基本使用说明</font>**
<font style="color:rgb(51, 51, 51);">1.点击”文件路径”后的文件夹图标，选择需要读取的Excel文件：</font>

![](https://cdn.nlark.com/yuque/0/2023/png/1675452/1693217223418-3ea22481-e9cc-444b-98dc-ab9fa6c41001.png)



<font style="color:rgb(51, 51, 51);">2.设置指定“工作表”，此处默认</font><font style="color:rgb(221, 17, 68);background-color:rgb(246, 246, 246);">0</font><font style="color:rgb(51, 51, 51);">，读取第一个Sheet页，其他属性也均为默认值；</font>

![](https://cdn.nlark.com/yuque/0/2023/jpeg/1675452/1693217241444-bb6e49c0-b5df-4e7c-a60c-87bbd0668562.jpeg)

<font style="color:rgb(51, 51, 51);"></font>

<font style="color:rgb(51, 51, 51);">3.运行流程，在运行日志窗口打印的内容为第一个工作表的数据：</font>

![](https://cdn.nlark.com/yuque/0/2023/jpeg/1675452/1693217253673-6edf1d91-360d-4562-98a0-e8e04b8f7da3.jpeg)



# 三.<font style="color:rgb(51, 51, 51);">配置项说明</font>
### 输入
**<font style="color:rgb(51, 51, 51);">文件路径</font>****<font style="color:rgb(51, 51, 51);">：</font>**<font style="color:rgb(51, 51, 51);">传入需要读取的目标Excel文件的路径，输入为字符串；可点击右侧的选择文件图标进行选择。</font>**<font style="color:rgb(51, 51, 51);"></font>**



**<font style="color:rgb(51, 51, 51);">sheet_name：</font>**<font style="color:rgb(51, 51, 51);">即表格文件的Sheet页，选定读取的目标工作表。</font>**<font style="color:rgb(51, 51, 51);">  
</font>**<font style="color:rgb(51, 51, 51);">	1.默认为</font><font style="color:rgb(221, 17, 68);background-color:rgb(246, 246, 246);">0</font><font style="color:rgb(51, 51, 51);">，表示表格文件的第一个Sheet页；工作表的下标从0开始，填入相应的数字代表了对应的Sheet页，例如入</font><font style="color:rgb(221, 17, 68);background-color:rgb(246, 246, 246);">2</font><font style="color:rgb(51, 51, 51);">，则表示第三个工作表；</font>

<font style="color:rgb(51, 51, 51);">  2.也可传入工作表名称的字符串，如</font><font style="color:rgb(221, 17, 68);background-color:rgb(246, 246, 246);">'产品详情'</font><font style="color:rgb(51, 51, 51);">，需要注意区分大小写以及空格，必须保证完全一致；</font>

<font style="color:rgb(51, 51, 51);">  3.如果需要读取所有的工作表，则可以输入</font><font style="color:rgb(221, 17, 68);background-color:rgb(246, 246, 246);">None</font><font style="color:rgb(51, 51, 51);">；此时返回的便是值为Dataframe的有序字典。</font>

<font style="color:rgb(51, 51, 51);">  4.输入工作表下标或名称组成的列表，读取列表内元素对应的工作表；例如输入</font><font style="color:rgb(221, 17, 68);background-color:rgb(246, 246, 246);">[0,2]</font><font style="color:rgb(51, 51, 51);">，便是读取表格第一、第三个工作表。</font>



**<font style="color:rgb(51, 51, 51);">header：</font>**<font style="color:rgb(51, 51, 51);">指定作为表头的行，输入为int整型或None。</font>

<font style="color:rgb(51, 51, 51);"> 1.默认为</font><font style="color:rgb(221, 17, 68);background-color:rgb(246, 246, 246);">0</font><font style="color:rgb(51, 51, 51);">，表示以读取的第一行作为表头，表头行以下行为数据。例如，若此处输入</font><font style="color:rgb(221, 17, 68);background-color:rgb(246, 246, 246);">1</font><font style="color:rgb(51, 51, 51);">，则表头为所读取表格的第二行，表头行以下为读取的数据：</font>

![](https://cdn.nlark.com/yuque/0/2023/jpeg/1675452/1693217290870-2236a1e1-3986-400c-81f8-fd3be68431af.jpeg)



<font style="color:rgb(51, 51, 51);"> 2.若表格数据不含表头，则可设置为None，默认列的下标作为表头：</font>

![](https://cdn.nlark.com/yuque/0/2023/png/1675452/1693217305904-3224b8f9-5172-472d-ab71-0a1cf6a9dafe.png)



**<font style="color:rgb(51, 51, 51);">skiprows：</font>**<font style="color:rgb(51, 51, 51);">从所读取表格的第一行开始，设置省略跳过的行数。默认为None，也就是不跳过行，输入int整型，跳过该整数行；例如输入2，跳过两行，即从表格第三行开始读取：</font>

![](https://cdn.nlark.com/yuque/0/2023/jpeg/1675452/1693217326796-5ce806be-4554-47d3-a156-cc7f487f1433.jpeg)



**<font style="color:rgb(51, 51, 51);">skip_footer：</font>**<font style="color:rgb(51, 51, 51);">从末行开始，跳过省略表格的行数。默认为0，不省略末尾的行，输入int整型，从末尾开始跳过该整数行；例如输入</font><font style="color:rgb(221, 17, 68);background-color:rgb(246, 246, 246);">2</font><font style="color:rgb(51, 51, 51);">，则可以省略最后两行：</font>

![](https://cdn.nlark.com/yuque/0/2023/jpeg/1675452/1693217345741-6251767d-5343-4935-9af7-0a0958db18f1.jpeg)



**<font style="color:rgb(51, 51, 51);">index_col：</font>**<font style="color:rgb(51, 51, 51);">指定列为索引列，默认为None，即不进行设置；也可输入工作表中列的下标，或列名的字符串，其对应类型为int整型和字符串。</font>

<font style="color:rgb(51, 51, 51);"> 1.输入工作表中列的下标，例如输入</font><font style="color:rgb(221, 17, 68);background-color:rgb(246, 246, 246);">1</font><font style="color:rgb(51, 51, 51);">：</font>

![](https://cdn.nlark.com/yuque/0/2023/jpeg/1675452/1693217399422-9a0f3042-f708-42e0-b756-107927e48716.jpeg)



<font style="color:rgb(51, 51, 51);"> 2.输入工作表列名称的字符串，例如输入</font><font style="color:rgb(221, 17, 68);background-color:rgb(246, 246, 246);">'产品类型'</font><font style="color:rgb(51, 51, 51);">：</font>

<font style="color:rgb(51, 51, 51);"> 3.输入列名组成的有序集合，例如</font><font style="color:rgb(221, 17, 68);background-color:rgb(246, 246, 246);">[0,2]</font><font style="color:rgb(51, 51, 51);">，将第一、三列作为索引列：</font>

<font style="color:rgb(51, 51, 51);"></font>

**<font style="color:rgb(51, 51, 51);">names：</font>**<font style="color:rgb(51, 51, 51);">参数设置表格中每列的列名。</font>

<font style="color:rgb(51, 51, 51);"> 1.默认为None，即不设置，此时默认“header”参数设置的表头为列名，如果“header”参数也默认为为None，则以列的下标为列名：</font>

<font style="color:rgb(51, 51, 51);"> 2.传入一个有序集合，如列表或元组等，此处输入列表</font><font style="color:rgb(221, 17, 68);background-color:rgb(246, 246, 246);">[1,2,'三','四','5',6]</font><font style="color:rgb(51, 51, 51);">为例：</font>

<font style="color:rgb(51, 51, 51);"> 3.注意有序集合的长度要与读取到的表格的数据列数必须是一致，否则报错，提示长度不匹配。  
</font><font style="color:rgb(51, 51, 51);">例如输入列表</font><font style="color:rgb(221, 17, 68);background-color:rgb(246, 246, 246);">[1,2,'三','四','5']</font><font style="color:rgb(51, 51, 51);">：</font>

<font style="color:rgb(51, 51, 51);"></font>

**<font style="color:rgb(51, 51, 51);">usecols：</font>**<font style="color:rgb(51, 51, 51);">设置获取表格的列数，默认为None，获取所有列数。</font>

<font style="color:rgb(51, 51, 51);"> 1.输入列的下标组成的有序集合如列表list或元组tuple，此时只读取列的下标对应的列。例如输入元组</font><font style="color:rgb(221, 17, 68);background-color:rgb(246, 246, 246);">(0,1,3)</font><font style="color:rgb(51, 51, 51);">,则获取第一列，第二列，以及第四列：</font>

![](https://cdn.nlark.com/yuque/0/2023/png/1675452/1693217417432-cd465334-290c-4b88-a190-76ff0be95e45.png)



<font style="color:rgb(51, 51, 51);"> 2.还可以输入列字母组成的字符串，以逗号</font><font style="color:rgb(221, 17, 68);background-color:rgb(246, 246, 246);">,</font><font style="color:rgb(51, 51, 51);">分隔，冒号</font><font style="color:rgb(221, 17, 68);background-color:rgb(246, 246, 246);">:</font><font style="color:rgb(51, 51, 51);">表示取范围。例如，输入字符串</font><font style="color:rgb(221, 17, 68);background-color:rgb(246, 246, 246);">'A,C:E'</font><font style="color:rgb(51, 51, 51);">获取的是A列，以及C到E列：</font>



**<font style="color:rgb(51, 51, 51);">converters：</font>**<font style="color:rgb(51, 51, 51);">用以设置表格中指定列的数据类型，输入为字典：例如“converters”参数输入</font><font style="color:rgb(221, 17, 68);background-color:rgb(246, 246, 246);">{u'视频保存时长':float}</font><font style="color:rgb(51, 51, 51);">，定义”视频保存时长”列的数据类型为浮点数类型：</font>

![](https://cdn.nlark.com/yuque/0/2023/jpeg/1675452/1693217433010-42825936-db6b-4dcf-813c-6fa7fd8367f7.jpeg)



**<font style="color:rgb(51, 51, 51);">还有很多不太常用的参数，可以查找资料参考pandas库的read_excel方法去进行相关设置。</font>**



### <font style="color:rgb(51, 51, 51);">输出</font>
**<font style="color:rgb(51, 51, 51);">返回值：</font>**<font style="color:rgb(51, 51, 51);">读取Excel后得到的表格数据，读取单个工作表时的返回类型为DataFrame，读取多个工作表，返回的是一个值为Dataframe的字典。</font>













