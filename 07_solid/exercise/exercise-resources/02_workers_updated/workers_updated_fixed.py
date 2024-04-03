from abc import abstractmethod, ABC
import time


class BaseWorker(ABC):

    @staticmethod
    @abstractmethod
    def work():
        ...


class Human(ABC):
    @staticmethod
    @abstractmethod
    def eat():
        ...


class Worker(BaseWorker, Human):

    @staticmethod
    def work():
        print("I'm normal worker. I'm working.")

    @staticmethod
    def eat():
        print("Lunch break....(5 secs)")
        time.sleep(5)


class SuperWorker(BaseWorker, Human):

    def work(self):
        print("I'm super worker. I work very hard!")

    def eat(self):
        print("Lunch break....(3 secs)")
        time.sleep(3)


class Robot(BaseWorker):

    @staticmethod
    def work():
        print("I'm a robot. I'm working....")


class BaseManager(ABC):

    def __init__(self):
        self.worker = None

    @abstractmethod
    def set_worker(self, worker):
        ...


class WorkManager(BaseManager):
    def set_worker(self, worker):
        assert isinstance(worker, BaseWorker), '`worker` must be of type {}'.format(BaseWorker)

        self.worker = worker

    def manage(self):
        self.worker.work()


class BreakManager(BaseManager):
    def set_worker(self, worker):
        assert isinstance(worker, Human), '`worker` must be of type {}'.format(Human)

        self.worker = worker

    def lunch_break(self):
        self.worker.eat()


# Test code
work_manager = WorkManager()
break_manager = BreakManager()
work_manager.set_worker(Worker())
break_manager.set_worker(Worker())
work_manager.manage()
break_manager.lunch_break()

work_manager.set_worker(SuperWorker())
break_manager.set_worker(SuperWorker())
work_manager.manage()
break_manager.lunch_break()

work_manager.set_worker(Robot())
work_manager.manage()

try:
    break_manager.set_worker(Robot())
    break_manager.lunch_break()
except AssertionError:
    pass
