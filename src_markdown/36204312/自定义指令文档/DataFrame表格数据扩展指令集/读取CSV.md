# 一.功能描述
<font style="color:rgb(51, 51, 51);">读取CSV文件中的数据，并将读取到的内容进行返回。</font>

![](https://cdn.nlark.com/yuque/0/2023/jpeg/1675452/1693365957794-da4b0c6b-4b57-4437-b33a-c301ff962046.jpeg)

_<font style="color:rgb(102, 102, 102);">注：组件使用的是pandas库的read_csv()方法，返回的是一个DataFrame数据集。</font>_





# 二.**<font style="color:rgb(51, 51, 51);">基本使用说明</font>**
<font style="color:rgb(51, 51, 51);">1.点击“文件路径”参数后的文件图标，选择需要读取的CSV文件：</font>



<font style="color:rgb(51, 51, 51);">2.组件返回值即csv文件的内容，其类型为DataFrame数据集：</font>

![](https://cdn.nlark.com/yuque/0/2023/jpeg/1675452/1693365981467-b1d240e1-9544-43f1-8365-20b68799f3da.jpeg)





# 三.<font style="color:rgb(51, 51, 51);">配置项说明</font>
### 输入
**<font style="color:rgb(51, 51, 51);">文件路径</font>****<font style="color:rgb(51, 51, 51);">：</font>**<font style="color:rgb(51, 51, 51);">填写读取的CSV文件的路径，输入为字符串；可点击右侧的选择文件图标进行选择。</font>



**<font style="color:rgb(51, 51, 51);">sep</font>****<font style="color:rgb(51, 51, 51);">：</font>**<font style="color:rgb(51, 51, 51);">填写文件的分隔符，输入为字符串，默认为</font><font style="color:rgb(221, 17, 68);background-color:rgb(246, 246, 246);">','</font><font style="color:rgb(51, 51, 51);">。</font>

_<font style="color:rgb(102, 102, 102);">注： CSV文件是以纯文本形式存储的表格数据，由任意数目的记录组成，记录间以某种换行符分隔开，最常见的就是逗号或制表符。</font>_**<font style="color:rgb(51, 51, 51);">  
</font>**

**<font style="color:rgb(51, 51, 51);">delimiter：</font>**<font style="color:rgb(51, 51, 51);">备选分隔符,输入字符串，默认为None，如果指定该参数，则sep参数失效。</font>

<font style="color:rgb(51, 51, 51);"></font>

**<font style="color:rgb(51, 51, 51);">delim_whitespace：</font>**<font style="color:rgb(51, 51, 51);">指定空格是否作为分隔符使用，等效于设定sep=’\s+’；默认为False，即不设置空格为分隔符，如果这个参数设定为Ture，那么“delimiter ”参数失效。</font>

<font style="color:rgb(51, 51, 51);"></font>

**<font style="color:rgb(51, 51, 51);">header：</font>**<font style="color:rgb(51, 51, 51);">指定行作为表头，默认为</font><font style="color:rgb(221, 17, 68);background-color:rgb(246, 246, 246);">'infer'</font><font style="color:rgb(51, 51, 51);">，csv表格第一行作为表头；没有表头则可设置为None，也可输入整型数字或整型数字组成的列表。</font>

<font style="color:rgb(51, 51, 51);"> 1.默认为</font><font style="color:rgb(221, 17, 68);background-color:rgb(246, 246, 246);">'infer'</font><font style="color:rgb(51, 51, 51);">，设置数据第一行为表头:</font>

<font style="color:rgb(51, 51, 51);"> 2.输入整型数字，对应表格内行的下标（从0开始），设置指定行为表头，指定行之前的数据不读取：</font>

![](https://cdn.nlark.com/yuque/0/2023/jpeg/1675452/1693366186209-cfc6ea05-1d85-4bd4-a84c-144588992ce9.jpeg)



<font style="color:rgb(51, 51, 51);"> 3.输入整型数字的列表，指定列表内元素对应的行为表头，也就是说每一列有多个列名，且介于表头行中间的行数据被忽略不读取：</font>

![](https://cdn.nlark.com/yuque/0/2023/jpeg/1675452/1693366201395-4e4c6fb4-e471-43de-bea9-f7c10048cd58.jpeg)



**<font style="color:rgb(51, 51, 51);">names：</font>**<font style="color:rgb(51, 51, 51);">用以设置结果表格的列名，默认为None，不设置列名；传入类似数组的有序集合，如列表、字符串以及元组等，从最后列开始，数据内的元素倒序依次作为对应列的列名。</font>

![](https://cdn.nlark.com/yuque/0/2023/jpeg/1675452/1693381993882-18f96077-5b39-4872-816d-4c71b32b29f9.jpeg)

_<font style="color:rgb(102, 102, 102);">注：该数据内的元素默认出现重复时，即不同列设置同样的列名时，因为“mangle_dupe_cols”参数默认为True，会自动修改重复的列名（添加后缀信息），并附加一条提示信息。</font>_



**<font style="color:rgb(51, 51, 51);">index_col：</font>**<font style="color:rgb(51, 51, 51);">指定列为行索引，默认为None，即不设置行索引；</font>

<font style="color:rgb(51, 51, 51);"> 1.输入列的整型数字下标或列名的字符串，指定该列为索引列：</font>

![](https://cdn.nlark.com/yuque/0/2023/jpeg/1675452/1693382034075-0450132f-a638-4af8-8eeb-66c0cd2c7938.jpeg)



<font style="color:rgb(51, 51, 51);"> 2.输入列名或列下标为元素组成的序列（如列表、元组等），指定序列元素所对应的列作行索引，这样每行便有多个索引。  
</font><font style="color:rgb(51, 51, 51);">例如，输入</font><font style="color:rgb(221, 17, 68);background-color:rgb(246, 246, 246);">['问题ID', 0]</font><font style="color:rgb(51, 51, 51);">，设置第一列和“类型”列为索引：</font>

![](https://cdn.nlark.com/yuque/0/2023/jpeg/1675452/1693382050700-cd4c091e-dbc9-4449-8670-141aeeebb1b3.jpeg)



**<font style="color:rgb(51, 51, 51);">usecols：</font>**<font style="color:rgb(51, 51, 51);">设置获取表格的指定列，返回指定列组成的DataFrame数据集。</font>

 1.<font style="color:rgb(51, 51, 51);">默认为None，获取所有列，即整个表格：</font>

<font style="color:rgb(51, 51, 51);"> 2.输入列名或列下标为元素组成的可迭代序列（如列表、元组等），获取序列元素对应表格中的列：</font>

![](https://cdn.nlark.com/yuque/0/2023/jpeg/1675452/1693382100517-135a4b5f-3fc2-43f7-922e-d886dc332c88.jpeg)

_<font style="color:rgb(102, 102, 102);">注：序列内的元素需统一，或均为列名，或均为列下标。</font>_

<font style="color:rgb(51, 51, 51);"></font>

**<font style="color:rgb(51, 51, 51);">squeeze：</font>**<font style="color:rgb(51, 51, 51);">如果文件只包含一列，则返回一个Series类型的数据。</font>

<font style="color:rgb(51, 51, 51);">  1.默认为False，文件只包含一列的情况下返回值依旧为Dataframe类型数据；</font>

<font style="color:rgb(51, 51, 51);">  2.设置为True，返回一个Series类型的数据。</font>



**<font style="color:rgb(51, 51, 51);">prefix：</font>**<font style="color:rgb(51, 51, 51);">在没有列名（header=None）时，给列下标组成的列名添加前缀。</font>

 1.<font style="color:rgb(51, 51, 51);">默认为None，不添加前缀</font>

<font style="color:rgb(51, 51, 51);"> 2.输入字符串，在列下标前添加前缀作为列名：</font>

![](https://cdn.nlark.com/yuque/0/2023/jpeg/1675452/1693382130638-6b7f26f7-df83-408b-89ce-75d95b14ccb4.jpeg)



**<font style="color:rgb(51, 51, 51);">mangle_dupe_cols：</font>**<font style="color:rgb(51, 51, 51);">出现重复的列名时，自动给重复的列名添加后缀，将相同的列名【…X…X…】修改为【…X…X.n…】，默认为True，且不支持False：</font>

_<font style="color:rgb(102, 102, 102);">注：设置为False，会抛出异常。</font>_

_<font style="color:rgb(102, 102, 102);"></font>_

**<font style="color:rgb(51, 51, 51);">dtype：</font>**<font style="color:rgb(51, 51, 51);">设置列的数据类型；输入列名为key，数据类型为value的字典，如</font><font style="color:rgb(221, 17, 68);background-color:rgb(246, 246, 246);">{'问题ID':float}</font><font style="color:rgb(51, 51, 51);">，设置“时长”列为浮点数类型：</font>

![](https://cdn.nlark.com/yuque/0/2023/jpeg/1675452/1693382611653-6c75d78f-2556-476a-9bb9-baf2db5a9be8.jpeg)



**<font style="color:rgb(51, 51, 51);">engine：</font>**<font style="color:rgb(51, 51, 51);">设置使用的分析引擎语言,默认为</font><font style="color:rgb(221, 17, 68);background-color:rgb(246, 246, 246);">'python'</font><font style="color:rgb(51, 51, 51);">,也可以使用</font><font style="color:rgb(221, 17, 68);background-color:rgb(246, 246, 246);">'C'</font><font style="color:rgb(51, 51, 51);">，C引擎快但是Python引擎功能更加完备。</font>

_<font style="color:rgb(102, 102, 102);"></font>_

**<font style="color:rgb(51, 51, 51);">converters：</font>**<font style="color:rgb(51, 51, 51);">可以在读取的时候对列数据进行变换；</font>_<font style="color:rgb(102, 102, 102);">  
</font>_<font style="color:rgb(51, 51, 51);">例如</font><font style="color:rgb(221, 17, 68);background-color:rgb(246, 246, 246);">{"问题ID": lambda x: int(x) + 100}</font><font style="color:rgb(51, 51, 51);">是对“风险”列的数值加100的操作：</font>

![](https://cdn.nlark.com/yuque/0/2023/jpeg/1675452/1693382597456-851bca04-f74c-488f-9847-4bf4aec018ab.jpeg)

_<font style="color:rgb(102, 102, 102);">自然也是可以对列进行修改数据类型之类的操作。</font>_

_<font style="color:rgb(102, 102, 102);"></font>_

**<font style="color:rgb(51, 51, 51);">skipinitialspace：</font>**<font style="color:rgb(51, 51, 51);">设置是否忽略分隔符后的空格，默认为False，不忽略，True即忽略。</font>

_<font style="color:rgb(102, 102, 102);"></font>_

**<font style="color:rgb(51, 51, 51);">skiprows：</font>**<font style="color:rgb(51, 51, 51);">设置需要跳过忽略的行数。</font>

_<font style="color:rgb(102, 102, 102);"> 1.</font>_<font style="color:rgb(51, 51, 51);">默认为None，不跳过任何行。</font>

_<font style="color:rgb(102, 102, 102);"> 2.</font>_<font style="color:rgb(51, 51, 51);">若输入为整型数字，便跳过多少行（从文件起始行开始）；</font>

![](https://cdn.nlark.com/yuque/0/2023/jpeg/1675452/1693382663028-e1c1450e-f277-4c6b-9a6e-fbf2c09a0831.jpeg)



<font style="color:rgb(51, 51, 51);"> 3.或输入需要跳过的行数号（文件第一行从0开始）组成的有序序列，如列表、元组：</font>

_<font style="color:rgb(102, 102, 102);"></font>_

**<font style="color:rgb(51, 51, 51);">skipfooter：</font>**<font style="color:rgb(51, 51, 51);">从文件尾部开始跳过忽略。</font>

<font style="color:rgb(51, 51, 51);">默认为0，忽略 0 行；输入整型数字，忽略该整数行数据：</font>

_<font style="color:rgb(102, 102, 102);">c引擎不支持。</font>_

<font style="color:rgb(51, 51, 51);"></font>

**<font style="color:rgb(51, 51, 51);">nrows：</font>**<font style="color:rgb(51, 51, 51);">设置读取数据的行数（不包括表头）。</font>

<font style="color:rgb(51, 51, 51);"> 1.默认为None，读取所有行；</font>

<font style="color:rgb(51, 51, 51);"> 2.或输入整型数字，读取该整数行数据：</font>

![](https://cdn.nlark.com/yuque/0/2023/jpeg/1675452/1693382695585-137292ab-6f4f-4c73-ba52-43fe57e2fa3f.jpeg)

<font style="color:rgb(51, 51, 51);"></font>

**<font style="color:rgb(51, 51, 51);">na_values：</font>**<font style="color:rgb(51, 51, 51);">替换表格中指定数据为空值（NA/NaN）。</font>

<font style="color:rgb(51, 51, 51);"> 1.默认为None，不替换；</font>

<font style="color:rgb(51, 51, 51);"> 2.输入字符串，将值与之相同的数据替换为NA/NaN：</font>

![](https://cdn.nlark.com/yuque/0/2023/jpeg/1675452/1693382733816-d96bd120-73ed-4f7a-be7b-05926c362bc6.jpeg)

<font style="color:rgb(51, 51, 51);"> 3.传入列表元组等序列，将序列内的元素对应的数据都替换：</font>

<font style="color:rgb(51, 51, 51);"> 4.输入字典，指定某个列里面的指定数据替换为NA/NaN；  
</font><font style="color:rgb(51, 51, 51);">例如，</font><font style="color:rgb(221, 17, 68);background-color:rgb(246, 246, 246);">{'问题ID':5}</font><font style="color:rgb(51, 51, 51);">只修改“问题ID”列值为5的数据为NaN：</font>

<font style="color:rgb(51, 51, 51);"></font>

**<font style="color:rgb(51, 51, 51);">keep_default_na：</font>**<font style="color:rgb(51, 51, 51);">设置对于表格中空值进行解析的方式，根据传入“na_values ”参数的不同，行为如下：</font>

<font style="color:rgb(51, 51, 51);"> 1.“na_values ”参数未设置，“keep_default_na ”参数默认为True，表格中空值解析为NaN：</font>

<font style="color:rgb(51, 51, 51);"> 2.“na_values ”参数未设置，“keep_default_na ”参数设置为False，表格中空值同样为空：</font>

<font style="color:rgb(51, 51, 51);"> 3.“na_values ”参数设置，“keep_default_na ”参数默认为True，空值均解析为NaN：</font>

<font style="color:rgb(51, 51, 51);"> 4.“na_values ”参数设置，“keep_default_na ”参数设置为False，被替代的空值解析为NaN，原本空值依旧为空：</font>

<font style="color:rgb(51, 51, 51);"> </font>_<font style="color:rgb(102, 102, 102);">注：如果将“na_filter”参数设置为False ，则将忽略“keep_default_na”和 “na_values”参数。</font>_



**<font style="color:rgb(51, 51, 51);">na_filter ：</font>**<font style="color:rgb(51, 51, 51);">是否检查丢失值（空字符串或者空值）。对于大文件来说数据集中没有空值，设定na_filter=False可以提升读取速度。</font>



**<font style="color:rgb(51, 51, 51);">encoding：</font>**<font style="color:rgb(51, 51, 51);">填写文件编码格式，输入为字符串，例如</font><font style="color:rgb(221, 17, 68);background-color:rgb(246, 246, 246);">'utf-8'</font><font style="color:rgb(51, 51, 51);">、</font><font style="color:rgb(221, 17, 68);background-color:rgb(246, 246, 246);">'ANSI'</font><font style="color:rgb(51, 51, 51);">,  </font><font style="color:rgb(221, 17, 68);background-color:rgb(246, 246, 246);">'GBK'</font><font style="color:rgb(51, 51, 51);">、</font><font style="color:rgb(221, 17, 68);background-color:rgb(246, 246, 246);">'GB2312'</font><font style="color:rgb(51, 51, 51);">, </font><font style="color:rgb(221, 17, 68);background-color:rgb(246, 246, 246);">'latin1'</font><font style="color:rgb(51, 51, 51);">、等。</font>



**<font style="color:rgb(51, 51, 51);">还有很多不太常用的参数，可以查找资料参考pandas库的read_excel方法去进行相关设置。</font>**



### <font style="color:rgb(51, 51, 51);">输出</font>
**<font style="color:rgb(51, 51, 51);">返回值：</font>**<font style="color:rgb(51, 51, 51);">返回读取到的CSV文件内容，其数据类型为Dataframe的数据集。</font>













