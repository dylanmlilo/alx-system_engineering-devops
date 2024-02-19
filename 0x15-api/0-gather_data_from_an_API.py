#!/usr/bin/python3
"""
script that uses REST API to return information about his/her
TODO list progress for a given employee ID
"""
import requests
import sys


def get_todo_list(employee_id):
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(employee_id)).json()
    todos = requests.get(url + "todos", params={"userId": employee_id}).json()

    comp_tasks = [task.get("title") for task in todos if task.get("completed")]
    print("Employee {} has completed {}/{} tasks:".format(
        user.get("name"), len(comp_tasks), len(todos)))
    for task in comp_tasks:
        print("\t{}".format(task))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: {} employee_id".format(sys.argv[0]))
        sys.exit(1)
    get_todo_list(sys.argv[1])
