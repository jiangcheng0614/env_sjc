## 描述
通过<font style="background-color:#D8DAD9;">数据库连接对象</font>，输入<font style="background-color:#D8DAD9;">sql语句</font>来实现执行sql语句的功能

![](https://cdn.nlark.com/yuque/0/2024/png/40912025/1713148586612-081fe2a0-ba02-4f86-9213-1636d6b5dbdc.png)

## 参数配置
### 指令输入
#### 常规
**数据库连接对象: **_文本框 _; 与Hana数据库的连接对象

**sql语句: **_文本框_; 输入要执行的sql语句，如(select * from <表名>)

### 指令输出
**result**:文本框;指令的执行结果

### 场景1
查询数据库中所有的数据信息

**参考流程**

![](https://cdn.nlark.com/yuque/0/2024/png/40912025/1713150334556-66b3a915-ae8a-4816-b0c2-fec63ea9eafd.png)

**关键指令配置**

![](https://cdn.nlark.com/yuque/0/2024/png/40912025/1713150356599-eadf85bd-cc28-41a2-9d76-d35b7fea7b7c.png)

**运行结果**

![](https://cdn.nlark.com/yuque/0/2024/png/40912025/1713150381144-2e302981-f09d-430a-a9f1-bb5e7a4ddb8f.png)

### 场景2
再来一个例子，删除列表中所有的信息

**参考流程**

![](https://cdn.nlark.com/yuque/0/2024/png/40912025/1713150565000-9064cb2c-1c17-4245-8cc4-eefe371203f3.png)

**关键指令配置**

![](https://cdn.nlark.com/yuque/0/2024/png/40912025/1713150583769-78120e91-0bfd-4318-aa35-4464f6aabf64.png)

**运行结果**

![](https://cdn.nlark.com/yuque/0/2024/png/40912025/1713150620118-c5450cb2-d2e2-4fe4-b96b-51f5d8be51cc.png)

![](https://cdn.nlark.com/yuque/0/2024/png/40912025/1713150638222-3a2be83f-80ea-40aa-b439-558f0f341b85.png)

返回的结果则是一个None。此时已经删除了表中所有内容~

### 场景2
将要执行存储过程，这条存储过程为

```plain
create PROCEDURE test1
    @name NVARCHAR(100),
    @age INT
AS
BEGIN
    SELECT * FROM students WHERE age = @age;
    delete  from students where age = 11;
    insert into students values('小紫',20);
    select * from students;
    Delete  FROM students WHERE name = @name;
END;
```

原本的数据库中仅有一条数据：(小兰，20)

现在进行存储过程的执行

**关键指令配置**

![](https://cdn.nlark.com/yuque/0/2024/jpeg/40912025/1713931048719-441090a9-3490-4798-b84f-f82d7eb5fe80.jpeg)

**运行结果**：(将以一个列表代表一个结果集)

![](https://cdn.nlark.com/yuque/0/2024/jpeg/40912025/1713931081788-87e6fceb-86d2-45e7-80d5-56d481e37d0b.jpeg)

## 常见问题
暂无



