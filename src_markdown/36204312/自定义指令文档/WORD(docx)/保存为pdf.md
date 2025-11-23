**描述**  
将docx文件保存为一个pdf文件

![](https://cdn.nlark.com/yuque/0/2024/png/40912025/1721628732351-db08ecbc-e1a4-4d8d-bd87-7d1ccc6b88aa.png)

  
**参数配置**  
**指令输入**  
**常规**  
**word对象: **返回一个word文件对象  
pdf文件路径：将word对象保存为pdf文件的路径  
  
**流程配置**

![](https://cdn.nlark.com/yuque/0/2024/png/40912025/1721628758463-84fd356f-2cbf-4263-8882-664594e1e0c7.png)

  
  
**运行结果**

docx:  
![](https://cdn.nlark.com/yuque/0/2024/png/40912025/1721628808054-a3b99607-088e-472d-8fd2-6934d4ab21d3.png)

pdf:

![](https://cdn.nlark.com/yuque/0/2024/png/40912025/1721628778877-b1885a5d-15ba-4808-a882-52a8395aee5b.png)

**使用前提：**

需先下载 wkhtmltopdf。方式1：

```plain
sudo apt-get install wkhtmltopdf
```

方式2：先手动安装下载包后再解压的方式

可以自行前往[https://github.com/wkhtmltopdf/packaging/releases/0.12.6-1](https://github.com/wkhtmltopdf/packaging/releases/0.12.6-1)选择需要下载的文件本地。

随后进入该文件目录使用命令sudo dpkg -i xxxx.deb的方式即可解压完成







若有收获，就点个赞吧

  
 

