#!/usr/bin/env python

import os
import json
import logging as log
from utils.common import LogManager

if __name__ == '__main__':
    print("RUNNING....")
    log_manager = LogManager()
    log_manager.init_logging()
    log.info("Hello World!")
    log.info("Environment: %s", os.environ)

    result = {'result': {
        'projectKey': 'TSTPRJ',
        'url': 'http://jira.yourcompany.example.com'
    }}

    with open(os.environ['RESULT_FILE'], 'w', encoding="utf8") as target_file:
        target_file.write(json.dumps(result))
