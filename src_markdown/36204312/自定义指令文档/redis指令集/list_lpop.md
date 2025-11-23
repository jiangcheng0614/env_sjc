# 一.功能描述
传入一个redis连接实例，实现对该实例下的redis为key列表的头部进行一个值的移除操作操作。（<font style="color:#DF2A3F;">注意：key的命名方式建议大家遵从python的</font>**<font style="color:#DF2A3F;">标识符</font>**<font style="color:#DF2A3F;">命名规则</font>）

![](https://cdn.nlark.com/yuque/0/2023/png/25504773/1679538582040-04eae545-4873-4777-8905-7d46e6fbc371.png)

# 二.使用参数说明
### 输入：
connection_pool：redis连接实例，是**启动redis连接**指令的返回值

key：列表的索引名称，格式为字符串

### 输出：
value:  在列表key的头部移除的一个元素值，格式为字符串



# 三.结果样例展示及使用说明
![](https://cdn.nlark.com/yuque/0/2023/png/25504773/1679538777023-3f26ba51-a29e-4da3-8861-cadf0f1ad9e0.png)

![](https://cdn.nlark.com/yuque/0/2023/png/25504773/1679538510208-58085c8f-55ea-4181-b4b0-d29eabe3046f.png)



