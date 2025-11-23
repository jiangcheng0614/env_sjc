import os
import time
import excute
import main
def process_directory(path, parent_id):
    if not os.path.exists(path) or not os.path.isdir(path):
        print(f"路径 {path} 不存在或不是一个目录。")
        return

    # 遍历目录中的每个条目
    for entry in os.listdir(path):
        full_path = os.path.join(path, entry)
        if os.path.isdir(full_path):
            result = excute.excute_filed(entry, parent_id)  # 调用函数 excute_filed 并获取返回的字典
            print(f"已经新建文件夹{entry}")
            new_id = result[entry]  # 从字典中提取新的文件夹 ID
            process_directory(full_path, new_id)  # 递归处理子目录
        elif os.path.isfile(full_path) and entry.lower().endswith('.md'):
            print(f"新建文件{entry}")
            mdid = excute.excute_md(entry.split(".")[0], parent_id)  # 调用函数 excute_md，并传递父目录 ID
            print(full_path, mdid)
            print(f"开始写入md数据进入{entry}")
            main.run(full_path, mdid)
            print(f"{entry}数据写入完成")
            time.sleep(2)
            print("休息结束，开始下一个任务")


if __name__ == '__main__':
# 使用示例
    md_path = r"C:\Users\11758\Desktop\新建文件夹 (2)\自定义指令文档"  # 替换为你的目录路径
    process_directory(md_path, '719719693357096960')
