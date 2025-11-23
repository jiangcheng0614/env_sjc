# 一.功能描述
<font style="color:rgb(51, 51, 51);">通过使用指定方法填充DataFrame数据中的NA/NaN值。</font>

![](https://cdn.nlark.com/yuque/0/2023/jpeg/1675452/1692672862384-c59c514b-3d75-4fde-a832-1eb903146742.jpeg)



# 二.<font style="color:rgb(51, 51, 51);">配置项说明</font>
### 输入
**<font style="color:rgb(51, 51, 51);">DataFrame</font>****<font style="color:rgb(51, 51, 51);">：</font>**<font style="color:rgb(51, 51, 51);">传入进行填充NaN值操作的DataFrame数据。</font>**<font style="color:rgb(51, 51, 51);">  
</font>**<font style="color:rgb(51, 51, 51);">例如传入【读取Excel】返回的DataFrame：</font>

![](https://cdn.nlark.com/yuque/0/2023/jpeg/1675452/1692590684043-8f7cc1bd-2375-4538-8cee-acdbc2a760ba.jpeg)



**<font style="color:rgb(51, 51, 51);">填充值：</font>**<font style="color:rgb(51, 51, 51);">设置用于填充空值的值；注意不能传入list：</font>**<font style="color:rgb(51, 51, 51);">  
</font>**<font style="color:rgb(51, 51, 51);">	1.传入字符串，该字符串填充所有的空值，默认为</font><font style="color:rgb(221, 17, 68);background-color:rgb(246, 246, 246);">''</font><font style="color:rgb(51, 51, 51);">，即默认空字符串填充所有空值。</font>**<font style="color:rgb(51, 51, 51);">  
</font>**<font style="color:rgb(51, 51, 51);">又例如输入字符串</font><font style="color:rgb(221, 17, 68);background-color:rgb(246, 246, 246);">'values'</font><font style="color:rgb(51, 51, 51);">，用字符串’values’填充所有空值：</font>

![](https://cdn.nlark.com/yuque/0/2023/jpeg/1675452/1692672866365-65f2bb13-657e-40b1-9b2f-fb747bc87ba5.jpeg)



<font style="color:rgb(51, 51, 51);"> 2.传入列名为key，填充值为value的字典，用字典内的value填充指定key列内的空值，未指定的列内的空值不变。</font>  
<font style="color:rgb(51, 51, 51);">例如</font><font style="color:rgb(221, 17, 68);background-color:rgb(246, 246, 246);">{'产品代码':'备用1','备注':'备用2'}</font><font style="color:rgb(51, 51, 51);">，“备用1”填充“</font><font style="color:rgb(221, 17, 68);background-color:rgb(246, 246, 246);">产品代码</font><font style="color:rgb(51, 51, 51);">”列内的空值，“备用2”填充“</font><font style="color:rgb(221, 17, 68);background-color:rgb(246, 246, 246);">备注</font><font style="color:rgb(51, 51, 51);">”列内的空值:</font>

![](https://cdn.nlark.com/yuque/0/2023/jpeg/1675452/1692672881224-1ec41658-4a80-4c11-8acf-50e6511badb9.jpeg)



**<font style="color:rgb(51, 51, 51);">填充方式：</font>**<font style="color:rgb(51, 51, 51);">定义了填充空值的方法， 包括{‘backfill’, ‘bfill’, ‘pad’, ‘ffill’, None}，默认为None。其中’pad’和 ‘ffill’ 表示用前面 行/列（行或列取决于“axis”参数，默认情况下为行） 的值，填充当前的空值， ‘backfill’ 和 ‘bfill’表示用后面 行/列 的值，填充当前的空值。  
</font><font style="color:rgb(51, 51, 51);">例如，“填充方式”参数传入</font><font style="color:rgb(221, 17, 68);background-color:rgb(246, 246, 246);">'pad'</font><font style="color:rgb(51, 51, 51);">：</font>

![](https://cdn.nlark.com/yuque/0/2023/jpeg/1675452/1692672933169-a194254c-19ef-46b6-b16b-9446358a32a3.jpeg)

_<font style="color:rgb(102, 102, 102);">注：“填充值”参数 和 “填充方式”两个参数必须有且只能有一个参数进行了设置，而指令上显示的"填充值"参数默认值</font>__<font style="color:rgb(221, 17, 68);background-color:rgb(246, 246, 246);">''</font>__<font style="color:rgb(102, 102, 102);">实际已经是进行了修改，所以在设置“填充方式”参数时，先将“填充值”参数设置为None。</font>_



_<font style="color:rgb(102, 102, 102);"></font>_

**<font style="color:rgb(51, 51, 51);">填充方向：</font>**<font style="color:rgb(51, 51, 51);">设置填充的方向，</font><font style="color:rgb(221, 17, 68);background-color:rgb(246, 246, 246);">0</font><font style="color:rgb(51, 51, 51);"> 或 </font><font style="color:rgb(221, 17, 68);background-color:rgb(246, 246, 246);">'index'</font><font style="color:rgb(51, 51, 51);">，从第一列开始逐列填充；</font><font style="color:rgb(221, 17, 68);background-color:rgb(246, 246, 246);">1</font><font style="color:rgb(51, 51, 51);"> 或 </font><font style="color:rgb(221, 17, 68);background-color:rgb(246, 246, 246);">'columns'</font><font style="color:rgb(51, 51, 51);">，从第一行开始逐行填充。</font>

<font style="color:rgb(51, 51, 51);"></font>

<font style="color:rgb(51, 51, 51);"></font>

**<font style="color:rgb(51, 51, 51);">填充个数限制：</font>**<font style="color:rgb(51, 51, 51);">设置填充个数的最大限制，默认为None，输入大于等于1的整型数字。如果"填充方式"被指定，对于连续的空值，这段连续区域，最多填充前 "</font>**<font style="color:rgb(51, 51, 51);">填充个数限制"</font>**<font style="color:rgb(51, 51, 51);"> 个空值（如果存在多段连续区域，每段最多填充前"</font>**<font style="color:rgb(51, 51, 51);">填充个数限制"</font>**<font style="color:rgb(51, 51, 51);">  个空值）。如果"填充方式"未被指定， 在该"填充方向"下，最多填充前 "</font>**<font style="color:rgb(51, 51, 51);">填充个数限制"</font>**<font style="color:rgb(51, 51, 51);">  个空值（不论空值连续区间是否间断）</font>

![](https://cdn.nlark.com/yuque/0/2023/jpeg/1675452/1692673014550-d9b435fe-8f1b-4004-8e2d-df794e42610a.jpeg)

<font style="color:rgb(51, 51, 51);"></font>

<font style="color:rgb(51, 51, 51);"></font>

**<font style="color:rgb(51, 51, 51);">downcast</font>****<font style="color:rgb(51, 51, 51);">：</font>**<font style="color:rgb(51, 51, 51);">输入为dict，默认为None。输入item-> dtype的字典，如果可能的话，将向下转换，或者是字符串“infer”，它将尝试向下转换为适当的等同类型（例如，如果可能，则从float64到int64）。</font>

<font style="color:rgb(51, 51, 51);"></font>

**<font style="color:rgb(51, 51, 51);">原数据修改</font>****<font style="color:rgb(51, 51, 51);">：</font>**<font style="color:rgb(51, 51, 51);">True表示直接在原来的DataFrame上删除重复项，传入的df变为填充NaN之后的DataFrame；而默认值False表示生成一个副本,传入的df不改变。</font>

    1. <font style="color:rgb(51, 51, 51);">对传入的df做输出打印，默认为False的情况下，df的值不变；</font>
    2. <font style="color:rgb(51, 51, 51);">设置为True，改变原来传入df的值。</font>

_<font style="color:rgb(102, 102, 102);"></font>_

### <font style="color:rgb(51, 51, 51);">输出</font>
**<font style="color:rgb(51, 51, 51);">返回值：</font>**<font style="color:rgb(51, 51, 51);">返回NaN值被填充后的DataFrame。</font>











