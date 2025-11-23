## <font style="background-color:rgb(217,245,214);">执行sql语句</font>
#### 描述
执行自定义的sql语句, select语句返回结果, 其他返回布尔类型

#### 使用示例
这里的:1, :2 表示占位符, 然后通过sql语句参数列表进行传参.【占位符的格式要求是以冒号（:）开头，后面跟着一个数字或者字母组成的标识符。:1, :name, :id都可以】

![](https://cdn.nlark.com/yuque/0/2023/png/12484056/1701311597648-54d24d2e-8f8d-4003-abaa-b7aff658fe3b.png)

或者

![](https://cdn.nlark.com/yuque/0/2023/png/12484056/1701311625164-cd423f20-fa34-404f-af69-4bc32c266cbf.png)

#### 执行select语句
![](https://cdn.nlark.com/yuque/0/2023/png/12484056/1701159840685-67064e4e-dbe0-4eb5-961d-a361e864b701.png)

高级中可以设置是否以字典格式返回查询结果

![](https://cdn.nlark.com/yuque/0/2023/png/12484056/1701159840731-4c336912-2b78-439b-897e-ed39cb344cd0.png)

勾选时的结果样式:

```plain
[{'ID': '5', 'NAME': '4', 'AGE': 9999, 'MY_Love': '4', '备注': '999', 'SALARY': 1.0, 'SALARY2': None}, {'ID': '4', 'NAME': '4', 'AGE': 9999, 'MY_Love': '4', '备注': '999', 'SALARY': None, 'SALARY2': None}, {'ID': '1', 'NAME': '999', 'AGE': 9999, 'MY_Love': '1', '备注': '999', 'SALARY': 2.0, 'SALARY2': None}]
```

取消勾选的结果样式:

```plain
[('5', '4', 9999, '4', '999', 1.0, None), ('4', '4', 9999, '4', '999', None, None), ('1', '999', 9999, '1', '999', 2.0, None)]
```

