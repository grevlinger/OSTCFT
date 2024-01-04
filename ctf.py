from tasks import tasks

def get_task_by_id(task_id):
    for task in tasks:
        if task['id'] == task_id:
            return task
    return None
