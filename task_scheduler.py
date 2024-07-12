import time
import datetime


class Task:
    
    def __init__(self,func,interval,set_time=None):
        self.func = func
        self.interval = interval
        self.next_run = set_time or datetime.datetime.now()
   
    
    
class Scheduler:
    def __init__(self):
        self.tasks = []
        self.running = False

    def add_task(self,func, interval, set_time=None):
        task = Task(func,interval,set_time)
        self.tasks.append(task)
        return task
        
    def start(self):
        self.running = True
        
        while self.running:
            now = datetime.datetime.now()
            for task in self.tasks:
                if now >= task.next_run:
                    task.func()
                    task.next_run = now + datetime.timedelta(seconds=task.interval)
            time.sleep(1)

    def stop(self):
        self.running = False








