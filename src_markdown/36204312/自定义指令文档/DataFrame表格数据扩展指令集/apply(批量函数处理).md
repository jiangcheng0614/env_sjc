# 一.功能描述
<font style="color:rgb(51, 51, 51);">通过使用apply方法，可以调用自己定义的函数。既可以作用于一行或者一列的元素，也可以作用于单个元素。</font>

![](https://cdn.nlark.com/yuque/0/2023/jpeg/1675452/1692950628895-7420cc26-70fc-4d67-9788-8525f97a7490.jpeg)

_<font style="color:rgb(102, 102, 102);">注：传递给函数的对象是Series对象，其索引是DataFrame的index（axis=0）或DataFramed的columns（axis=1）。默认情况下（result_type=None），根据函数的返回类型推断最终的返回类型，否则，取决于result_type参数。</font>_





# 二.<font style="color:rgb(51, 51, 51);">配置项说明</font>
### 输入
**<font style="color:rgb(51, 51, 51);">DataFrame</font>****<font style="color:rgb(51, 51, 51);">：</font>**<font style="color:rgb(51, 51, 51);">传入目标DataFrame对象。</font>**<font style="color:rgb(51, 51, 51);">  
</font>**<font style="color:rgb(51, 51, 51);">例如传入【读取Excel】返回的DataFrame：</font>

![](https://cdn.nlark.com/yuque/0/2023/jpeg/1675452/1692590684043-8f7cc1bd-2375-4538-8cee-acdbc2a760ba.jpeg)



**<font style="color:rgb(51, 51, 51);">func</font>****<font style="color:rgb(51, 51, 51);">：</font>**<font style="color:rgb(51, 51, 51);">传入应用于行或列的函数。</font>**<font style="color:rgb(51, 51, 51);">  
</font>**<font style="color:rgb(51, 51, 51);">	1.使用lambda匿名函数调用内置方法或简单语句 例如：</font><font style="color:rgb(221, 17, 68);background-color:rgb(246, 246, 246);">lambda x:max(x)</font><font style="color:rgb(51, 51, 51);">，获取最大值：</font>

![](https://cdn.nlark.com/yuque/0/2023/jpeg/1675452/1692950688822-b4c5a3e0-f519-48b1-81c9-d14d835c0559.jpeg)



2.使用lambda匿名函数调用python自定义函数方法 例如：lambda x: get_addData(x.产品风险等级,x.视频保存时长)

def get_addData(x.产品风险等级,x.视频保存时长):  方法预先写在python代码块中，通过apply方法逐行遍历调用。



![](https://cdn.nlark.com/yuque/0/2023/jpeg/1675452/1692951172982-e224cd15-dfdd-40df-a4a4-e238a88a875e.jpeg)



![](https://cdn.nlark.com/yuque/0/2023/jpeg/1675452/1692951184702-7bcc9276-aaca-4d7c-acfd-70827ac02a25.jpeg)





**<font style="color:rgb(51, 51, 51);">axis</font>****<font style="color:rgb(51, 51, 51);">：</font>**<font style="color:rgb(51, 51, 51);">设置沿DataFrame的轴，默认为 </font><font style="color:rgb(221, 17, 68);background-color:rgb(246, 246, 246);">0</font><font style="color:rgb(51, 51, 51);">，函数应用于每一行。</font>

<font style="color:rgb(51, 51, 51);">输入</font><font style="color:rgb(221, 17, 68);background-color:rgb(246, 246, 246);">0</font><font style="color:rgb(51, 51, 51);">或 </font><font style="color:rgb(221, 17, 68);background-color:rgb(246, 246, 246);">'index'</font><font style="color:rgb(51, 51, 51);">，将函数应用于每一列；  
</font><font style="color:rgb(51, 51, 51);">输入</font><font style="color:rgb(221, 17, 68);background-color:rgb(246, 246, 246);">1</font><font style="color:rgb(51, 51, 51);">或 </font><font style="color:rgb(221, 17, 68);background-color:rgb(246, 246, 246);">'columns'</font><font style="color:rgb(51, 51, 51);">，将函数应用于每一行。		  
</font><font style="color:rgb(51, 51, 51);">例如修改默认值，设置为</font><font style="color:rgb(221, 17, 68);background-color:rgb(246, 246, 246);">1</font><font style="color:rgb(51, 51, 51);">，函数应用于每行:</font>

![](https://cdn.nlark.com/yuque/0/2023/jpeg/1675452/1692950724488-352fb86c-0b36-4a01-b58d-1482ef3e4f73.jpeg)



**<font style="color:rgb(51, 51, 51);">raw：</font>**<font style="color:rgb(51, 51, 51);">设置将行或列作为Series或ndarray对象传递。</font>  
<font style="color:rgb(51, 51, 51);">默认为False，将每个行或列作为Series传递给函数；</font>  
<font style="color:rgb(51, 51, 51);">设置为True，则传递ndarray对象给函数。</font>

<font style="color:rgb(51, 51, 51);"></font>

**<font style="color:rgb(51, 51, 51);">result_type：</font>**<font style="color:rgb(51, 51, 51);">可输入</font><font style="color:rgb(221, 17, 68);background-color:rgb(246, 246, 246);">'expand'</font><font style="color:rgb(51, 51, 51);">、</font><font style="color:rgb(221, 17, 68);background-color:rgb(246, 246, 246);">'reduce'</font><font style="color:rgb(51, 51, 51);">、</font><font style="color:rgb(221, 17, 68);background-color:rgb(246, 246, 246);">'broadcast'</font><font style="color:rgb(51, 51, 51);">或</font><font style="color:rgb(221, 17, 68);background-color:rgb(246, 246, 246);">None</font><font style="color:rgb(51, 51, 51);">，用以设置最终的返回类型；</font>

<font style="color:rgb(51, 51, 51);">1.默认为</font><font style="color:rgb(221, 17, 68);background-color:rgb(246, 246, 246);">None</font><font style="color:rgb(51, 51, 51);">，根据函数的返回类型推断最终的返回类型。</font>

![](https://cdn.nlark.com/yuque/0/2023/jpeg/1675452/1692951532450-2bedf05a-ffd9-46a3-b678-1ea6e6793c8c.jpeg)





<font style="color:rgb(51, 51, 51);">2.只有“axis”参数设置为</font><font style="color:rgb(221, 17, 68);background-color:rgb(246, 246, 246);">1</font><font style="color:rgb(51, 51, 51);"> 或</font><font style="color:rgb(221, 17, 68);background-color:rgb(246, 246, 246);">'columns'</font><font style="color:rgb(51, 51, 51);">，才可输入</font><font style="color:rgb(221, 17, 68);background-color:rgb(246, 246, 246);">'expand'</font><font style="color:rgb(51, 51, 51);">,</font><font style="color:rgb(221, 17, 68);background-color:rgb(246, 246, 246);">'reduce'</font><font style="color:rgb(51, 51, 51);">以及 </font><font style="color:rgb(221, 17, 68);background-color:rgb(246, 246, 246);">'broadcast'</font><font style="color:rgb(51, 51, 51);">:</font>  
<font style="color:rgb(221, 17, 68);background-color:rgb(246, 246, 246);">'expand'</font><font style="color:rgb(51, 51, 51);">：将类似列表的结果数据扩展为DataFrame的列；</font>  
<font style="color:rgb(221, 17, 68);background-color:rgb(246, 246, 246);">'reduce'</font><font style="color:rgb(51, 51, 51);">：和’expand’相反，返回一个Series ；</font>  
<font style="color:rgb(221, 17, 68);background-color:rgb(246, 246, 246);">'broadcast'</font><font style="color:rgb(51, 51, 51);">：结果将以DataFrame的原始形态传递，原始索引和列将保留。</font>  
<font style="color:rgb(51, 51, 51);">例如，默认情况下输入列表：</font>

![](https://cdn.nlark.com/yuque/0/2023/jpeg/1675452/1692950765953-eb431296-aacb-48d4-b7a1-cbe6baff4075.jpeg)

<font style="color:rgb(51, 51, 51);"></font>

![](https://cdn.nlark.com/yuque/0/2023/png/1675452/1692951002236-8bbd437c-e424-4535-99a2-c6177956ab99.png)



<font style="color:rgb(51, 51, 51);">设置为</font><font style="color:rgb(221, 17, 68);background-color:rgb(246, 246, 246);">'expand'</font><font style="color:rgb(51, 51, 51);">:</font>

![](https://cdn.nlark.com/yuque/0/2023/jpeg/1675452/1692950765953-eb431296-aacb-48d4-b7a1-cbe6baff4075.jpeg)



![](https://cdn.nlark.com/yuque/0/2023/jpeg/1675452/1692950819471-3f6063cf-5e2b-425f-b8a6-7bc8ac37118d.jpeg)



<font style="color:rgb(51, 51, 51);"></font>

### <font style="color:rgb(51, 51, 51);">输出</font>
**<font style="color:rgb(51, 51, 51);">返回值：</font>**<font style="color:rgb(51, 51, 51);">如果“函数”参数为None，返回原DataFrame；否则返回函数处理后的结果DataFrame或Series。</font>



 









