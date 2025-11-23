# 一.功能描述
<font style="color:rgb(51, 51, 51);">重新设置DataFrame的索引。</font>

_<font style="color:rgb(102, 102, 102);">注:如果DataFrame具有多个index，则此方法可以删除一个或多个级别。</font>_

![](https://cdn.nlark.com/yuque/0/2023/jpeg/1675452/1692624258122-e5baa505-6b83-4ab8-98b7-f40871a8c887.jpeg)





# 二.<font style="color:rgb(51, 51, 51);">配置项说明</font>
### 输入
**<font style="color:rgb(51, 51, 51);">DataFrame</font>****<font style="color:rgb(51, 51, 51);">：</font>**<font style="color:rgb(51, 51, 51);">传入重置index操作的目标DataFrame</font>**<font style="color:rgb(51, 51, 51);">  
</font>**<font style="color:rgb(51, 51, 51);">例如传入【读取Excel】返回的DataFrame：</font>

![](https://cdn.nlark.com/yuque/0/2023/jpeg/1675452/1692590684043-8f7cc1bd-2375-4538-8cee-acdbc2a760ba.jpeg)



**<font style="color:rgb(51, 51, 51);">level</font>****<font style="color:rgb(51, 51, 51);">：</font>**<font style="color:rgb(51, 51, 51);">删除指定索引，输入int, str, tuple 或 list等。</font>**<font style="color:rgb(51, 51, 51);">  
</font>**<font style="color:rgb(51, 51, 51);">	1.默认为</font><font style="color:rgb(221, 17, 68);background-color:rgb(246, 246, 246);">None</font><font style="color:rgb(51, 51, 51);">，删除所有索引，并使用默认索引（即 0,1,2,3……格式的整型索引）替代：</font>**<font style="color:rgb(51, 51, 51);">  
</font>**<font style="color:rgb(51, 51, 51);">例如下例中，默认为None，删除了原索引“产品”和“备注”，使用了默认的整型索引：</font>

![](https://cdn.nlark.com/yuque/0/2023/jpeg/1675452/1692624294549-a697ae3b-c4f2-4381-8d49-dcbee665a6e3.jpeg)

<font style="color:rgb(51, 51, 51);"></font>

<font style="color:rgb(51, 51, 51);">  2.输入索引名的字符串（str)或索引的下标(int)，删除该索引；</font>  
<font style="color:rgb(51, 51, 51);">设置为</font><font style="color:rgb(221, 17, 68);background-color:rgb(246, 246, 246);">1</font><font style="color:rgb(51, 51, 51);">,删除了第列列索引“产品”：</font>

![](https://cdn.nlark.com/yuque/0/2023/jpeg/1675452/1692624315660-48316f4d-8c8a-4b54-8bda-19ce81a886b6.jpeg)



<font style="color:rgb(51, 51, 51);"> 3.输入指定索引为元素组成的tuple/list ，或输入指定索引下标为元素组成的tuple/list ，删除指定索引：  
</font><font style="color:rgb(51, 51, 51);">设置为</font><font style="color:rgb(221, 17, 68);background-color:rgb(246, 246, 246);">(0,1)</font><font style="color:rgb(51, 51, 51);">,删除了第一和第二列索引：</font>

![](https://cdn.nlark.com/yuque/0/2023/jpeg/1675452/1692624331915-50fc94b1-4f0d-4409-8592-590508bcb156.jpeg)





**<font style="color:rgb(51, 51, 51);">drop</font>****<font style="color:rgb(51, 51, 51);">：</font>**<font style="color:rgb(51, 51, 51);">是否将删除的索引列重新插入到DataFrame中，默认为False。设置为True，则删除索引列不保留</font>

![](https://cdn.nlark.com/yuque/0/2023/jpeg/1675452/1692624349997-7c140e65-2d94-4785-a927-f0fa2a2d531d.jpeg)



**<font style="color:rgb(51, 51, 51);">col_level</font>****<font style="color:rgb(51, 51, 51);">：</font>**<font style="color:rgb(51, 51, 51);">保留索引列的（“drop”参数为False）情况下，设置索引列插入DataFrame的位置。默认为0，插入第一列；  
</font><font style="color:rgb(51, 51, 51);">例如设置为</font><font style="color:rgb(221, 17, 68);background-color:rgb(246, 246, 246);">'1'</font><font style="color:rgb(51, 51, 51);">，索引列设置为第二列：</font>

![](https://cdn.nlark.com/yuque/0/2023/jpeg/1675452/1692624372390-bc4f481e-f17d-4077-a08e-24aad8fbf973.jpeg)

<font style="color:rgb(51, 51, 51);"></font>

**<font style="color:rgb(51, 51, 51);">col_fill</font>****<font style="color:rgb(51, 51, 51);">：</font>**<font style="color:rgb(51, 51, 51);">表头有多个级别的情况下，用以设置保留索引列的其他级别索引列的列名，默认为</font><font style="color:rgb(221, 17, 68);background-color:rgb(246, 246, 246);">''</font><font style="color:rgb(51, 51, 51);">。如果输入None，则重复索引名称。</font>

<font style="color:rgb(51, 51, 51);"></font>

### <font style="color:rgb(51, 51, 51);">输出</font>
**<font style="color:rgb(51, 51, 51);">返回值：</font>**<font style="color:rgb(51, 51, 51);">返回重新设置索引后生成的DataFrame。</font>











