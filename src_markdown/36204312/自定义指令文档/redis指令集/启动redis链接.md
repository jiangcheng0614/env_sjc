# 一.功能描述
通过python的第三方redis库建立redis连接，并返回一个redis连接实例。（<font style="color:#DF2A3F;">注意：该指令必须与“关闭redis连接”指令配合使用</font>）

![](https://cdn.nlark.com/yuque/0/2023/png/25504773/1679283401781-e7094c5f-c0d0-414c-ae03-ee9c0022219a.png)

# 二.使用参数说明
### 输入：
host：连接地址，默认为'127.0.0.1'，格式为字符串

port：端口号，默认为'6379'，格式为字符串  
password:  redis密码，默认为空字符，格式为字符串

db:  redis数据库索引，默认为0，格式为整数

### 输出：
connection_pool：redis连接实例，在后续的指令中传参使用



# 三.结果样例展示及使用说明
**启动redis连接**指令必须与**关闭redis连接**指令成对使用，在**启动redis连接**与**关闭redis连接**指令中间进行你需要的redis增删改查操作

![](https://cdn.nlark.com/yuque/0/2023/png/25504773/1679292144448-7d93d534-7562-4b97-a995-86644af624f3.png)



