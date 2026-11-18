"""Console interface for the Student Task Manager."""
from task_manager import TaskManager

MENU = "Menu: 1 Add | 2 Show | 3 Complete | 4 Delete | 5 Exit"


def show_tasks(manager):
    tasks = manager.get_tasks()
    if not tasks:
        print("No tasks yet.")
        return
    for task in tasks:
        mark = "x" if task.completed else " "
        print(f"[{mark}] {task.id}. {task.title}")


def handle_add(manager):
    title = input("Task title: ")
    try:
        task = manager.add_task(title)
    except ValueError as error:
        print(f"Error: {error}")
        return
    print(f"Added task {task.id}.")


def handle_complete(manager):
    raw = input("Task id to complete: ").strip()
    if not raw.isdigit():
        print("Error: task id must be a number.")
        return
    try:
        manager.complete_task(int(raw))
    except ValueError as error:
        print(f"Error: {error}")
        return
    print("Task marked as completed.")


def handle_delete(manager):
    task_id = int(input("Task id to delete: "))
    manager.delete_task(task_id)
    print("Task deleted.")


def main():
    manager = TaskManager()
    actions = {
        "1": handle_add,
        "2": show_tasks,
        "3": handle_complete,
        "4": handle_delete,
    }
    while True:
        print(MENU)
        choice = input("Choose an option: ").strip()
        if choice == "5":
            print("Goodbye!")
            break
        action = actions.get(choice)
        if action:
            action(manager)
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
