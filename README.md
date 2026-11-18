# student-task-manager

A small Python console Student Task Manager, built to practise a complete
Git and GitHub workflow (branches, pull requests, conflicts, CI and releases).

Project status: Released (v1.0.0)

## Features

- Add tasks (empty titles are rejected)
- Show all tasks with a completed marker
- Mark a task as completed by its id
- Delete a task by its id
- Input validation with friendly error messages

## Setup

1. Install Python 3.10 or newer.
2. Clone the repository:

       git clone https://github.com/<your-username>/student-task-manager.git
       cd student-task-manager

No third-party packages are needed.

## Usage

    python app.py

Choose an option from the menu: `1` add, `2` show, `3` complete, `4` delete,
`5` exit. See [docs/user-guide.md](docs/user-guide.md) for examples.

## Run the tests

    python -m unittest discover -s tests -v

The same command runs automatically in GitHub Actions on every push to `main`
and on every pull request to `main`.

## License

MIT - see [LICENSE](LICENSE).
