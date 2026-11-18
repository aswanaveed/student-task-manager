# User Guide

## Start the program

    python app.py

## Menu

| Option | Action   | What it asks for        |
|--------|----------|-------------------------|
| 1      | Add      | A task title            |
| 2      | Show     | Nothing                 |
| 3      | Complete | The id of a task        |
| 4      | Delete   | The id of a task        |
| 5      | Exit     | Nothing                 |

## Example session

    Menu: 1 Add | 2 Show | 3 Complete | 4 Delete | 5 Exit
    Choose an option: 1
    Task title: Write report
    Added task 1.
    Choose an option: 3
    Task id to complete: 1
    Task marked as completed.
    Choose an option: 2
    [x] 1. Write report

## Error messages

- `Task title cannot be empty.` - type at least one visible character.
- `task id must be a number.` - ids are whole numbers shown in the list.
- `No task with id N.` - check the id with option 2 first.
