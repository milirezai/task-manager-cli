from collections import Counter

def analysi_tasks(data, status: list)-> list:
    statsu_count = Counter(status)
    return [
            len(data) - 1,
            statsu_count.most_common(1),
            statsu_count['completed'],
            statsu_count['uncompleted']
        ]

def show_task_analysis(task):
    print('\n=====================================')
    print('            tasks                ')
    print('=====================================\n')
    print(f'all : {task[0]}')
    print(f'most status : {task[1][0][0]}')
    print(f'completed : {task[2]}')
    print(f'uncompleted : {task[3]}','\n')

def task_serialize(task)-> str:
        return f"\nid: {task.id}. title: {task.title}. description: {task.description}. status: {task.status}. created_at: {task.created_at}. updated_at: {task.updated_at}"

def select_operation():
    print('\n\n=====================================')
    print('            operations                ')
    print('=====================================')
    print('\n1 - create task  ')
    print('2 - list task  ')
    print('3 - search task  ')
    print('4 - update task  ')     
    print('5 - complecte task  ')     
    print('6 - uncompleted task  ')     
    print('7 - delete task  ')     
    print('8 - close \n   ')
    return int(input('things you can do badly :    '))     

def create_task()-> tuple:
     print('\ncreate a new task:')
     title = input('name? ')
     description = input('description? ')
     new_task = {"title": title,"description": description}
     return new_task
 
def update_task():
    print('\nupdate a task:')
    id = int(input('id? '))
    title = input('new name? ')
    description = input('new description? ')
    status = input('new status? ')
    update_task = {'id': id ,'title': title,'description': description,'status': status}
    return update_task
 