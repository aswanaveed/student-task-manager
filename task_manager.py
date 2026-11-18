"""Core task logic for the Student Task Manager."""
from dataclasses import dataclass


@dataclass
class Task:
    id: int
    title: str
    completed: bool = False


class TaskManager:
    def __init__(self):
        self._tasks = []
        self._next_id = 1

    def add_task(self, title):
        task = Task(self._next_id, title)
        self._tasks.append(task)
        self._next_id += 1
        return task

    def get_tasks(self):
        return list(self._tasks)

    def _find(self, task_id):
        for task in self._tasks:
            if task.id == task_id:
                return task
        raise ValueError(f"No task with id {task_id}.")

    # --- complete ------------------------------------------------
    def complete_task(self, task_id):
        task = self._find(task_id)
        task.completed = True
        return task

    # --- delete --------------------------------------------------
    def delete_task(self, task_id):
        raise NotImplementedError("delete_task is not implemented yet")
