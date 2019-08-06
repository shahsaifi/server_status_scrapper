import requests

response_sample = {"Application":"Cache0",
     "Version":"0.2.0",
     "Uptime":4029194611,
     "Request_Count":1722952160,
     "Error_Count":905551894,
     "Success_Count":817400266}

def test_fixture(requests_mock):
    requests_mock.get("http://Cache0/status", json=response_sample)
    response = requests.get("http://Cache0/status")

    assert response.json() == response_sample
