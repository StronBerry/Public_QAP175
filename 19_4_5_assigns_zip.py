def assign_tasks_to_engineers(engineers, tasks):
    return list(zip(engineers, tasks))

print(assign_tasks_to_engineers(['Mia', 'Noah', 'Olivia'], ['Task I', 'Task II', 'Task III']))