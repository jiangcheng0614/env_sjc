# 一.功能描述
<font style="color:rgb(51, 51, 51);">用以在csv文件末追加数据。</font>

_<font style="color:rgb(102, 102, 102);">指令执行过程中CSV文件处于关闭状态。</font>_

![](https://cdn.nlark.com/yuque/0/2023/jpeg/1675452/1676876183702-aea9b884-6d47-4f6d-89fc-e6a23f67e0b7.jpeg)



# 二.<font style="color:rgb(51, 51, 51);">配置项说明</font>
### 输入
**<font style="color:rgb(51, 51, 51);">目标文件路径：</font>**

<font style="color:rgb(51, 51, 51);">指定传入待追加数据的目标CSV文件的绝对路径，str类型，可点击参数后的文件图标进行选择文件。</font>

**<font style="color:rgb(51, 51, 51);">分隔符：</font>**

<font style="color:rgb(51, 51, 51);">设置CSV文件的分隔符，str类型，默认为逗号 ','。</font>

**编码：**

<font style="color:rgb(51, 51, 51);">设</font><font style="color:rgb(51, 51, 51);">置文件的编码格式，str类型，默认为'ANSI'。</font>

**行数据list：**

<font style="color:rgb(51, 51, 51);">输入追加的数据，其类型为列表list；注意列表的长度必须与CSV文件的列数一致，默认为空二维list。</font>

### <font style="color:rgb(51, 51, 51);">输出</font>
返回None**<font style="color:rgb(51, 51, 51);">：</font>**

返回状态判断，成功执行返回None，结果如下图

注：_<font style="color:rgb(102, 102, 102);">指令执行过程中CSV文件需处于关闭状态。</font>_

![](https://cdn.nlark.com/yuque/0/2023/png/1675452/1676876137966-27daa673-1ede-4bbd-bbec-896b0417752c.png)



![](https://cdn.nlark.com/yuque/0/2023/png/1675452/1676876094145-c85dc3d0-4acf-4a68-b551-1f8a1e01530e.png)

