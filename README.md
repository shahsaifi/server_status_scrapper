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
2019-08-07 23:17:04,785 - INFO - connecting to from localhost:5000
2019-08-07 23:17:04,788 - INFO - connecting to from localhost:5000
2019-08-07 23:17:04,789 - INFO - connecting to from localhost:5000
2019-08-07 23:17:04,791 - INFO - connecting to from localhost:5000
2019-08-07 23:17:04,792 - INFO - connecting to from localhost:5000
2019-08-07 23:17:04,799 - INFO - connecting to from localhost:5000
2019-08-07 23:17:04,803 - INFO - connecting to from localhost:5000
2019-08-07 23:17:04,806 - INFO - connecting to from localhost:5000
2019-08-07 23:17:04,807 - INFO - connecting to from localhost:5000
2019-08-07 23:17:04,808 - INFO - connecting to from localhost:5000
2019-08-07 23:17:04,808 - ERROR - localhost:500 returned HTTPConnectionPool(host='localhost', port=500): Max retries exceeded with url: /status (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x113619110>: Failed to establish a new connection: [Errno 61] Connection refused'))

Status report of servers: 
   Application  Error_Count  Request_Count  Success_Count      Uptime Version
0      Cache0    905551894     1722952160      817400266  4029194611   0.2.0
1      Cache0    905551894     1722952160      817400266  4029194611   0.2.0
2      Cache0    905551894     1722952160      817400266  4029194611   0.2.0
3      Cache0    905551894     1722952160      817400266  4029194611   0.2.0
4      Cache0    905551894     1722952160      817400266  4029194611   0.2.0
5      Cache0    905551894     1722952160      817400266  4029194611   0.2.0
6      Cache0    905551894     1722952160      817400266  4029194611   0.2.0
7      Cache0    905551894     1722952160      817400266  4029194611   0.2.0
8      Cache0    905551894     1722952160      817400266  4029194611   0.2.0
9      Cache0    905551894     1722952160      817400266  4029194611   0.2.0 
```

- Generating json output:
```bash
 ᐅ python server_status_scrapper.py -s example.txt -j
2019-08-07 23:17:32,316 - INFO - connecting to from localhost:5000
2019-08-07 23:17:32,319 - INFO - connecting to from localhost:5000
2019-08-07 23:17:32,321 - INFO - connecting to from localhost:5000
2019-08-07 23:17:32,324 - INFO - connecting to from localhost:5000
2019-08-07 23:17:32,326 - INFO - connecting to from localhost:5000
2019-08-07 23:17:32,333 - INFO - connecting to from localhost:5000
2019-08-07 23:17:32,342 - INFO - connecting to from localhost:5000
2019-08-07 23:17:32,342 - INFO - connecting to from localhost:5000
2019-08-07 23:17:32,342 - INFO - connecting to from localhost:5000
2019-08-07 23:17:32,343 - INFO - connecting to from localhost:5000
2019-08-07 23:17:32,344 - ERROR - localhost:500 returned HTTPConnectionPool(host='localhost', port=500): Max retries exceeded with url: /status (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x1184c9350>: Failed to establish a new connection: [Errno 61] Connection refused'))

Json format data from server status: 
 [{"Application": "Cache0", "Error_Count": 905551894, "Request_Count": 1722952160, "Success_Count": 817400266, "Uptime": 4029194611, "Version": "0.2.0"}, {"Application": "Cache0", "Error_Count": 905551894, "Request_Count": 1722952160, "Success_Count": 817400266, "Uptime": 4029194611, "Version": "0.2.0"}, {"Application": "Cache0", "Error_Count": 905551894, "Request_Count": 1722952160, "Success_Count": 817400266, "Uptime": 4029194611, "Version": "0.2.0"}, {"Application": "Cache0", "Error_Count": 905551894, "Request_Count": 1722952160, "Success_Count": 817400266, "Uptime": 4029194611, "Version": "0.2.0"}, {"Application": "Cache0", "Error_Count": 905551894, "Request_Count": 1722952160, "Success_Count": 817400266, "Uptime": 4029194611, "Version": "0.2.0"}, {"Application": "Cache0", "Error_Count": 905551894, "Request_Count": 1722952160, "Success_Count": 817400266, "Uptime": 4029194611, "Version": "0.2.0"}, {"Application": "Cache0", "Error_Count": 905551894, "Request_Count": 1722952160, "Success_Count": 817400266, "Uptime": 4029194611, "Version": "0.2.0"}, {"Application": "Cache0", "Error_Count": 905551894, "Request_Count": 1722952160, "Success_Count": 817400266, "Uptime": 4029194611, "Version": "0.2.0"}, {"Application": "Cache0", "Error_Count": 905551894, "Request_Count": 1722952160, "Success_Count": 817400266, "Uptime": 4029194611, "Version": "0.2.0"}, {"Application": "Cache0", "Error_Count": 905551894, "Request_Count": 1722952160, "Success_Count": 817400266, "Uptime": 4029194611, "Version": "0.2.0"}] 
```

- Generating json parseable file:
```bash
  ᐅ python server_status_scrapper.py -s example.txt -f
2019-08-07 23:17:38,443 - INFO - connecting to from localhost:5000
2019-08-07 23:17:38,445 - INFO - connecting to from localhost:5000
2019-08-07 23:17:38,450 - INFO - connecting to from localhost:5000
2019-08-07 23:17:38,450 - INFO - connecting to from localhost:5000
2019-08-07 23:17:38,451 - INFO - connecting to from localhost:5000
2019-08-07 23:17:38,460 - INFO - connecting to from localhost:5000
2019-08-07 23:17:38,462 - INFO - connecting to from localhost:5000
2019-08-07 23:17:38,468 - ERROR - localhost:500 returned HTTPConnectionPool(host='localhost', port=500): Max retries exceeded with url: /status (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x10dd7d110>: Failed to establish a new connection: [Errno 61] Connection refused'))
2019-08-07 23:17:38,470 - INFO - connecting to from localhost:5000
2019-08-07 23:17:38,470 - INFO - connecting to from localhost:5000
2019-08-07 23:17:38,471 - INFO - connecting to from localhost:5000

Json format file is saved to /Users/sahnawaz/code/server_status_report/status_report.txt 

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
