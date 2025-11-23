# 一.功能描述
传入一个redis连接实例，实现对该实例下的redis为key列表的尾部进行一个或多个值的添加操作。（<font style="color:#DF2A3F;">注意：key的命名方式建议大家遵从python的</font>**<font style="color:#DF2A3F;">标识符</font>**<font style="color:#DF2A3F;">命名规则</font>）

![](https://cdn.nlark.com/yuque/0/2023/png/25504773/1679471763330-081b9576-746d-4ef5-9fbe-586af5a842c3.png)

# 二.使用参数说明
### 输入：
connection_pool：redis连接实例，是**启动redis连接**指令的返回值

key：用于查找该列表的索引名称，建议使用python的标识符命名规则，格式为字符串  
value_list:  将要依次在列表尾部添加元素值的列表，格式为列表



# 三.结果样例展示及使用说明
![](https://cdn.nlark.com/yuque/0/2023/png/25504773/1679472459490-d322f89f-5f10-485c-95d6-60ef983ec181.png)

![](https://cdn.nlark.com/yuque/0/2023/png/25504773/1679472541633-db266a38-9fef-417d-9f37-c8c69689574e.png)



