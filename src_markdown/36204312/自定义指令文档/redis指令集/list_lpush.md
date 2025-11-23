# 一.功能描述
传入一个redis连接实例，实现对该实例下的redis为key列表一个或多个值插入到列表头部操作。（<font style="color:#DF2A3F;">注意：key的命名方式建议大家遵从python的</font>**<font style="color:#DF2A3F;">标识符</font>**<font style="color:#DF2A3F;">命名规则</font>）

![](https://cdn.nlark.com/yuque/0/2023/png/25504773/1679473104133-23e998e0-1cd1-4447-9a32-e6fefcd1695c.png)

# 二.使用参数说明
### 输入：
connection_pool：redis连接实例，是**启动redis连接**指令的返回值

key：用于查找该列表的索引名称，建议使用python的标识符命名规则，格式为字符串  
value_list:  将要依次在列表尾部添加元素值的列表，格式为列表



# 三.结果样例展示及使用说明
![](https://cdn.nlark.com/yuque/0/2023/png/25504773/1679473245714-3fb24661-e134-4e34-ba90-4a5a14eea76c.png)

![](https://cdn.nlark.com/yuque/0/2023/png/25504773/1679473235525-89ec9d9e-098e-40c9-b6f5-e3919323871c.png)



