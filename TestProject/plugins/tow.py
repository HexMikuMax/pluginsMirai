"""
pluginMirai插件模版
"""
import time


class plugins:
    def config(self) -> dict:
        # 插件配置项
        config = {
            "pluginName": "测试插件1",  # 插件的名字
            "Version": "v1.0.39",  # 插件的版本
            "uri": "http://127.0.0.1",  # MiraiHTTPAPI接口地址
            "port": "8080",  # MiraiHTTPAPI端口地址
            "verifyKey": "87654321",  # 接口连接密钥
            "BotID": "87654321"  # QQBot的号码
        }
        return config

    def activate(self):
        # 在加载插件的过程中加载一次此方法
        print("这是第一次调用此方法！")

    def render(self):
        # 循环运行的主程序方法
        pass

    def deactivate(self):
        # 框架关闭时运行 用于释放一些资源使用
        pass
