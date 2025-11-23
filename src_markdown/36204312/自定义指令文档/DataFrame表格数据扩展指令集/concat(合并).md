# 一.功能描述
<font style="color:rgb(51, 51, 51);">可以沿着一条轴将多个对象堆叠到一起 concat方法相当于数据库中的全连接(UNION ALL),可以指定按某个轴进行连接,也可以指定连接的方式join(outer,inner 只有这两种)。</font>

![](https://cdn.nlark.com/yuque/0/2023/jpeg/1675452/1692878330034-8be239ad-efdd-471b-b646-7e7fd6835990.jpeg)



# 二.**<font style="color:rgb(51, 51, 51);">基本使用说明</font>**
<font style="color:rgb(51, 51, 51);">轴向连接 pd.concat() 就是单纯地把两个表拼在一起，这个过程也被称作连接（concatenation）、绑定（binding）或堆叠（stacking）。因此可以想见，这个函数的关键参数应该是 axis，用于指定连接的轴向。 在默认的 axis=0 情况下，pd.concat([obj1,obj2]) 函数的效果与 obj1.append(obj2) 是相同的； 而在 axis=1 的情况下，pd.concat([df1,df2],axis=1) 的效果与 pd.merge(df1,df2,left_index=True,right_index=True,how=’outer’) 是相同的。 可以理解为 concat 函数使用索引作为“连接键”。</font>

<font style="color:rgb(51, 51, 51);">示例：</font>

<font style="color:rgb(51, 51, 51);">df1：</font>

![](https://cdn.nlark.com/yuque/0/2023/jpeg/1675452/1692878484406-6226d79f-9302-45ad-9adf-6298ece058b1.jpeg)



<font style="color:rgb(51, 51, 51);">df2：</font>

![](https://cdn.nlark.com/yuque/0/2023/jpeg/1675452/1692878499078-b64d4906-7790-4a0b-adc3-9b450524fa67.jpeg)

<font style="color:rgb(51, 51, 51);"></font>

<font style="color:rgb(51, 51, 51);">执行结果：</font>

![](https://cdn.nlark.com/yuque/0/2023/jpeg/1675452/1692878689552-0a7f2b13-cc5e-41cf-8896-dd576abbbe1e.jpeg)



# 三.<font style="color:rgb(51, 51, 51);">配置项说明</font>
### 输入
**<font style="color:rgb(51, 51, 51);">objs</font>****<font style="color:rgb(51, 51, 51);">：</font>**<font style="color:rgb(36, 41, 47);">要合并的DataFrame对象的序列或者字典，必须提供至少一个DataFrame对象。</font>

**<font style="color:rgb(51, 51, 51);">axis</font>****<font style="color:rgb(51, 51, 51);">：</font>**<font style="color:rgb(36, 41, 47);">指定合并的轴，可以是0（按行合并）或1（按列合并）。</font>

<font style="color:rgb(51, 51, 51);">默认值：axis=0</font>

<font style="color:rgb(51, 51, 51);">axis=0：竖方向（index）合并，合并方向index作列表相加，非合并方向columns取并集</font>

![](https://cdn.nlark.com/yuque/0/2023/jpeg/1675452/1692878707985-722a0f4c-9e78-40d4-a0db-e66514b3949f.jpeg)



<font style="color:rgb(51, 51, 51);">axis=1：横方向（columns）合并，合并方向columns作列表相加，非合并方向index取并集</font>

![](https://cdn.nlark.com/yuque/0/2023/jpeg/1675452/1692878723472-89e01062-f775-45e7-984c-96e5e9e81b0e.jpeg)

<font style="color:rgb(221, 17, 68);background-color:rgb(246, 246, 246);">备注：原df中，取并集的行/列名称不能有重复项，即axis=0时columns不能有重复项，axis=1时index不能有重复项。</font>

<font style="color:rgb(221, 17, 68);background-color:rgb(246, 246, 246);"></font>

**<font style="color:rgb(51, 51, 51);">join</font>****<font style="color:rgb(51, 51, 51);">：</font>**<font style="color:rgb(36, 41, 47);">指定合并时的索引方式，可选值为’outer’（并集）、‘inner’（交集）。</font>

<font style="color:rgb(51, 51, 51);">默认值：join=‘outer’</font><font style="color:rgb(36, 41, 47);">  
</font><font style="color:rgb(51, 51, 51);">非合并方向的行/列名称：取交集（inner），取并集（outer）。</font><font style="color:rgb(36, 41, 47);">  
</font><font style="color:rgb(51, 51, 51);">axis=0时join=’inner’，columns取交集：</font>

![](https://cdn.nlark.com/yuque/0/2023/jpeg/1675452/1692878920886-c59eba7a-f454-4d06-9ee6-02f38d1ea6b1.jpeg)

**<font style="color:rgb(51, 51, 51);">  
</font>**

<font style="color:rgb(51, 51, 51);">axis=1时join=’inner’，index取交集：</font>

![](https://cdn.nlark.com/yuque/0/2023/jpeg/1675452/1692878936344-1d070501-8759-4775-8f61-2af053f3d723.jpeg)



**<font style="color:rgb(51, 51, 51);">ignore_index</font>****<font style="color:rgb(51, 51, 51);">：</font>**<font style="color:rgb(36, 41, 47);">是否忽略合并后的索引，可选值为True或False。</font>

<font style="color:rgb(51, 51, 51);">默认值：ignore_index=False</font><font style="color:rgb(36, 41, 47);">  
</font><font style="color:rgb(51, 51, 51);">合并方向是否忽略原行/列名称，而采用系统默认的索引，即从0开始的int。</font><font style="color:rgb(36, 41, 47);">  
</font><font style="color:rgb(51, 51, 51);">axis=0时ignore_index=True，index采用系统默认索引：</font>

![](https://cdn.nlark.com/yuque/0/2023/jpeg/1675452/1692878986849-4106428d-abb0-42fe-a635-8fc82ff912d6.jpeg)



<font style="color:rgb(51, 51, 51);">axis=1时ignore_index=True，columns采用系统默认索引：</font>

![](https://cdn.nlark.com/yuque/0/2023/jpeg/1675452/1692879105288-2d8b908d-0926-4fdf-90e4-7134a8bd6f03.jpeg)



**<font style="color:rgb(51, 51, 51);">keys：</font>**<font style="color:rgb(36, 41, 47);">一个层次化索引对象，用于创建分层索引。</font>

<font style="color:rgb(51, 51, 51);">默认值：keys=None</font><font style="color:rgb(36, 41, 47);">  
</font><font style="color:rgb(51, 51, 51);">可以加一层标签，标识行/列名称属于原来哪个df。</font><font style="color:rgb(36, 41, 47);">  
</font><font style="color:rgb(51, 51, 51);">axis=0时设置keys：</font>

![](https://cdn.nlark.com/yuque/0/2023/jpeg/1675452/1692879124312-b62d3b8b-3ef4-4927-a8b5-ba2493f3570f.jpeg)



<font style="color:rgb(51, 51, 51);">axis=1时设置keys：</font>

![](https://cdn.nlark.com/yuque/0/2023/jpeg/1675452/1692879220582-2db7a5de-8686-43d5-83b2-d85ffaabc6e5.jpeg)

<font style="color:rgb(51, 51, 51);"></font>

**<font style="color:rgb(51, 51, 51);">levels：</font>**<font style="color:rgb(36, 41, 47);">用于创建分层索引的层级标签。</font>

<font style="color:rgb(51, 51, 51);">默认值：levels=None</font>  
<font style="color:rgb(51, 51, 51);">明确行/列名称取值范围：</font>

<font style="color:rgb(51, 51, 51);"></font>

**<font style="color:rgb(51, 51, 51);">names：</font>**<font style="color:rgb(36, 41, 47);">用于创建分层索引的层级名称。</font>

<font style="color:rgb(51, 51, 51);">默认值：names=None</font><font style="color:rgb(36, 41, 47);">  
</font><font style="color:rgb(51, 51, 51);">生成的层次结构索引中级别的名称。</font>

<font style="color:rgb(51, 51, 51);"></font>

**<font style="color:rgb(51, 51, 51);">verify_integrity：</font>**<font style="color:rgb(36, 41, 47);">在合并过程中检查新索引的重复情况。</font><font style="color:rgb(51, 51, 51);">检查新的串联轴是否包含重复项。</font>

<font style="color:rgb(51, 51, 51);">默认值：levels=None  
</font><font style="color:rgb(51, 51, 51);">明确行/列名称取值范围：</font>

<font style="color:rgb(36, 41, 47);"></font>

**<font style="color:rgb(51, 51, 51);">copy：</font>**<font style="color:rgb(36, 41, 47);">是否复制合并的对象数据，默认为True。</font>

<font style="color:rgb(51, 51, 51);">默认值：copy=True  
</font><font style="color:rgb(51, 51, 51);">如果为False，不复制数据。</font>

### <font style="color:rgb(51, 51, 51);">输出</font>
**<font style="color:rgb(51, 51, 51);">返回值：</font>**<font style="color:rgb(51, 51, 51);">返回concat合并后的df</font>













