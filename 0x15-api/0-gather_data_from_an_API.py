#!/usr/bin/python3
"""
script that, uses this REST API, for a given employee ID, returns
information about his/her TODO list progress
"""

import json
import requests
from sys import argv


if __name__ == "__main__":

    sessionReq = requests.Session()

    EmpID = argv[1]
    urlID = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(EmpID)
    urlName = 'https://jsonplaceholder.typicode.com/users/{}'.format(EmpID)

    employee = sessionReq.get(urlID)
    employeeName = sessionReq.get(urlName)

    json_req = employee.json()
    name = employeeName.json()['name']

    total_tasks = 0

    for done_tasks in json_req:
        if done_tasks['completed']:
            total_tasks += 1

    print("Employee {} is done with tasks({}/{}):".
          format(name, total_tasks, len(json_req)))

    for done_tasks in json_req:
        if done_tasks['completed']:
            print("\t " + done_tasks.get('title'))
