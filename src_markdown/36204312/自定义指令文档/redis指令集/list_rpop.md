# 一.功能描述
传入一个redis连接实例，实现对该实例下的redis为key列表的尾部进行一个值的移除操作操作。（<font style="color:#DF2A3F;">注意：key的命名方式建议大家遵从python的</font>**<font style="color:#DF2A3F;">标识符</font>**<font style="color:#DF2A3F;">命名规则</font>）

![](https://cdn.nlark.com/yuque/0/2023/png/25504773/1679473472419-10679499-09ff-465c-9ac3-cbda873c31bd.png)

# 二.使用参数说明
### 输入：
connection_pool：redis连接实例，是**启动redis连接**指令的返回值

key：列表的索引名称，格式为字符串

### 输出：
value:  在列表key的尾部移除的一个元素值，格式为字符串



# 三.结果样例展示及使用说明
![](https://cdn.nlark.com/yuque/0/2023/png/25504773/1679473962833-56699333-6a01-4593-904d-e5a822979c9a.png)

![](https://cdn.nlark.com/yuque/0/2023/png/25504773/1679473953266-6b47c9bf-2068-40a3-b340-ecc9885d4660.png)



