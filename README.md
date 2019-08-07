## Server Status Scrapper 

`server_status_scrapper.py` tool scrapes `/status` page of servers given in a `file`.
 
#### Features 
 - generates human readable, 
 - json parseable output
 - saves json pareable data to a file.

`server_status_scrapper.py` is written using `python 3.7.4` version.
```bash
ᐅ python --version
Python 3.7.4
```
 
#### Modules used:
- [requests](https://pypi.org/project/requests/)
- [json](https://docs.python.org/3/library/json.html)
- [argparse](https://docs.python.org/3/library/argparse.html)
- [pandas](https://pypi.org/project/pandas/)
- [pytest](https://pypi.org/project/pytest/)
- [requests-mock](https://pypi.org/project/requests-mock/)
- [concurrent.futures](https://docs.python.org/3/library/concurrent.futures.html)
- [os](https://docs.python.org/3/library/os.html)
- [logging](https://docs.python.org/3/library/logging.html)

#### installing above modules
```bash
pip install -r requirements.txt
```

#### usage:
```bash
usage: server_status_scrapper.py [-h] [-s SERVER] [-t] [-j] [-f]

Fetch status page of server to generate an aggregated report

optional arguments:
  -h, --help            show this help message and exit
  -s SERVER, --server SERVER
                        input a server name or file with server names
  -t, --table           print a human readable table
  -j, --json            print a json output
  -f, --file            save to a file
```

### Examples
- Generating a table: 
```bash
ᐅ python server_status_scrapper.py -s example.txt -t
  Application  Error_Count  Request_Count  Success_Count      Uptime Version
0      Cache0    905551894     1722952160      817400266  4029194611   0.2.0
1      Cache1    905551894     1722952160      817400266  4029194611   0.2.0
2      Cache2    905551894     1722952160      817400266  4029194611   0.2.0
3      Cache3    905551894     1722952160      817400266  4029194611   0.2.0

{'Cache4': 'ConnectionError', 'server-0022': 'ConnectionError'}
```

- Generating json output:
```bash
ᐅ python server_status_scrapper.py -s example.txt -j | jq .
[
  {
    "Application": "Cache0",
    "Error_Count": 905551894,
    "Request_Count": 1722952160,
    "Success_Count": 817400266,
    "Uptime": 4029194611,
    "Version": "0.2.0"
  },
  {
    "Application": "Cache0",
    "Error_Count": 905551894,
    "Request_Count": 1722952160,
    "Success_Count": 817400266,
    "Uptime": 4029194611,
    "Version": "0.2.0"
  }
]
```

- Generating json parseable file:
```bash
 ᐅ python server_status_scrapper.py -s example.txt -f
 ᐅ cat status_report.txt | jq . 
[
  {
    "Application": "Cache0",
    "Error_Count": 905551894,
    "Request_Count": 1722952160,
    "Success_Count": 817400266,
    "Uptime": 4029194611,
    "Version": "0.2.0"
  },
  {
    "Application": "Cache0",
    "Error_Count": 905551894,
    "Request_Count": 1722952160,
    "Success_Count": 817400266,
    "Uptime": 4029194611,
    "Version": "0.2.0"
  }
]
```

### Testing
`server_status_scrapper.py` is tested for basic functionality of requests module with `test_sample.py` using `pytest` 
and `requests-mock` modules. To generate above examples outputs `flask` app was used mocking json output from a server.
```bash
 ᐅ py.test -v                                      
========================================================================================================================== test session starts ==========================================================================================================================
platform darwin -- Python 3.7.4, pytest-5.0.1, py-1.8.0, pluggy-0.12.0 -- /usr/local/opt/python/bin/python3.7
cachedir: .pytest_cache
rootdir: /Users/sahnawaz/code/server_status_scrapper
plugins: requests-mock-1.6.0
collected 1 item                                                                                                                                                                                                                                                        

test_sample.py::test_fixture PASSED                                                                                                                                                                                                                               [100%]

======================================================================================================================= 1 passed in 0.08 seconds ============================================================================
```

### Files in directory:
- `server_status_scrapper.py`: Contains code base for the report.
- `app.py`: A testing flask app, runs local server on port 5000 with sample data
- `requirements.txt`: Contains modules to be installed to use the tool
- `servers.txt`: an example file from challenge tarball
- `example.txt`: contains dummy servers list used with `app.py` for testing
- `test_sample.py`: contains test code
- `sample_status_report_file.txt`: a sample json output file from `server_status_scrapper.py`
