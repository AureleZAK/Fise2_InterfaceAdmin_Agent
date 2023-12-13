"""This module defines an exemple of test"""
import threading
from fastapi.testclient import TestClient
from server import app
from domain.services.logservice import log_parser, count_log
from monitor import MonitorTask



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
    ip: str = "192.168.1.100"
    

    def __init__(self):
        super().__init__()
        # Définir des valeurs prédéfinies pour la RAM
        self.hostname_info = "usertest"
        self.ram_stats = {
            'total': 8000,  # Exemple : 8000 MB de RAM totale
            'used': 4000,   # 4000 MB utilisés
            'free': 4000,   # 4000 MB libres
            'percent': 50   # 50% d'utilisation
        }
        


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
page = {"/":2, "/?page_id=2":1, "/wp-cron.php":1, "/?p=1":1 }

def test_parsing():
    result = log_parser(log)
    assert result == result_log

def test_count_log() :
    result = count_log("src/tests/filelog.txt")
    assert result['total_ip'] == 3
    assert result['good'] == 4
    assert result['error'] == 1
    assert result['total_pages'] == page


def test_get_cpu_core():
    response = client.get("/metrics/v1/cpu/core")
    # we can test types but not values because they will change at each test.
    assert response.status_code == 200
    assert isinstance(response.json()["number"], int)

def test_get_ram():
    original_monitortask = app.state.monitortask

    app.state.monitortask = MonitorTaskFake()

    response = client.get("/metrics/v1/ram")
    assert response.status_code == 200
    data = response.json()

    assert data == {
        'total': 8000,
        'used': 4000,
        'free': 4000,
        'percent': 50
    }

    app.state.monitortask = original_monitortask

def test_get_ip():
    save_app = app.state.monitortask
    
    app.state.monitortask = MonitorTaskFake()
    response = client.get("/metrics/v1/ip")
    print(f"Response IP: {response.json()}")
    assert response.status_code == 200
    assert response.json() == {"ip": "testclient"}
    app.state.monitortask = save_app

def test_get_hostname():
    save_app = app.state.monitortask
    
    app.state.monitortask = MonitorTaskFake()
    
    response = client.get("/metrics/v1/hostname")
    data = response.json()
    assert response.status_code == 200
    assert data == {"hostname": "usertest"}
    app.state.monitortask = save_app