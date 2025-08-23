def generate_numbered_tasks(tasks: list[str]):
    numbered_tasks = []
    for index, task in enumerate(tasks, start=1):
        numbered_tasks.append(f"{index}. {task}")
    return numbered_tasks
