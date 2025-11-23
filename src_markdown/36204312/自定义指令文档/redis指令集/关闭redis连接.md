# 一.功能描述
传入一个redis连接实例，通过python的第三方redis库实现关闭redis连接（<font style="color:#DF2A3F;">注意：该指令必须与“启动redis连接”指令配合使用</font>）

![](https://cdn.nlark.com/yuque/0/2023/png/25504773/1679454055051-b0efd957-80cd-40c1-a11d-c9a8196e5812.png)

# 二.使用参数说明
### 输入：
connection_pool：redis连接实例，是**启动redis连接**指令传出的结果

# 三.结果样例展示及使用说明
**关闭redis连接**指令必须与**启动redis连接**指令成对使用，在**启动redis连接**与**关闭redis连接**指令中间进行你需要的redis增删改查操作

![](https://cdn.nlark.com/yuque/0/2023/png/25504773/1679292144448-7d93d534-7562-4b97-a995-86644af624f3.png)



