# 一.功能描述
本指令可以根据进程号杀进程，达到关闭某一应用的效果。

# 二.使用参数说明
![](https://cdn.nlark.com/yuque/0/2023/png/561060/1675922695466-d53ae8f4-99b9-47c0-a17b-7e63f05ae134.png)

## 1.输入参数
PID介绍：<font style="background-color:#FBDE28;">进程的进程号</font>

PID数据格式：<font style="background-color:#FBDE28;">int类型</font>

## 2.输出参数
无

# 三.结果样例及展示说明
使用前：

![](https://cdn.nlark.com/yuque/0/2023/png/561060/1675922936562-5eea5289-b34d-442b-bd49-cd584b1a017a.png)

使用后：

![](https://cdn.nlark.com/yuque/0/2023/png/561060/1675922997015-db1e12c9-a2b0-47a2-a2f9-abed44b285f2.png)

# 四.常见问题
## q1：使用后应用依旧存在
a1：检查进程号是否为主进程号，有些应用有多个进程号需找到主进程号才可关闭应用；或者添加管理员权限运行。

