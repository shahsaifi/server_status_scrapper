"""
server status scrapper using /status of each given server
"""
import requests
import json
import pandas
import argparse
import logging
import concurrent.futures
from os import getcwd


logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)


def fetch_status(url, timeout):
    status_url = "http://{}/twitter.com/status".format(url)

    try:
        response = requests.get(status_url, timeout=timeout)
        logging.info("connecting to from {}".format(url))
        return response.json()
    except requests.exceptions.ConnectionError as e:
        logging.error("{} returned {}".format(url, e))
        e = "ConnectionError"
        return e


def main():
    parser = argparse.ArgumentParser(description='Fetch status page of server to generate an aggregated report')
    parser.add_argument("-s", "--server", action='store', help="input a server name or file with server names")
    parser.add_argument("-t", "--table", action='store_true', help="print a human readable table")
    parser.add_argument("-j", "--json", action='store_true', help="print a json output")
    parser.add_argument("-f", "--file", action='store_true', help="save to a file")

    args = parser.parse_args()

    data = []
    current_working_dir = getcwd()
    file_to_dump = "{}/status_report.txt".format(current_working_dir)

    if args.server:
        servers_to_parse = [i.strip() for i in open(args.server).readlines()]

        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
            future_to_url = {executor.submit(fetch_status, url, 2): url for url in servers_to_parse}
            for future in concurrent.futures.as_completed(future_to_url):
                url = future_to_url[future]
                try:
                    serv_output = future.result()
                    if isinstance(serv_output, dict):
                        data.append(serv_output)
                except Exception as exc:
                    print("{} generated an exception: {}".format(url, exc))

    human_readable = pandas.DataFrame.from_dict(data)

    if args.table:
        print("\nStatus report of servers: \n {} \n".format(human_readable))

    if args.json:
        print("\nJson format data from server status: \n {} \n".format(json.dumps(data)))

    if args.file:
        with open(file_to_dump, 'w') as f:
            f.write(json.dumps(data))
        print("\nJson format file is saved to {} \n".format(file_to_dump))


if __name__ == "__main__":
    main()
