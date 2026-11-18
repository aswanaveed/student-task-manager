import unittest

from task_manager import TaskManager


class TaskManagerTests(unittest.TestCase):
    def setUp(self):
        self.manager = TaskManager()

    def test_add_task(self):
        task = self.manager.add_task("Write report")
        self.assertEqual(task.id, 1)
        self.assertEqual(task.title, "Write report")
        self.assertFalse(task.completed)
        self.assertEqual(len(self.manager.get_tasks()), 1)

    def test_add_task_rejects_empty_title(self):
        with self.assertRaises(ValueError):
            self.manager.add_task("   ")
        self.assertEqual(self.manager.get_tasks(), [])

    def test_complete_task(self):
        task = self.manager.add_task("Study Git")
        self.manager.complete_task(task.id)
        self.assertTrue(self.manager.get_tasks()[0].completed)

    def test_complete_unknown_task_raises(self):
        with self.assertRaises(ValueError):
            self.manager.complete_task(42)

    def test_delete_task(self):
        task = self.manager.add_task("Old task")
        self.manager.delete_task(task.id)
        self.assertEqual(self.manager.get_tasks(), [])

    def test_delete_unknown_task_raises(self):
        with self.assertRaises(ValueError):
            self.manager.delete_task(99)


if __name__ == "__main__":
    unittest.main()
