# 一.功能描述
<font style="color:rgb(51, 51, 51);">将DataFrame中时间列的内容转为时间戳格式。</font><font style="color:rgb(77, 77, 77);">也就是该指令可以将字符型的时间数据转换为时间型数据</font>

![](https://cdn.nlark.com/yuque/0/2023/jpeg/1675452/1692930704367-47b63113-e1cc-4fab-8646-0c2881765cae.jpeg)



# 二.基本使用说明
<font style="color:rgb(51, 51, 51);">传入含有时间列的DataFrame，将该列转化为时间戳：</font>

![](https://cdn.nlark.com/yuque/0/2023/jpeg/1675452/1692930729618-286d9010-8a07-43e6-b228-4a736262902a.jpeg)



# 三.<font style="color:rgb(51, 51, 51);">配置项说明</font>
### 输入
**<font style="color:rgb(51, 51, 51);">DataFrame</font>****<font style="color:rgb(51, 51, 51);">：</font>**<font style="color:rgb(51, 51, 51);">输入进行转化列为日期操作的目标DataFrame；</font>**<font style="color:rgb(51, 51, 51);">  
</font>**<font style="color:rgb(51, 51, 51);">例如传入【读取Excel】返回的DataFrame：</font>

![](https://cdn.nlark.com/yuque/0/2023/jpeg/1675452/1692590684043-8f7cc1bd-2375-4538-8cee-acdbc2a760ba.jpeg)



**<font style="color:rgb(51, 51, 51);">列名</font>****<font style="color:rgb(51, 51, 51);">：</font>**<font style="color:rgb(51, 51, 51);">输入表格中时间列的列名；</font>**<font style="color:rgb(51, 51, 51);"></font>**



**<font style="color:rgb(51, 51, 51);">format</font>****<font style="color:rgb(51, 51, 51);">：</font>**<font style="color:rgb(51, 51, 51);">设置返回的时间格式，如 format="%Y-%m-%d %H:%M:%S" 或 format="%Y-%m-%d"；</font>



**<font style="color:rgb(51, 51, 51);">errors：</font>**<font style="color:rgb(36, 41, 47);">指定在遇到错误时的处理方式，可选值为’raise’（抛出异常，默认）、‘coerce’（将无法转换的值设为NaT）和’ignore’（保持原始值）。</font>

<font style="color:rgb(51, 51, 51);">  raise（默认）：无效的解析将引发异常；  
</font><font style="color:rgb(51, 51, 51);">	ignore：无效的解析将返回输入；  
</font><font style="color:rgb(51, 51, 51);">	coerce：无效的解析将被设置为NaT</font>



**<font style="color:rgb(51, 51, 51);">dayfirst：</font>**<font style="color:rgb(36, 41, 47);">用于指定日期字符串中日期部分是否优先显示。</font><font style="color:rgb(51, 51, 51);">布尔类型选项，True：如</font><font style="color:rgb(36, 41, 47);">“2022-03-15”解析为 15 日 3 月 2022 年；</font><font style="color:rgb(51, 51, 51);">默认为False；</font>



**<font style="color:rgb(36, 41, 47);">yearfirst：</font>**<font style="color:rgb(36, 41, 47);">用于指定日期字符串中年份是否优先显示。</font><font style="color:rgb(51, 51, 51);">布尔类型选项，True：</font><font style="color:rgb(36, 41, 47);"> </font><font style="color:rgb(51, 51, 51);">如</font><font style="color:rgb(36, 41, 47);">“2022-03-15”</font><font style="color:rgb(51, 51, 51);"> 解析为</font><font style="color:rgb(36, 41, 47);">2022 年 3 月 15 日；</font><font style="color:rgb(51, 51, 51);">默认为False；</font>

<font style="color:rgb(51, 51, 51);"></font>

**<font style="color:rgb(51, 51, 51);">utc：</font>**<font style="color:rgb(51, 51, 51);">布尔类型选项，True：返回UTC DatetimeIndex（转换任何感知到tz的信号）；默认为False；</font>

<font style="color:rgb(51, 51, 51);"></font>

**<font style="color:rgb(51, 51, 51);">exact：</font>**<font style="color:rgb(51, 51, 51);">布尔类型选项，True：要求精确的格式匹配；False：允许格式匹配目标字符串中的任何位置；</font>

<font style="color:rgb(51, 51, 51);"></font>

**<font style="color:rgb(51, 51, 51);">unit：</font>**<font style="color:rgb(51, 51, 51);">初始时间的单位，默认为None；</font>

<font style="color:rgb(51, 51, 51);"></font>

**<font style="color:rgb(51, 51, 51);">infer_datetime：</font>**<font style="color:rgb(51, 51, 51);">如果为True并且未给出“format”，则会尝试推断datetime字符串；在某些情况下，可能会增加解析度，速度提高约5-10倍；</font>

<font style="color:rgb(51, 51, 51);"></font>

**<font style="color:rgb(51, 51, 51);">origin：</font>**<font style="color:rgb(51, 51, 51);">定义参考日期的标量，默认为’unix’；数值将解析为数字；“unix”： 原点设置为1970-01-01”；“julian”：单位必须为’D’，并且origin设置为的开头；</font>

<font style="color:rgb(51, 51, 51);"></font>

**<font style="color:rgb(51, 51, 51);">cache：</font>**<font style="color:rgb(51, 51, 51);">布尔类型选项，True：使用唯一的转换日期缓存来应用datetime转换，解析重复日期时可能会产生明显的提速，尤其是具有时区偏移的字符串。</font>

<font style="color:rgb(51, 51, 51);"></font>

### <font style="color:rgb(51, 51, 51);">输出</font>
**<font style="color:rgb(51, 51, 51);">返回值：</font>**<font style="color:rgb(51, 51, 51);">返回df列转换时间数据值</font>













