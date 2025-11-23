# 描述
根据应用名称或uuid，将该应用依赖的python模块加入当前应用环境，使当前应用能够成功导入该应用依赖的python模块。

<font style="color:#DF2A3F;">注意：指定的应用必须在本地有代码(成功打开应用后再关闭即可，或者运行一次，会自动下载代码)</font>

![](https://cdn.nlark.com/yuque/0/2023/png/22242030/1676516203442-ed90452d-9898-4cee-a033-011efd8e5bd7.png)



# 参数配置
## 指令输入
### 常规
**应用名称：**当前账号创建的应用的名称或者应用的uuid







## 指令输出
**保存模块列表至：**保存指定应用所依赖的Python名称（仅仅只是名称而已，方便查看该应用依赖了哪些模块）





# 参考案例
## 场景
使用案例



在【python模块管理】应用中安装两个python模块

![](https://cdn.nlark.com/yuque/0/2023/png/22242030/1676536079513-b460f7d6-9b1b-47aa-bad5-4f45261f45e3.png)





在其他应用中使用【python模块管理】应用中的模块



可视化方式

![](https://cdn.nlark.com/yuque/0/2023/png/22242030/1676516430970-2a0dcd75-f2d2-4ca8-9631-e195334620b4.png)



代码方式

```python
# 使用提醒:
# 1. xbot包提供软件自动化、数据表格、Excel、日志、AI等功能
# 2. package包提供访问当前应用数据的功能，如获取元素、访问全局变量、获取资源文件等功能
# 3. 当此模块作为流程独立运行时执行main函数
# 4. 可视化流程中可以通过"调用模块"的指令使用此模块

import xbot
from xbot import print, sleep

from .import package
from .package import variables as glv
from xbot_extensions import activity_venv # 导入指令

activity_venv.introduce("python模块管理")  # 引入【python模块管理】应用依赖的python模块

# 导入所需的模块
import lxml  
import numpy 
# 有多个可以导入多个

def main(args):

    pass
```



