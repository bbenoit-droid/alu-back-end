#!/usr/bin/python3
# """ Library to gather data from an API. """

# import requests
# import sys

# """ Script to return a given employee ID
# together with their TODO list progress
# """

# if __name__ == "__main__":
#     employee_id = sys.argv[1]
#     url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)

#     todo = "https://jsonplaceholder.typicode.com/todos?userId={}"
#     todo = todo.format(employee_id)

#     user_info = requests.request("GET", url).json()
#     todo_info = requests.request("GET", todo).json()

#     employee_name = user_info.get("name")
#     total_tasks = list(filter(lambda x: (x["completed"] is True), todo_info))
#     task_com = len(total_tasks)
#     total_task_done = len(todo_info)

#     print(
#         "Employee {} is done with tasks({}/{}):".format(
#             employee_name, task_com, total_task_done
#         )
#     )
#     [print("\t {}".format(task.get("title"))) for task in total_tasks]

#!/usr/bin/python3
"""
Returns information about an employee's TODO list progress.
"""

import requests
import sys

if __name__ == "__main__":
    employee_id = sys.argv[1]

    user = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    ).json()

    todos = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    ).json()

    completed = [task for task in todos if task["completed"]]

    print(
        f"Employee {user['name']} is done with tasks"
        f"({len(completed)}/{len(todos)}):"
    )

    for task in completed:
        print(f"\t {task['title']}")
