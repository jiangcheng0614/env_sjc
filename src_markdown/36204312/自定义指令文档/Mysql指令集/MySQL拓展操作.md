## 使用场景:
1. 客户要求数据入库，且业务中涉及事务回滚，可以通过该指令快速实现

## 指令使用指南:
2. 初始化数据库连接，在一个应用中只需初始化一次数据库
3. 在业务开始前获取一个事务管理器对象，并在业务中使用该事务管理器对象
4. 期间可以任意使用增删改指令
5. 若在业务中遇到异常，可使用手动回滚进行全事务回滚
6. 若在增删改中遇到异常，指令默认在事务管理对象销毁时回滚所有操作
7. 业务正常结束后可正常提交事务结束

## 参数配置
![](https://cdn.nlark.com/yuque/0/2023/png/34646410/1700637916148-1a558c7d-48bd-4cbb-8c70-3fda7cae7f35.png)

+ 数据库地址： 填入数据库连接地址，如IP形式 **127.0.0.1 **或域名形式 **mysql.yd**
+ 账号：该项为Mysql用于登录的用户名
+ 密码：该项为Mysql用于登录的密码
+ 数据库名：填入需要操作的数据库名称

![](https://cdn.nlark.com/yuque/0/2025/png/51054638/1740472606730-582d2283-49d3-46b2-87cb-5be48189e57d.png)



+ 最大连接数：数据库池的最大连接数
+ 端口：数据连接端口
+ 是否开启事务：勾选后初始化生成一个事务对象，用于数据库事务管理
+ 是否开启日志：勾选后开启日志
+ 超时时间：默认20s 超时自动断开

## 指令集
1. [单条数据插入(insert)](https://ydrpa.yuque.com/org-wiki-ydrpa-xtutvv/ga4dm6/ypage0du9iz5hf6g)
2. [批量插入数据(batch_insert)](about:blank)
3. [单条更新插入(upsert)](about:blank)
4. [批量更新插入(batch_upsert)](about:blank)
5. [删除数据(delete)](about:blank)
6. [查询(select)](about:blank)
7. [更新(update)](about:blank)
8. [提交(commit)](about:blank)
9. [回滚(rollback)](about:blank)

