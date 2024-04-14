from datetime import datetime


def pytest_configure():
    # exq after conf loading and be4 tuc exq
    print(f"{datetime.now()} python开始执行")


def pytest_unload_configure():
    # exq b4 conf unloading and be4 tuc exq
    print(f"{datetime.now()} python结束执行")
