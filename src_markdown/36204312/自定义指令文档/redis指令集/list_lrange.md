# 一.功能描述
获取列表中指定范围内的元素（<font style="color:#DF2A3F;">注意：key的命名方式建议大家遵从python的</font>**<font style="color:#DF2A3F;">标识符</font>**<font style="color:#DF2A3F;">命名规则</font>）

![](https://cdn.nlark.com/yuque/0/2023/png/25504773/1679540313698-1f0a47f7-3c63-487f-97a7-06e65d00b53b.png)

# 二.使用参数说明
### 输入：
connection_pool：redis连接实例，是**启动redis连接**指令的返回值

key：列表的索引名称，格式为字符串  
start：需要获取范围的开始下标，格式为整数  
end：需要获取范围的结束下标，格式为整数

### 输出：
value_list:  获取到的列表指定范围内元素值列表，格式为列表



# 三.结果样例展示及使用说明
![](https://cdn.nlark.com/yuque/0/2023/png/25504773/1679539584805-96779c96-b9c4-4b38-9578-49b070ec433c.png)

![](https://cdn.nlark.com/yuque/0/2023/png/25504773/1679539566174-8b4a3459-907c-4b1b-b71c-689233243534.png)



