# 一.功能描述
<font style="color:rgb(51, 51, 51);">阿普斯usbhub 设备串口指令调用操作。</font>

![](https://cdn.nlark.com/yuque/0/2024/png/1675452/1714031098833-0cfc689a-9093-487a-bf59-1d2e88574c10.png)



# 二.**<font style="color:rgb(51, 51, 51);">基本使用说明</font>**
<font style="color:rgb(51, 51, 51);">1.输入连接串口，输入波特率，操作类型，操作端口号即可通过usbhub连接至指定usb进行操作：</font>

![](https://cdn.nlark.com/yuque/0/2024/png/1675452/1714031098833-0cfc689a-9093-487a-bf59-1d2e88574c10.png)





# 三.<font style="color:rgb(51, 51, 51);">配置项说明</font>
### 输入
**<font style="color:rgb(51, 51, 51);">连接串口</font>****<font style="color:rgb(51, 51, 51);">：</font>**<font style="color:rgb(51, 51, 51);">传入需要连接的串口号，输入为字符串；默认值："COM3"。</font>



**<font style="color:rgb(51, 51, 51);">波特率</font>****<font style="color:rgb(51, 51, 51);">：</font>**<font style="color:rgb(51, 51, 51);">传入指定的波特率，默认值：115200。</font>



**<font style="color:rgb(51, 51, 51);">超时时间</font>****<font style="color:rgb(51, 51, 51);">：</font>**<font style="color:rgb(51, 51, 51);">设置超时时间，默认值：None。</font>



**<font style="color:rgb(51, 51, 51);">操作类型：</font>**<font style="color:rgb(51, 51, 51);">设置所需要执行的操作方式，一共三种方式：关闭，打开，查询</font>

<font style="color:rgb(51, 51, 51);">关闭：执行关闭指定端口的操作。</font>

<font style="color:rgb(51, 51, 51);">打开：执行打开指定端口的操作。</font>

<font style="color:rgb(51, 51, 51);">查询：执行查询指定端口的操作。</font>



**<font style="color:rgb(51, 51, 51);">端口号：</font>**<font style="color:rgb(51, 51, 51);">需要触发的端口号，例如"00"：表示全选端口； "01"：表示选择01端口</font>![](https://cdn.nlark.com/yuque/0/2024/png/1675452/1714032032773-bce52f7d-979f-4dcd-a778-7e21eb8facbb.png)





### <font style="color:rgb(51, 51, 51);">输出</font>
**<font style="color:rgb(51, 51, 51);">返回值：</font>**<font style="color:rgb(51, 51, 51);">usbhub设备操作返回值</font>

