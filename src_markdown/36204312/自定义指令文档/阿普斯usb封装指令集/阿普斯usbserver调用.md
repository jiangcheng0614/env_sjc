# 一.功能描述
<font style="color:rgb(51, 51, 51);">阿普斯usbserver 设备端口指令调用操作。</font>

![](https://cdn.nlark.com/yuque/0/2024/png/1675452/1714048267267-4d92c5ed-8d9c-4e73-8847-57311a90852b.png)



# 二.**<font style="color:rgb(51, 51, 51);">基本使用说明</font>**
<font style="color:rgb(51, 51, 51);">1.输入ip，port，操作类型，num即可通过usbserver连接至指定usb口进行操作：</font>

![](https://cdn.nlark.com/yuque/0/2024/png/1675452/1714048275186-cf9ef080-810f-4292-b05d-4f9ed58c1a8a.png)





# 三.<font style="color:rgb(51, 51, 51);">配置项说明</font>
### 输入
**<font style="color:rgb(51, 51, 51);">ip</font>****<font style="color:rgb(51, 51, 51);">：</font>**<font style="color:rgb(51, 51, 51);">传入执行连接的useserver设备ip，类型：str类型。</font>



**<font style="color:rgb(51, 51, 51);">port</font>****<font style="color:rgb(51, 51, 51);">：</font>**<font style="color:rgb(51, 51, 51);">传入执行连接的usbserver设备port，类型：str类型。</font>



**<font style="color:rgb(51, 51, 51);">操作类型：</font>**<font style="color:rgb(51, 51, 51);">设置所需要执行的操作方式，一共三种方式：关闭，打开，查询</font>

<font style="color:rgb(51, 51, 51);">关闭：执行usvserver设备关闭指定端口的操作。</font>

<font style="color:rgb(51, 51, 51);">打开：执行usvserver设备打开指定端口的操作。</font>

<font style="color:rgb(51, 51, 51);">通电：执行usbserver设备指定端口的通电操作。</font>

<font style="color:rgb(51, 51, 51);">断电：执行usbserver设备指定端口的断电操作。</font>

<font style="color:rgb(51, 51, 51);">查询：执行usbserver设备查询指定端口的状态操作。</font>



**<font style="color:rgb(51, 51, 51);">num：</font>**<font style="color:rgb(51, 51, 51);">需要触发的num口号，类型：int类型    </font>

<font style="color:rgb(51, 51, 51);">           例如0：表示全选usb口； 1：表示选择1号usb</font>

![](https://cdn.nlark.com/yuque/0/2024/png/1675452/1714057081306-6c978b29-f118-443c-8c9b-0e6fd4bedeb7.png)



### <font style="color:rgb(51, 51, 51);">输出</font>
**<font style="color:rgb(51, 51, 51);">返回值：</font>**<font style="color:rgb(51, 51, 51);">usbserver设备操作结果</font>

