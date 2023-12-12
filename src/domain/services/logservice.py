"""
This module defines a controller class for fetching CPU values from a monitoring task.
"""
from domain.models import Log
import apache_log_parser

def log_parser(log_entry):
    log_format = '%v %h %l %u %t "%r" %>s %b "%{Referer}i" "%{User-Agent}i"'
    parser = apache_log_parser.make_parser(log_format)

    parsed_data = parser(log_entry)
    result_log = [
        parsed_data.get('remote_host', ''),
        parsed_data.get('time_received', ''),
        parsed_data.get('request_first_line', ''),
        parsed_data.get('status', '')
    ]
    return result_log

def count_log(log_file):
    unique_ips = set()
    cpt404 = 0
    cpt200 = 0
    page_visits = {}

    try:
        with open(log_file, 'r') as file:
            for line in file:
                log_entry = log_parser(line)
                ip = log_entry[0]
                status = log_entry[3]
                request_url = log_entry[2]
                request_url_split = request_url.split()[1]
                page_visits[request_url_split] = page_visits.get(request_url_split,0)+1
                if (status == '404'):
                    cpt404 = cpt404 + 1
                else:
                    cpt200 = cpt200 + 1

                if (ip != '127.0.0.1'):
                    unique_ips.add(ip)

        return {'total_ip': len(unique_ips), 'good': cpt200, 'error':cpt404, 'total_pages':page_visits}

    except FileNotFoundError:
        print(f"Le fichier {log_file} n'a pas été trouvé.")
        return None


# Controller class to fetch cpu values from monitoring task
class LogService:

    def __init__(self):
        ...

    async def get_log(self) -> Log:
        result= count_log("src/tests/filelog.txt")
        return Log(
            nbip= result['total_ip'],
            failed= result['error'],
            succed= result['good'],
            nbwebsites= result['total_pages'])

    def __str__(self):
        return self.__class__.__name__
