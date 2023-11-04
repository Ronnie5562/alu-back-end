#!/usr/bin/python3
"""
    Using a REST API, and a given emp_ID, return info about their TODO list progress.
"""
import json
import requests
import sys


if __name__ == "__main__":
    """ main section """
    employee = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}/'.format(sys.argv[1])).json()
    EMPLOYEE_NAME = employee.get("name")
    employee_todos = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}/todos'.format(sys.argv[1])).json()
    serialized_todos = {}

    for todo in employee_todos:
        serialized_todos.update({todo.get("title"): todo.get("completed")})

    COMPLETED_TODOS_LENGTH = len([k for k, v in serialized_todos.items() if v is True])
    print("Employee {} is done with tasks({}/{}):".format(
        EMPLOYEE_NAME, COMPLETED_TODOS_LENGTH, len(serialized_todos)))
    for key, val in serialized_todos.items():
        if val is True:
            print("\t {}".format(key))
