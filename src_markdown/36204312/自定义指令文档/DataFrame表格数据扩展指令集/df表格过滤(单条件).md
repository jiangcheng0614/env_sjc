# 一.功能描述
<font style="color:rgb(51, 51, 51);">对获取到的DataFrame数据集进行单条件过滤操作，并将过滤后的数据返回。</font>

![](https://cdn.nlark.com/yuque/0/2023/png/1675452/1692956705488-28020900-096e-46e3-9e5d-42e279a48eed.png)

_<font style="color:rgb(102, 102, 102);">注：  
</font>__<font style="color:rgb(102, 102, 102);">1.过滤处理的对象类型为DataFrame，仅支持单个条件过滤；  
</font>__<font style="color:rgb(102, 102, 102);">2.数据过滤后的返回值依旧为DataFrame类型数据集。</font>_



# 二.基本使用说明
通过指定筛选字段列，指定筛选方式，和需要筛选过滤的出的值范围，筛选出df的数据范围。

![](https://cdn.nlark.com/yuque/0/2023/jpeg/1675452/1692956727568-059ad89c-1253-4004-8fa4-9cb884d7b30b.jpeg)





# 三.<font style="color:rgb(51, 51, 51);">配置项说明</font>
### 输入
**<font style="color:rgb(51, 51, 51);">DataFrame</font>****<font style="color:rgb(51, 51, 51);">：</font>**<font style="color:rgb(51, 51, 51);">传入待过滤处理的表格数据，输入类型为Dataframe；</font>**<font style="color:rgb(51, 51, 51);">  
</font>**<font style="color:rgb(51, 51, 51);">例如传入【读取Excel】返回的DataFrame：</font>

![](https://cdn.nlark.com/yuque/0/2023/jpeg/1675452/1692590684043-8f7cc1bd-2375-4538-8cee-acdbc2a760ba.jpeg)



**<font style="color:rgb(51, 51, 51);">筛选字段：</font>**<font style="color:rgb(51, 51, 51);">输入指定列的字段名称；</font>

<font style="color:rgb(51, 51, 51);">1.指定列的列名是字符串时，输入字符串；列名为整型数字时，直接输入数字。</font>

<font style="color:rgb(51, 51, 51);">2.输入参数也支持传入变量操作</font>**<font style="color:rgb(51, 51, 51);"></font>**





**<font style="color:rgb(51, 51, 51);">筛选方式：</font>**<font style="color:rgb(51, 51, 51);">下拉选择筛选方法，默认为“==”，也就是等于。</font>

<font style="color:rgb(51, 51, 51);">下面依次介绍这些方法：</font>  
<font style="color:rgb(51, 51, 51);">“ </font>**<font style="color:rgb(51, 51, 51);">==</font>**<font style="color:rgb(51, 51, 51);"> ”：匹配指定列的内容中等于指定值的数据，例如匹配“产品名称”列中内容为“name0002”的数据；</font>

**<font style="color:rgb(51, 51, 51);">筛选值：</font>**<font style="color:rgb(51, 51, 51);">"name0002"</font>

<font style="color:rgb(51, 51, 51);"></font>

<font style="color:rgb(51, 51, 51);">“ </font>**<font style="color:rgb(51, 51, 51);">> </font>**<font style="color:rgb(51, 51, 51);">”: 匹配指定列的内容中大于指定值的数据，如匹配“产品风险级别”列中内容大于5的数据:</font>

**<font style="color:rgb(51, 51, 51);">筛选值：</font>**<font style="color:rgb(51, 51, 51);">5</font>



<font style="color:rgb(51, 51, 51);">“ </font>**<font style="color:rgb(51, 51, 51);">>=</font>**<font style="color:rgb(51, 51, 51);"> ”: 匹配指定列的内容中大于或等于指定值的数据，如匹配“产品风险等级”列中内容大于等于5的数据:</font>

**<font style="color:rgb(51, 51, 51);">筛选值：</font>**<font style="color:rgb(51, 51, 51);">5</font>

<font style="color:rgb(51, 51, 51);"></font>

<font style="color:rgb(51, 51, 51);">“ </font>**<font style="color:rgb(51, 51, 51);">< </font>**<font style="color:rgb(51, 51, 51);">”: 匹配指定列的内容中小于指定值的数据，如匹配“视频保存时长”列中内容小于6的数据:</font>

**<font style="color:rgb(51, 51, 51);">筛选值：</font>**<font style="color:rgb(51, 51, 51);">6</font>

<font style="color:rgb(51, 51, 51);"></font>

<font style="color:rgb(51, 51, 51);">“ </font>**<font style="color:rgb(51, 51, 51);"><= </font>**<font style="color:rgb(51, 51, 51);">”: 匹配指定列的内容中小于或等于指定值的数据，如匹配“视频保存时长”列中内容小于或等于6的数据参考:</font>

**<font style="color:rgb(51, 51, 51);">筛选值：</font>**<font style="color:rgb(51, 51, 51);">6</font>

<font style="color:rgb(51, 51, 51);"></font>

<font style="color:rgb(51, 51, 51);">“ </font>**<font style="color:rgb(51, 51, 51);">!= </font>**<font style="color:rgb(51, 51, 51);">”: 匹配指定列的内容中不等于指定值的数据，如匹配“产品名称”列中内容不为“name0002”的数据参考:</font>

**<font style="color:rgb(51, 51, 51);">筛选值：</font>**<font style="color:rgb(51, 51, 51);">"name0002"</font>

<font style="color:rgb(51, 51, 51);"></font>

<font style="color:rgb(51, 51, 51);">“</font>**<font style="color:rgb(51, 51, 51);">contains</font>**<font style="color:rgb(51, 51, 51);">”：匹配指定列的内容中字符串数据，包含字符串子集，也可以通过正则匹配。例如“产品代码”列中开头为“zs”的数据：</font>

**<font style="color:rgb(51, 51, 51);">筛选值："zs"     </font>**

**<font style="color:rgb(51, 51, 51);">筛选值："zs.*" </font>**

**<font style="color:rgb(51, 51, 51);">以上两种方法均可，     </font>**

_<font style="color:rgb(102, 102, 102);">注意：如果筛选的列中有空值，则会抛出异常，需要进行过滤空值。</font>_

<font style="color:rgb(51, 51, 51);"></font>

<font style="color:rgb(51, 51, 51);">“</font>**<font style="color:rgb(51, 51, 51);">startswith</font>**<font style="color:rgb(51, 51, 51);">”：匹配指定列的内容中以某个字符开头的数据，如匹配“产品代码”列中开头为“zs”的数据：</font>

**<font style="color:rgb(51, 51, 51);">筛选值："zs"</font>**

_<font style="color:rgb(102, 102, 102);">注意：如果筛选的列中有空值，则会抛出异常，需要进行过滤空值。</font>_

_<font style="color:rgb(102, 102, 102);"></font>_

<font style="color:rgb(51, 51, 51);">“ </font>**<font style="color:rgb(51, 51, 51);">notna</font>**<font style="color:rgb(51, 51, 51);"> ”：匹配指定列的内容中不为空的数据，例如匹配“产品代码”列中内容不为空的记录：</font>

**<font style="color:rgb(51, 51, 51);">筛选值：(不填值)</font>**

_<font style="color:rgb(102, 102, 102);">也可应用于类似上例中，去除筛选列中的空值，避免抛出异常：</font>_

_<font style="color:rgb(102, 102, 102);"></font>_

<font style="color:rgb(51, 51, 51);">“ </font>**<font style="color:rgb(51, 51, 51);">endswith </font>**<font style="color:rgb(51, 51, 51);">”：匹配指定列的内容中以某个字符结束的数据，如“产品代码”列中为“0002”结尾的记录：</font>

**<font style="color:rgb(51, 51, 51);">筛选值：</font>**<font style="color:rgb(51, 51, 51);">"0002"</font>

_<font style="color:rgb(102, 102, 102);">同样，若是筛选的列中有空值，则会抛出异常，需要进行过滤空值。</font>_

_<font style="color:rgb(102, 102, 102);"></font>_

<font style="color:rgb(51, 51, 51);">“ </font>**<font style="color:rgb(51, 51, 51);">match</font>**<font style="color:rgb(51, 51, 51);"> ”：比对指定列的内容中与正则表达式匹配的数据，注意筛选的列中不能有空值，否则会抛出异常；例如“产品代码”列中匹配符合</font><font style="color:rgb(221, 17, 68);background-color:rgb(246, 246, 246);">'zs.*'</font><font style="color:rgb(51, 51, 51);">正则表达式的数据：</font>

**<font style="color:rgb(51, 51, 51);">筛选值："zs.*"</font>**

**<font style="color:rgb(51, 51, 51);"></font>**

<font style="color:rgb(51, 51, 51);">“ </font>**<font style="color:rgb(51, 51, 51);">isnull</font>**<font style="color:rgb(51, 51, 51);"> ”：匹配指定列的内容中为空的数据，例如匹配“产品代码”列中内容为空的记录：</font>

**<font style="color:rgb(51, 51, 51);">筛选值：(不填值)</font>**

**<font style="color:rgb(51, 51, 51);"></font>**

<font style="color:rgb(51, 51, 51);">“ </font>**<font style="color:rgb(51, 51, 51);">isin </font>**<font style="color:rgb(51, 51, 51);">”：匹配指定列的内容中包含指定字符的数据，注意指定字符的内容需填写完全一致，写入列表输入，例如匹配“产品类型”列中内容为“A1”的记录：</font>

**<font style="color:rgb(51, 51, 51);">筛选值：["A1"]       </font>**

**<font style="color:rgb(51, 51, 51);">筛选值："A1"   （不可直接填写"A1",触发异常）</font>**

_<font style="color:rgb(102, 102, 102);">注意：指定字符不能直接输入，否则会抛出异常，提示需要传入一个list-like的对象数据。</font>_

_<font style="color:rgb(102, 102, 102);"></font>_

_<font style="color:rgb(102, 102, 102);"></font>_

**<font style="color:rgb(51, 51, 51);">筛选值：</font>**<font style="color:rgb(51, 51, 51);">输入匹配条件的内容。</font>

<font style="color:rgb(51, 51, 51);"></font>

### <font style="color:rgb(51, 51, 51);">输出</font>
**<font style="color:rgb(51, 51, 51);">返回值：</font>**<font style="color:rgb(51, 51, 51);"> 返回表格单条件过滤后得到的数据，其类型依旧为Dataframe。</font>



![](https://cdn.nlark.com/yuque/0/2023/jpeg/1675452/1692958830123-c897ccaf-7174-4402-9788-1574be1363f3.jpeg)











