## 描述
通过<font style="background-color:#D8DAD9;">数据库连接对象</font>，输入<font style="background-color:#D8DAD9;">sql语句</font>来实现执行sql语句的功能

![](https://cdn.nlark.com/yuque/0/2024/png/40912025/1713148586612-081fe2a0-ba02-4f86-9213-1636d6b5dbdc.png)

## 参数配置
### 指令输入
#### 常规
**数据库连接对象: **_文本框 _; 与Hana数据库的连接对象

**sql语句: **_文本框_; 输入要执行的sql语句，如(select * from <表名>)

### 指令输出
**result**:列表;指令的执行结果，如果是select语句则返回列表信息;若不是则返回空列表

## 参考案例
### 场景1
查询数据库中所有的数据信息

**参考流程**

![](https://cdn.nlark.com/yuque/0/2024/png/40912025/1713148823292-87e0cb88-1102-4dca-8ac1-d0d2489e907b.png)

**关键指令配置**

![](https://cdn.nlark.com/yuque/0/2024/png/40912025/1713148875064-3927fa4e-7c89-444d-a033-9365bd22cdcd.png)

**运行结果**

![](https://cdn.nlark.com/yuque/0/2024/png/40912025/1713148940007-bf28d81b-0673-4c49-a80c-9cf2c4d60de3.png)



### 场景2
删除列表中所有的信息

**参考流程**

![](https://cdn.nlark.com/yuque/0/2024/png/40912025/1713149001986-79ea6890-614a-40c4-b832-611e4866cdeb.png)

**关键指令配置**

![](https://cdn.nlark.com/yuque/0/2024/png/40912025/1713145977422-7dd73101-f0af-4526-93a8-ac3594c50603.png)

**运行结果**

![](https://cdn.nlark.com/yuque/0/2024/png/40912025/1713146003321-ff9a2613-2ea2-4799-bf6d-f25bd89087ff.png)

## 常见问题
暂无

