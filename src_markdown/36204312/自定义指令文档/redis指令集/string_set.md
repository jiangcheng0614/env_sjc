# 一.功能描述
传入一个redis连接实例，实现对该实例下的redis进行字符串格式的数据保存。（<font style="color:#DF2A3F;">注意：将value字符串保存到redis的key中，key的命名方式建议大家遵从python的</font>**<font style="color:#DF2A3F;">标识符</font>**<font style="color:#DF2A3F;">命名规则</font>）

![](https://cdn.nlark.com/yuque/0/2023/png/25504773/1679455082794-55711c27-9aba-4175-a874-80627488c0fd.png)

# 二.使用参数说明
### 输入：
connection_pool：redis连接实例，是**启动redis连接**指令的返回值

key：用于查找value值的索引名称，建议使用python的标识符命名规则，格式为字符串  
value:  存储在key下的值，各种类型均可，该指令会对value进行一次json封装后再set到redis中



# 三.结果样例展示及使用说明
![](https://cdn.nlark.com/yuque/0/2023/png/25504773/1679456728581-2cfbc190-bdd3-4ec8-8d32-f1388a529b9e.png)

![](https://cdn.nlark.com/yuque/0/2023/png/25504773/1679456754501-dbaebe2f-e975-4fc9-bd0f-5145a19d37b2.png)

![](https://cdn.nlark.com/yuque/0/2023/png/25504773/1679456772591-0675106c-76a3-452d-b73e-eee0a577a5f5.png)



