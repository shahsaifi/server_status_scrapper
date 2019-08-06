"""
server status scrapper using /status of each given server
"""
import requests
import json
import pandas
import argparse


def fetch_status(server):
    status_url = "http://{}.twitter.com/status".format(server)

    try:
        response = requests.get(status_url)
        return response.json()
    except requests.exceptions.ConnectionError as e:
        e = "ConnectionError"
        return e


def main():
    parser = argparse.ArgumentParser(description='Fetch status page of server for aggregated report')
    parser.add_argument("-s", "--server", action='store', help="input a file with server names")
    parser.add_argument("-t", "--table", action='store_true', help="print a human readable table")
    parser.add_argument("-j", "--json", action='store_true', help="print a json parseable output")
    parser.add_argument("-f", "--file", action='store_true', help="save json output to a file")

    args = parser.parse_args()

    data = []
    bad_data = {}

    if args.server:
        servers_to_parse = [i.strip() for i in open(args.server).readlines()]

        for serv in servers_to_parse:
            serv_output = fetch_status(serv)
            if isinstance(serv_output, dict):
                data.append(serv_output)
            else:
                bad_data[serv] = serv_output

    human_readable = pandas.DataFrame.from_dict(data)
    bad_nodes = json.dumps(bad_data)

    if args.table:
        print(human_readable)
        print(bad_data)

    if args.json:
        print(json.dumps(data))
        print(bad_nodes)

    if args.file:
        print(bad_nodes)
        with open('status_report.txt', 'w') as f:
            f.write(json.dumps(data))


if __name__ == "__main__":
    main()
