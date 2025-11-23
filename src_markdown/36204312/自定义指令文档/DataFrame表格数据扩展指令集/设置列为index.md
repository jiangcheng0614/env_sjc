# 一.功能描述
<font style="color:rgb(51, 51, 51);">指定DataFrame的列为index。</font>

![](https://cdn.nlark.com/yuque/0/2023/jpeg/1675452/1692610129574-b7ef3ca0-0bbb-410e-b786-6c70bc4eeab8.jpeg)



# 二.<font style="color:rgb(51, 51, 51);">配置项说明</font>
### 输入
**<font style="color:rgb(51, 51, 51);">DataFrame</font>****<font style="color:rgb(51, 51, 51);">：</font>**<font style="color:rgb(51, 51, 51);">指定列为index操作的目标DataFrame</font>**<font style="color:rgb(51, 51, 51);">  
</font>**<font style="color:rgb(51, 51, 51);">例如传入【读取Excel】返回的DataFrame：</font>

![](https://cdn.nlark.com/yuque/0/2023/jpeg/1675452/1692590684043-8f7cc1bd-2375-4538-8cee-acdbc2a760ba.jpeg)



**<font style="color:rgb(51, 51, 51);">新索引：</font>**<font style="color:rgb(51, 51, 51);">输入目标列的列名，该列即为新的index；</font>**<font style="color:rgb(51, 51, 51);">  
</font>**<font style="color:rgb(51, 51, 51);">	1.默认为</font><font style="color:rgb(221, 17, 68);background-color:rgb(246, 246, 246);">None</font><font style="color:rgb(51, 51, 51);">，未指定列为新的index；</font>

<font style="color:rgb(51, 51, 51);"> 2.输入列名的字符串，指定该列为index：</font>

![](https://cdn.nlark.com/yuque/0/2023/jpeg/1675452/1692610155850-7c95bc48-dd29-4d2e-803c-97261b580957.jpeg)

<font style="color:rgb(51, 51, 51);"> </font>

<font style="color:rgb(51, 51, 51);">3.输入列名为元素组成的列表，指定所有元素对应列为index：</font>

![](https://cdn.nlark.com/yuque/0/2023/jpeg/1675452/1692610174155-66e5938b-6633-4657-b607-f166ec4513a4.jpeg)



**<font style="color:rgb(51, 51, 51);">是否删除索引：</font>**<font style="color:rgb(51, 51, 51);">默认为True，删除用作新索引的列.设置为False，则在不会删除。</font>

![](https://cdn.nlark.com/yuque/0/2023/jpeg/1675452/1692610193068-d0f6f947-62f9-4d82-a93a-b3210424fbe4.jpeg)



**<font style="color:rgb(51, 51, 51);">是否追加索引：</font>**<font style="color:rgb(51, 51, 51);">是否将列附加到现有索引,默认为False，不添加，即覆盖原有索引；设置为True，在原有索引的基础上在添加索引：</font>

![](https://cdn.nlark.com/yuque/0/2023/jpeg/1675452/1692610406700-a4c84910-5f7a-4076-b3d3-294d60a8b256.jpeg)

<font style="color:rgb(51, 51, 51);"></font>

**<font style="color:rgb(51, 51, 51);">原数据修改：</font>**<font style="color:rgb(51, 51, 51);">True表示直接在原来的DataFrame上删除重复项，传入的df变为设置列为index之后的DataFrame；而默认值False表示生成一个副本,传入的df不改变。</font>

<font style="color:rgb(51, 51, 51);">对传入的df做输出打印：</font>

    1. <font style="color:rgb(51, 51, 51);">默认为False的情况下，df的值不变：</font>
    2. <font style="color:rgb(51, 51, 51);">设置为True，改变原来传入df的值：</font>

![](https://cdn.nlark.com/yuque/0/2023/jpeg/1675452/1692610819395-f33e3157-fe01-4369-83a4-258db5ded7b0.jpeg)

<font style="color:rgb(51, 51, 51);"></font>

**<font style="color:rgb(51, 51, 51);">是否检查索引重复：</font>**<font style="color:rgb(51, 51, 51);">检查新索引是否重复；默认为False将提高此方法的性能。</font>

<font style="color:rgb(51, 51, 51);"></font>

### <font style="color:rgb(51, 51, 51);">输出</font>
**<font style="color:rgb(51, 51, 51);">返回值：</font>**<font style="color:rgb(51, 51, 51);">返回设置列为index后的新DataFrame。</font>

![](https://cdn.nlark.com/yuque/0/2023/jpeg/1675452/1692610951082-2685fd34-3494-4190-9706-58349b1aea25.jpeg)











