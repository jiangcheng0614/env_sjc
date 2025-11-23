![](https://cdn.nlark.com/yuque/0/2024/png/5368516/1709867630107-7c09dbd7-0869-459a-9b16-d40058df02d7.png)



比如创建一张数据表

![](https://cdn.nlark.com/yuque/0/2024/png/5368516/1709868032026-100b246e-3333-4fc5-9692-859cdaad63a5.png)

```sql
CREATE TABLE company_test (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    description TEXT
);
```

![](https://cdn.nlark.com/yuque/0/2024/png/5368516/1709868059047-ebb48ac3-380c-42a4-9a78-591c046a5672.png)

![](https://cdn.nlark.com/yuque/0/2024/png/5368516/1709868083810-98a4dad8-3d91-4089-b00a-b34cf200a02c.png)



注意事项:该指令不适应于执行查询语句，执行查询语句请使用Sql查询指令

