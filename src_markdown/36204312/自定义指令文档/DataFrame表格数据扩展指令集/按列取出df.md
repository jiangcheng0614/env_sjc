# 一.功能描述
<font style="color:rgb(51, 51, 51);">取出DataFrame中指定的列。</font>

![](https://cdn.nlark.com/yuque/0/2023/jpeg/1675452/1692776702014-e4442651-e403-456c-8ddd-383a5476158a.jpeg)



# 二.<font style="color:rgb(51, 51, 51);">配置项说明</font>
### 输入
**<font style="color:rgb(51, 51, 51);">DataFrame</font>****<font style="color:rgb(51, 51, 51);">：</font>**<font style="color:rgb(51, 51, 51);">输入进行取列操作的目标表格，其类型为DataFrame</font>**<font style="color:rgb(51, 51, 51);">  
</font>**<font style="color:rgb(51, 51, 51);">例如传入【读取Excel】返回的DataFrame：</font>

![](https://cdn.nlark.com/yuque/0/2023/jpeg/1675452/1692590684043-8f7cc1bd-2375-4538-8cee-acdbc2a760ba.jpeg)



**<font style="color:rgb(51, 51, 51);">列名：</font>**<font style="color:rgb(51, 51, 51);">输入目标列的列名，组件执行后取出该列；</font>**<font style="color:rgb(51, 51, 51);">  
</font>**<font style="color:rgb(51, 51, 51);">	1.默认为</font><font style="color:rgb(221, 17, 68);background-color:rgb(246, 246, 246);">''</font><font style="color:rgb(51, 51, 51);">，选择所有列：</font>

![](https://cdn.nlark.com/yuque/0/2023/jpeg/1675452/1692776774645-9ae6643e-fad0-439a-97c0-7624c3200f64.jpeg)



<font style="color:rgb(51, 51, 51);"></font>

<font style="color:rgb(51, 51, 51);">  2.输入列名的字符串，取出该指定列：</font>

![](https://cdn.nlark.com/yuque/0/2023/jpeg/1675452/1692776759063-2f3f5d5e-b934-48cd-8c80-038d0d988409.jpeg)

<font style="color:rgb(51, 51, 51);"> </font>

<font style="color:rgb(51, 51, 51);">  3.输入列名为元素组成的有序集合，如list，取出该list内所有元素对应的列；  
</font><font style="color:rgb(51, 51, 51);">例如</font><font style="color:rgb(221, 17, 68);background-color:rgb(246, 246, 246);">['产品代码','产品名称']</font><font style="color:rgb(51, 51, 51);">，取出“产品代码”列和“产品名称”列:</font>

![](https://cdn.nlark.com/yuque/0/2023/jpeg/1675452/1692776833699-a1d6d191-6810-4367-bc33-57511fadfb60.jpeg)





### <font style="color:rgb(51, 51, 51);">输出</font>
**<font style="color:rgb(51, 51, 51);">返回值：</font>**<font style="color:rgb(51, 51, 51);">返回指定列的DataFrame数据集。</font>













