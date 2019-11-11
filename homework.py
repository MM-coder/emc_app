import os, os.path, json, datetime

current_year = datetime.datetime.now().year
current_month = datetime.datetime.now().month
current_day = datetime.datetime.now().day
current_min = datetime.datetime.now().minute
current_hour = datetime.datetime.now().hour


def create_tasks_if_not_exists():
    exists = os.path.exists('todo.json')
    if exists == False:
        print("[WARN] Could not find todo.json, initializing setup...")
        with open("todo.json","w+") as taskfile:
            task = {"tasks": [],"tasknumber": 0}
            json.dump(task, taskfile)
            print("[SUCCESS] setup complete")
    else:
        pass

def add_task(taskname: str, taskdescription: str, tasksubject: str, deliver_time, deliver_date):
    create_tasks_if_not_exists()
    with open("todo.json", "r") as read:
        data = json.load(read) # Gets current data
        number = data['tasknumber'] # Gets old number
    with open("todo.json", "w+") as tasks:
        tasknumb = number + 1
        split_date = deliver_date.split('-')
        deliverdate = str(datetime.date(int(current_year), int(split_date[1]), int(split_date[2])))
        task = {
            "number": tasknumb,
            "name": taskname,
            "description": taskdescription,
            "subject": tasksubject,
            "deliver_time": deliver_time,
            "deliver_date": deliverdate
        }
        data['tasks'].append(dict(task))
        data['tasknumber'] = tasknumb
        json.dump(data, tasks) # Dumps changes

def return_datetime_obj(data: str):
    split_date = data.split('-')
    return datetime.date(int(split_date[0]), int(split_date[1]), int(split_date[2]))



def remove_task(tasknumb: int):
    create_tasks_if_not_exists()
    with open("todo.json", "r") as read:
        data = json.load(read) # Gets current data
        number = data['tasknumber'] # Gets old number
    with open("todo.json", "w+") as tasks:
        newnumb = number - 1
        data['tasks'].pop(tasknumb - 1) # Removes task, since arrays start at 0 you need to subract 1
        data['tasknumber'] = newnumb
        json.dump(data, tasks) # Dumps changes

def get_next_task_due():
    create_tasks_if_not_exists()
    current_date = str(datetime.datetime.now().date())
    with open("todo.json", "r") as read:
        data = json.load(read)
        min_list = []
        for i in data['tasks']:
            print(type(i))
            if i['deliver_date'] == current_date:
                min_list.append(return_datetime_obj(i['deliver_date']))
                break
            if i['deliver_date'] < current_date:
                remove_task(i['number']) # Cleanup past events
            else:
                min_list.append(return_datetime_obj(i['deliver_date']))
        minimum = min(min_list)
        print(min_list)
        print(minimum)
        for i in data['tasks']:
            if i['deliver_date'] == str(minimum):
                return i