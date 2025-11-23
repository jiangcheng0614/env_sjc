# 一.功能描述
<font style="color:rgb(51, 51, 51);">将两个DataFrame数据集依照指定列，进行合并操作，得到一个新的DataFrame。</font>

![](https://cdn.nlark.com/yuque/0/2023/png/1675452/1693400133306-2bbda521-b56a-4a80-924e-2c1ffef37e6b.png)





# 二.**<font style="color:rgb(51, 51, 51);">基本使用说明</font>**
<font style="color:rgb(51, 51, 51);">1.“left”：参与合并的左侧DataFrame数据集，  
</font><font style="color:rgb(51, 51, 51);">	“right”：参与合并的右侧DataFrame数据集。  
</font><font style="color:rgb(51, 51, 51);">	例如传入【读取excel】返回的DataFrame：</font>

<font style="color:rgb(51, 51, 51);">2.在“on”参数内指定用于连接合并两个DataFrame的列：</font>

<font style="color:rgb(51, 51, 51);">"产品类型"  作为merge的列，</font>

<font style="color:rgb(51, 51, 51);">3.得到以“key”为指定列合并的DataFrame：</font>

<font style="color:rgb(51, 51, 51);">df1:</font>

![](https://cdn.nlark.com/yuque/0/2023/png/1675452/1693398688764-6b365f1c-63e9-440c-9ba7-738e58c4bb75.png)

<font style="color:rgb(51, 51, 51);">df2:</font>

![](https://cdn.nlark.com/yuque/0/2023/png/1675452/1693398702405-7321d0ca-da16-42a9-b0ec-219ba24fb591.png)

left：左连接  

得到以下拼接出的merge数据

![](https://cdn.nlark.com/yuque/0/2023/png/1675452/1693398666612-f2b24a6d-5159-4df5-b30f-bcb6aa036243.png)





# 三.<font style="color:rgb(51, 51, 51);">配置项说明</font>
### 输入
**<font style="color:rgb(51, 51, 51);">left：</font>**<font style="color:rgb(51, 51, 51);">参与合并的左侧DataFrame数据集</font>

<font style="color:rgb(51, 51, 51);"></font>

**<font style="color:rgb(51, 51, 51);">right</font>****<font style="color:rgb(51, 51, 51);">：</font>**<font style="color:rgb(51, 51, 51);">参与合并的右侧DataFrame数据集</font>

<font style="color:rgb(51, 51, 51);"></font>

**<font style="color:rgb(51, 51, 51);">on：</font>**<font style="color:rgb(51, 51, 51);">指定用于连接合并两个DataFrame的列，必须在左右DataFrame数据集中都存在(找到)的列。</font>**<font style="color:rgb(51, 51, 51);">  
</font>**<font style="color:rgb(51, 51, 51);">	1.未指定情况即默认为None，则以两个DataFrame中都存在的列名作为连接列。例如以"产品类型"  这列合并两个DataFrame：</font>

<font style="color:rgb(51, 51, 51);">  2.输入列名，以该列合并两个DataFrame：</font>

<font style="color:rgb(51, 51, 51);">  3.输入列名为元素的有序集合，通过这些列合并两个DataFrame，例如输入列表</font><font style="color:rgb(221, 17, 68);background-color:rgb(246, 246, 246);">['产品类型','产品名称']</font><font style="color:rgb(51, 51, 51);">：</font>



**<font style="color:rgb(51, 51, 51);">how：</font>**<font style="color:rgb(51, 51, 51);">用以设置合并两个DataFrame的方式，有</font><font style="color:rgb(221, 17, 68);background-color:rgb(246, 246, 246);">'inner'</font><font style="color:rgb(51, 51, 51);">（默认）、</font><font style="color:rgb(221, 17, 68);background-color:rgb(246, 246, 246);">'outer'</font><font style="color:rgb(51, 51, 51);">、</font><font style="color:rgb(221, 17, 68);background-color:rgb(246, 246, 246);">'left'</font><font style="color:rgb(51, 51, 51);">以及</font><font style="color:rgb(221, 17, 68);background-color:rgb(246, 246, 246);">'right'</font><font style="color:rgb(51, 51, 51);">四种方式。</font>

<font style="color:rgb(51, 51, 51);"> 1.</font><font style="color:rgb(221, 17, 68);background-color:rgb(246, 246, 246);">'inner'</font><font style="color:rgb(51, 51, 51);">（默认）：内连接，使用指定列的交集合并两个DataFrame数据集，即根据列名，匹配出相同列内容的数据：  
</font><font style="color:rgb(51, 51, 51);">例如以 "产品类型" 列作为合并列，两个DataFrame数据集中该列的交集只有一个：</font>

![](https://cdn.nlark.com/yuque/0/2023/png/1675452/1693399564635-204c8736-7f3a-4e79-bd00-86bd4e577f91.png)



<font style="color:rgb(51, 51, 51);"> 2.</font><font style="color:rgb(221, 17, 68);background-color:rgb(246, 246, 246);">'outer'</font><font style="color:rgb(51, 51, 51);">：外连接，使用指定列的并集合并两个DataFrame数据集，即根据列名匹配出所有列内容的数据，未匹配上的内容填为NaN：  
</font><font style="color:rgb(51, 51, 51);">例如以“产品类型”列作为合并列，匹配出两个DataFrame数据集中该列的所有内容数据：</font>

![](https://cdn.nlark.com/yuque/0/2023/png/1675452/1693399639067-1ef4be1d-387f-47c3-bef6-704892311c1d.png)



<font style="color:rgb(51, 51, 51);">3.</font><font style="color:rgb(221, 17, 68);background-color:rgb(246, 246, 246);">'left'</font><font style="color:rgb(51, 51, 51);">：左连接，使用左侧DataFrame数据集指定列，即根据列名左侧DataFrame取全部，右侧DataFrame取匹配的内容，未匹配上的内容填为NaN：</font>  
<font style="color:rgb(51, 51, 51);">例如以“产品类型”列作为合并列，取左侧df1的全部，右侧df2只取与df1完全匹配的数据，其余内容填为NaN：</font>

![](https://cdn.nlark.com/yuque/0/2023/png/1675452/1693399432189-7357dfea-5390-41cd-99ab-3be59aad4156.png)



<font style="color:rgb(51, 51, 51);">4.</font><font style="color:rgb(221, 17, 68);background-color:rgb(246, 246, 246);">'right'</font><font style="color:rgb(51, 51, 51);">：右连接，使用右侧DataFrame数据集指定列，即根据列名右侧DataFrame取全部，左侧DataFrame取匹配的内容，未匹配上的内容填为NaN：  
</font><font style="color:rgb(51, 51, 51);">例如以“产品类型”列作为合并列，取右侧df2的全部，左侧df1只取与df1完全匹配的数据，其余内容填为NaN：</font>

![](https://cdn.nlark.com/yuque/0/2023/png/1675452/1693399518263-fc4b7010-bb44-4551-acad-803f8c66f285.png)



**<font style="color:rgb(51, 51, 51);">left_on、 right_on：</font>**<font style="color:rgb(51, 51, 51);">当两个DataFrame数据集合并的指定列不相同时，使用左侧DataFrame中的”left_on”列和右侧DataFrame中的”right_on”列作为合并列：  
</font><font style="color:rgb(51, 51, 51);">例如df1的“产品类型1”列和df2的“产品类型2”列作为指定列的内连接：</font>

![](https://cdn.nlark.com/yuque/0/2023/png/1675452/1693400020643-752e2d33-310d-4bdb-9942-e35d785288f2.png)



**<font style="color:rgb(51, 51, 51);">left_index、ight_index：</font>**<font style="color:rgb(51, 51, 51);">根据左右侧DataFrame中共有的index进行合并，默认为False，使用时需为True</font>



**<font style="color:rgb(51, 51, 51);">sort：</font>**<font style="color:rgb(51, 51, 51);">按照字典顺序通过连接列对结果DataFrame进行排序；默认为True，设置为False时，在很多情况下大大提高性能。</font>

<font style="color:rgb(51, 51, 51);"></font>

**<font style="color:rgb(51, 51, 51);">suffixes：</font>**<font style="color:rgb(51, 51, 51);">对两个数据集中出现的重复列，新数据集中加上后缀进行区别,默认为</font><font style="color:rgb(221, 17, 68);background-color:rgb(246, 246, 246);">('_x', '_y')</font>



**<font style="color:rgb(51, 51, 51);">还有很多不太常用的参数，可以查找资料参考pandas库的read_excel方法去进行相关设置。</font>**



### <font style="color:rgb(51, 51, 51);">输出</font>
**<font style="color:rgb(51, 51, 51);">返回值：</font>**<font style="color:rgb(51, 51, 51);">返回merge(拼接)两个df后的结果数据，得到一个新的DataFrame。</font>













