# 描述
异步关闭广告，网页刷新会失效，需要重新调用

![](https://cdn.nlark.com/yuque/0/2023/png/22242030/1690717373275-05773ab4-a336-49e4-b4f5-861cf1b35593.png)



# 参数配置
## 指令输入
### 常规
**网页对象：**需要关闭广告的网页对象

**广告Xpath：**广告弹窗的Xpath路径

**关闭方式：**

+ 隐藏 - 隐藏出现的广告
+ 点击	- 点击出现的广告，如果选择点击的方式，一定要是要能够触发点击事件的元素才能生效。

**使用内置广告Xpath：**内置的广告弹窗Xpath路径，随着时间的推移，会慢慢积累大家出现的广告元素，所以大家

遇到了新的广告，可以发给我，或者让我远程获取





## 指令输出
无





# 内置广告XPath表单
| 平台 | 域名 | XPath |
| --- | --- | --- |
| 抖店 | jinritemai.com | 1. //div[@class="auxo-modal-root" and .=""]<br/>2. //div[contains(@class, "index_DragController")] |
| 拼多多商家后台 | pinduoduo.com | 1. //div[@data-testid="beast-core-modal-mask" or @data-testid="beast-core-modal"] |
| 吉客云 | jackyun.com | 1. //*[@id="notice-center"] |
| 天猫后台 | myseller.taobao.com | 1. //div[@class="next-overlay-wrapper opened"] |




