"""This module defines an exemple of test"""
import threading
from fastapi.testclient import TestClient
from server import app, log_parser, count_ip
from monitor import MonitorTask
from domain.models import Ram



class MonitorTaskFake(MonitorTask):
    """
    Monitor class to mock the real monitor
    Instead of using the real monitor that fetch data on the host
    we use a monitor that provide "fake" values to control the output
    and make deterministic test (deterministic = repeatable and known values)
    """
    interval: int = 0
    cpu_percent: list[float] = [10, 12]
    num_cores: int = 3
    ram_info: Ram = Ram(total=12345678, percent=57.8)


    def monitor(self):
        pass

# Launching the real monitor for test involving the real monitor
client = TestClient(app)
thread = threading.Thread(target=app.state.monitortask.monitor, daemon=True)
thread.start()


def test_health():
    response = client.get("/health")
    assert response.status_code == 200


def test_get_cpu_usage():
    # backup of the existing monitortask to restore it after the test
    save_app = app.state.monitortask
    # use fake monitor to have deterministic values
    app.state.monitortask = MonitorTaskFake()
    response = client.get("/metrics/v1/cpu/usage")
    assert response.status_code == 200
    assert response.json() == [{"id": 0, "usage": 10}, {"id": 1, "usage": 12}]
    # restore monitortask for next test
    app.state.monitortask = save_app

log = 'localhost:80 192.168.240.50 - - [08/Dec/2023:08:55:20 +0000] "GET / HTTP/1.0" 200 15075 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"'
result_log = ['192.168.240.50','[08/Dec/2023:08:55:20 +0000]','GET / HTTP/1.0','200']


def test_parsing():
    result = log_parser(log)
    assert result == result_log

def test_count_ip() :
    result = count_ip("/Users/corentinlaval/Desktop/TSE/INTERFACE/ProjetV2/agent/src/tests/filelog.txt")
    assert result == 3


def test_get_cpu_core():
    response = client.get("/metrics/v1/cpu/core")
    # we can test types but not values because they will change at each test.
    assert response.status_code == 200
    assert isinstance(response.json()["number"], int)

def test_get_ram():
    save_app = app.state.monitortask
    app.state.monitortask = MonitorTaskFake()
    response = client.get("/metrics/v2/ram/usage")
    assert response.status_code == 200
    assert response.json() == {"total": 12345678, "percent": 57.8}
    app.state.monitortask = save_app