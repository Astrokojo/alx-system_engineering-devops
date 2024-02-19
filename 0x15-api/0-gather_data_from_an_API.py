#!/usr/bin/python3
"""
Script returns TODO list progress when given emloyee ID
"""

import requests
import sys

if __name__ == "__main__":
    api_url = 'https://jsonplaceholder.typicode.com/'
    user_id = {'userId': sys.argv[1]}

    todos_response = requests.get(api_url + "todos", params=user_id)
    todos = todos_response.json()

    employee_response = requests.get(api_url + "users/{}".format(sys.argv[1]))
    employee = employee_response.json()

    completed = [t.get("title") for t in todos if t.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        employee.get("name"), len(completed), len(todos)))
    [print("\t {}".format(c)) for c in completed]
    print(todos_response.url)
