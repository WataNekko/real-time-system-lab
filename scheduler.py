from collections import deque


class Task:
    def __init__(self, _pTask, _Delay, _Period):
        self.pTask = _pTask
        self.Delay = _Delay
        self.Period = _Period

    pTask = None
    Delay = 0
    Period = 0
    RunMe = 0
    TaskID = -1


class Scheduler:
    TICK = 1000
    SCH_MAX_TASKS = 40
    SCH_tasks_G = []
    current_index_task = 0

    def __int__(self):
        return

    def SCH_Init(self):
        self.current_index_task = 0

    def SCH_Add_Task(self, pFunction, DELAY, PERIOD):
        if self.current_index_task < self.SCH_MAX_TASKS:
            aTask = Task(pFunction, DELAY / self.TICK, PERIOD / self.TICK)
            aTask.TaskID = self.current_index_task
            self.SCH_tasks_G.append(aTask)
            self.current_index_task += 1
        else:
            print("PrivateTasks are full!!!")

    def SCH_Update(self):
        for i in range(0, len(self.SCH_tasks_G)):
            if self.SCH_tasks_G[i].Delay > 0:
                self.SCH_tasks_G[i].Delay -= 1
            else:
                self.SCH_tasks_G[i].Delay = self.SCH_tasks_G[i].Period
                self.SCH_tasks_G[i].RunMe += 1

    def SCH_Dispatch_Tasks(self):
        for i in range(0, len(self.SCH_tasks_G)):
            if self.SCH_tasks_G[i].RunMe > 0:
                self.SCH_tasks_G[i].RunMe -= 1
                self.SCH_tasks_G[i].pTask()

    def SCH_Delete(self, aTask):
        return

    def SCH_GenerateID(self):
        return -1


class Scheduler2:
    TICK = 1000
    SCH_MAX_TASKS = 40
    SCH_tasks_G = deque()
    current_index_task = 0

    def __int__(self):
        return

    def SCH_Init(self):
        self.current_index_task = 0

    def SCH_Add_Task(self, pFunction, DELAY, PERIOD):
        if self.current_index_task < self.SCH_MAX_TASKS:
            aTask = Task(pFunction, DELAY / self.TICK, PERIOD / self.TICK)
            aTask.TaskID = self.current_index_task
            self._schedule_task(aTask)
            self.current_index_task += 1
        else:
            print("PrivateTasks are full!!!")

    def _schedule_task(self, task: Task):
        i = 0
        # find place to insert
        for curr_task in self.SCH_tasks_G:
            if (d := task.Delay - curr_task.Delay) > 0:
                task.Delay = d
            else:
                curr_task.Delay -= task.Delay
                self.SCH_tasks_G.insert(i, task)
                return
            i += 1

        # insert at the end if cannot find place
        self.SCH_tasks_G.append(task)

    def SCH_Update(self):
        if self.SCH_tasks_G[0].Delay > 0:
            self.SCH_tasks_G[0].Delay -= 1

    def SCH_Dispatch_Tasks(self):
        while task := self.SCH_tasks_G[0]:
            if task.Delay > 0:
                return
            # run then reschedule all ready tasks from the beginning of the deque
            task.pTask()

            self.SCH_tasks_G.popleft()
            task.Delay = task.Period
            self._schedule_task(task)

    def SCH_Delete(self, aTask):
        return

    def SCH_GenerateID(self):
        return -1
