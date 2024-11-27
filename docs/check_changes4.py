import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import shutil
import time
# 定义一个事件处理器


def apend_to_file(file_path, content):
    with open(file_path, "a") as file:
        file.write(content)
        
class MyHandler(FileSystemEventHandler):
    def __init__(self):
        FileSystemEventHandler.__init__(self)

    def on_moved(self, event):
        if event.is_directory:
            print("directory moved from {0} to {1}".format(
                event.src_path, event.dest_path))
        else:
            print("file moved from {0} to {1}".format(
                event.src_path, event.dest_path))

    def on_created(self, event):
        if event.is_directory:
            print("directory created:{0}".format(event.src_path))
        else:
            print("file created:{0}".format(event.src_path))

    def on_deleted(self, event):
        if event.is_directory:
            print("directory deleted:{0}".format(event.src_path))
        else:
            print("file deleted:{0}".format(event.src_path))

    def on_modified(self, event):
        if event.is_directory:
            print("directory modified:{0}".format(event.src_path))
        else:
            print("file modified:{0}".format(event.src_path))
            # print(event.src_path)
            if ("\\source\\fnk_sku" in event.src_path):
                new_path = str(event.src_path).replace("fnk_sku", "fnk0066")
                # os.system("cp -r " + event.src_path + " " + new_path)
                shutil.copy2(event.src_path, new_path)
                apend_to_file(".\\changes\\changes.rst", str(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())) + "\n")


def monitor_directory(path):
    # 创建事件处理器实例
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    print(f"开始监听目录: {path}")

    try:
        while True:
            pass  # 保持程序运行
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


if __name__ == "__main__":
    # 输入你的目标目录路径
    watch_path = os.getcwd()+"\\source\\"
    folder_to_monitor = "C:\\path\\to\\your\\directory"
    monitor_directory(watch_path)
