# 一.功能描述
传入一个redis连接实例，获取redis中指定key存储的值。

![](https://cdn.nlark.com/yuque/0/2023/png/25504773/1679464584143-c7e2412f-1c69-475a-b8d4-68e7e7ac0836.png)

# 二.使用参数说明
### 输入：
connection_pool：redis连接实例，是**启动redis连接**指令的返回值

key：用于查找value值的索引名称，建议使用python的标识符命名规则，格式为字符串

### 输出： 
value:  存储在key下的值，该指令会对获取到的value进行一次json解压后再返回

# 三.结果样例展示及使用说明
![](https://cdn.nlark.com/yuque/0/2023/png/25504773/1679456728581-2cfbc190-bdd3-4ec8-8d32-f1388a529b9e.png)

![](https://cdn.nlark.com/yuque/0/2023/png/25504773/1679456754501-dbaebe2f-e975-4fc9-bd0f-5145a19d37b2.png)

![](https://cdn.nlark.com/yuque/0/2023/png/25504773/1679456772591-0675106c-76a3-452d-b73e-eee0a577a5f5.png)



