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
    """
    Test case for the '/health' endpoint.

    This function sends a GET request to the '/health' endpoint using the TestClient
    to check the health status of the API. It asserts that the response status code
    should be 200 if the API health check endpoint is functioning correctly.

    Raises:
        AssertionError: If the response status code is not 200.

    """
    response = client.get("/health")
    assert response.status_code == 200


def test_get_cpu_usage():
    """
    Test case for the '/metrics/v1/cpu/usage' endpoint.

    This function tests the '/metrics/v1/cpu/usage' endpoint by sending a GET request
    using the TestClient. It sets up a fake monitor to provide deterministic CPU usage
    values, then asserts that the response status code is 200 and checks if the returned
    JSON matches the expected CPU usage values.

    Raises:
        AssertionError: If the response status code is not 200 or the CPU usage values
                        in the response JSON don't match the expected values.
    """
    # backup of the existing monitortask to restore it after the test
    save_app = app.state.monitortask
    # use fake monitor to have deterministic values
    app.state.monitortask = MonitorTaskFake()
    response = client.get("/metrics/v1/cpu/usage")
    assert response.status_code == 200
    assert response.json() == [{"id": 0, "usage": 10}, {"id": 1, "usage": 12}]
    # restore monitortask for next test
    app.state.monitortask = save_app

LOG = (
    'localhost:80 192.168.240.50 - - [08/Dec/2023:08:55:20 +0000] "GET / HTTP/1.0" '
    '200 15075 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
    '(KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"'
)


result_log = ['192.168.240.50','[08/Dec/2023:08:55:20 +0000]','GET / HTTP/1.0','200']
page = {"/":2, "/?page_id=2":1, "/wp-cron.php":1, "/?p=1":1 }

def test_parsing():
    """
    Test case for parsing a log using `log_parser`.

    This function tests the `log_parser` function by passing a log message
    (`LOG`) and checks if the returned result matches the `result_log`.

    Raises:
        AssertionError: If the parsed result does not match the expected result.
    """
    result = log_parser(LOG)
    assert result == result_log

def test_count_log() :
    """
    Test case for counting logs in a file.

    This function tests the `count_log` function by providing a file path
    and asserts the counts of unique IPs, successful requests, failed requests,
    and page visit counts against expected values.

    Raises:
        AssertionError: If the counts of IPs, successful requests, failed requests,
                        or page visits do not match the expected values.
    """
    result = count_log("src/tests/filelog.txt")
    assert result['total_ip'] == 3
    assert result['good'] == 4
    assert result['error'] == 1
    assert result['total_pages'] == page


def test_get_cpu_core():
    """
    Test case for fetching CPU core information.

    This function sends a GET request to the '/metrics/v1/cpu/core' endpoint
    using the TestClient and asserts the status code and the type of the JSON response.

    Raises:
        AssertionError: If the response status code is not 200 or if the type of
                        the JSON response['number'] is not an integer.
    """
    response = client.get("/metrics/v1/cpu/core")
    # we can test types but not values because they will change at each test.
    assert response.status_code == 200
    assert isinstance(response.json()["number"], int)

def test_get_ram():
    """
    Test case for fetching RAM information.

    This function tests the '/metrics/v1/ram/ram' endpoint by sending a GET request
    and asserting the status code and the retrieved RAM information in the JSON response.

    Raises:
        AssertionError: If the response status code is not 200 or if the retrieved
                        RAM information in the JSON response does not match the expected values.
    """
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
    """
    Test case for fetching IP information.

    This function tests the '/metrics/v1/ip/ip' endpoint by sending a GET request
    and checks if the response status code and the JSON response['ip'] match the expected value.

    Raises:
        AssertionError: If the response status code is not 200 or if the retrieved IP
                        information in the JSON response does not match the expected value.
    """
    save_app = app.state.monitortask
    app.state.monitortask = MonitorTaskFake()
    response = client.get("/metrics/v1/ip")
    print(f"Response IP: {response.json()}")
    assert response.status_code == 200
    # Vérifier si 'ip' est présent dans la réponse JSON
    json_response = response.json()
    assert 'ip' in json_response, "Response does not contain 'ip' key"

    # Vérifier la valeur de 'ip' uniquement si 'ip' est présent dans la réponse
    if 'ip' in json_response:
        assert json_response['ip'] == "testclient"
    app.state.monitortask = save_app


def test_get_hostname():
    """
    Test case for fetching hostname information.

    This function tests the '/metrics/v1/hostname/hostname' endpoint by sending a GET request
    and verifies if the response status code and the retrieved hostname information 
    in the JSON response
    match the expected value.

    Raises:
        AssertionError: If the response status code is not 200 or if the retrieved hostname
                        information in the JSON response does not match the expected value.
    """
    save_app = app.state.monitortask
    app.state.monitortask = MonitorTaskFake()
    response = client.get("/metrics/v1/hostname/hostname")
    data = response.json()
    assert response.status_code == 200
    assert data == {"hostname": "usertest"}
    app.state.monitortask = save_app
