# 一.功能描述
<font style="color:rgb(51, 51, 51);">用以创建一个csv文件。</font>

_<font style="color:rgb(102, 102, 102);">CSV（Comma-Separated Values）是逗号分隔值（有时也称为字符分隔值，因为分隔字符也可以不是逗号），其文件以纯文本（数字和文本）形式存储表格数据。</font>_

![](https://cdn.nlark.com/yuque/0/2023/jpeg/1675452/1676871659028-88581319-d366-4bb3-be7e-8e9b9fe47e49.jpeg)



# 二.<font style="color:rgb(51, 51, 51);">配置项说明</font>
### 输入
**<font style="color:rgb(51, 51, 51);">保存目录：</font>**

<font style="color:rgb(51, 51, 51);">指定新建csv文件存放的目录，可点击参数后的文件夹图标进行选择目录。</font>

**<font style="color:rgb(51, 51, 51);">文件名称：</font>**

<font style="color:rgb(51, 51, 51);">设置csv文件的名称。</font>

**分隔符：**

<font style="color:rgb(51, 51, 51);">设置CSV文件的分隔符，输入为字符串，默认为逗号。</font>

**编码：**

<font style="color:rgb(51, 51, 51);">设</font><font style="color:rgb(51, 51, 51);">置文件的编码格式，输入为字符串，默认为’ANSI’。</font>

**列名：**

<font style="color:rgb(51, 51, 51);">设置CSV文件的表头，输入为列表，列表内的元素按下标顺序依次作为对应列的列名。</font>

**索引列：**

<font style="color:rgb(51, 51, 51);">表示是否需要行索引，默认为False，不需要，创建的表格中便不会出现行索引，True则生成索引行。</font>

**是否覆盖：**

<font style="color:rgb(51, 51, 51);">默认为“是”，即保存目录下已存在所要创建的csv文件时，会自动覆盖掉原有文件的内容；设置为“否”，则文件已经存在时，抛出异常。</font>

### <font style="color:rgb(51, 51, 51);">输出</font>
返回创建CSV文件路径**<font style="color:rgb(51, 51, 51);">：</font>**

返回创建CSV文件的路径   例：如下图片显示

![](https://cdn.nlark.com/yuque/0/2023/jpeg/1675452/1676871937888-a5ed4b13-220d-4306-8237-fe83448e657a.jpeg)



