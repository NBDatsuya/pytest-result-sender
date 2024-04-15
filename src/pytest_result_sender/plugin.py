from datetime import datetime
import pytest

data = {}


def pytest_configure():
    # exq after conf loading and be4 tuc exq
    data['start_time'] = datetime.now()
    print(f"{data['start_time']} python开始执行")


def pytest_unconfigure():
    # exq b4 conf unloading and be4 tuc exq
    data['end_time'] = datetime.now()
    print(f"{data['end_time']} python结束执行")

    data['duration'] = data['end_time'] - data['start_time']

    print(data)
