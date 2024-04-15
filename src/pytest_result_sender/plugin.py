from datetime import datetime, timedelta

import pytest

data = {
    "failed": 0,
    "passed": 0,
    "start_time": datetime.now(),
    "end_time": datetime.now(),
    "pass_ratio": 0.0,
    "pass_ratio_percentage": "0.000000%"
}


def pytest_configure(config):
    # exq after conf loading and be4 tuc exq
    data["start_time"] = datetime.now()
    print(f"{data['start_time']} python开始执行")


def pytest_unconfigure(config):
    # exq b4 conf unloading and be4 tuc exq
    data["end_time"] = datetime.now()
    print(f"{data['end_time']} python结束执行")

    data["duration"] = data["end_time"] - data["start_time"]
    data["pass_ratio"] = data["passed"] / data["total"]
    data["pass_ratio_percentage"] = "%.6f%%" % (data["pass_ratio"]*100)

    print(data)

    assert timedelta(seconds=3.5) > data["duration"] >= timedelta(seconds=3.1)
    assert data["total"] == 3
    assert data["passed"] == 2
    assert data["failed"] == 1
    assert data["pass_ratio"] == 2 / 3
    assert data["pass_ratio_percentage"] == "66.6667%"


def pytest_collection_finish(session: pytest.Session):
    data["total"] = len(session.items)


def pytest_runtest_logreport(report: pytest.TestReport):
    # setup call teardown
    if report.when == "call":
        data[report.outcome] += 1
