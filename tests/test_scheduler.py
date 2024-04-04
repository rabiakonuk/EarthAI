import sys
import os
import unittest
# Add the src directory to the system path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
from scheduler import Task, DynamicTaskScheduler
from batching import SelectiveBatching

class TestTask(unittest.TestCase):
    def setUp(self):
        # Setup for each test
        self.task = Task(task_id=1, priority=1, execution_time=10, data="Test data")

    def test_task_creation(self):
        # Test if the task is created with the correct properties
        self.assertEqual(self.task.task_id, 1)
        self.assertEqual(self.task.priority, 1)
        self.assertEqual(self.task.execution_time, 10)
        self.assertEqual(self.task.data, "Test data")

class TestSelectiveBatching(unittest.TestCase):
    def setUp(self):
        # Setup for each test
        self.batching = SelectiveBatching()
        self.tasks = [Task(task_id=i, priority=1, execution_time=10, data=f"Test data {i}") for i in range(5)]

    def test_batch_creation(self):
        # Test if the batching groups tasks appropriately
        max_batch_size = 20
        self.batching.create_batch(self.tasks, max_batch_size)
        for batch_type, batch in self.batching.batches:
            self.assertTrue(sum(task.data_size for task in batch) <= max_batch_size)

    def test_batch_edge_cases(self):
        # Test edge cases like zero execution time or large data size
        edge_tasks = [Task(task_id=999, priority=1, execution_time=0, data="Zero execution time"),
                      Task(task_id=1000, priority=1, execution_time=10, data="Large data", data_size=999999)]
        self.batching.create_batch(edge_tasks, max_batch_size=1000000)
        # Assert that batches are created even for edge cases
        self.assertEqual(len(self.batching.batches), 2)

class TestDynamicTaskScheduler(unittest.TestCase):
    def setUp(self):
        # Setup for each test
        self.scheduler = DynamicTaskScheduler(max_workers=2)
        self.tasks = [Task(task_id=i, priority=i, execution_time=10, data=f"Test data {i}") for i in range(5)]

    def test_scheduler_priority(self):
        # Test if the scheduler adds and executes tasks based on priority
        for task in self.tasks:
            self.scheduler.add_task(task)
        self.scheduler.schedule_tasks()
        # Since tasks have different priorities, check if the scheduler is empty at the end
        self.assertTrue(not self.scheduler.tasks)

    def test_scheduler_edge_cases(self):
        # Test the scheduler with edge case tasks
        edge_tasks = [Task(task_id=999, priority=1, execution_time=0, data="Zero execution time"),
                      Task(task_id=1000, priority=1, execution_time=10, data="Large data", data_size=999999)]
        for task in edge_tasks:
            self.scheduler.add_task(task)
        self.scheduler.schedule_tasks()
        # Edge cases should be handled gracefully
        self.assertTrue(not self.scheduler.tasks)

if __name__ == '__main__':
    unittest.main()
