# batching.py

"""
This script introduces a SelectiveBatching class that manages the execution of tasks in an efficient manner by 
selectively batching them based on certain criteria. The goal is to optimize processing throughput and resource 
efficiency by intelligently batching compatible tasks together.

The SelectiveBatching class handles the logic of creating and executing batches. Tasks are grouped into batches 
such that the total data size of tasks in a batch does not exceed the maximum batch size. In addition to size,
the type of task is considered to ensure that batches are homogeneous in terms of task processing requirements.

Attention operations, known for their computational intensity, are handled individually to prevent them from blocking 
the execution of non-attention tasks, following the ORCA paper's strategy for iteration-level task scheduling and 
selective batching.
"""

class Task:
    def __init__(self, task_type, data_size):
        self.task_type = task_type
        self.data_size = data_size

class SelectiveBatching:
    def __init__(self, max_batch_size=40):
        self.max_batch_size = max_batch_size
        self.batches = []

    def create_batch(self, tasks):
        """
        Organizes tasks into batches, where each batch contains tasks of the same type
        and the total data size does not exceed the max batch size. Attention tasks are
        kept separate to allow individual processing.
        """
        current_batch = []
        current_batch_size = 0
        current_batch_type = None

        for task in tasks:
            # Start a new batch if this task is a different type or size would be exceeded
            if (task.task_type != current_batch_type or 
                    current_batch_size + task.data_size > self.max_batch_size):
                
                if current_batch:
                    self.batches.append((current_batch_type, current_batch))
                
                current_batch = [task]
                current_batch_size = task.data_size
                current_batch_type = task.task_type
            else:
                current_batch.append(task)
                current_batch_size += task.data_size

        # Add the last batch if it's not empty
        if current_batch:
            self.batches.append((current_batch_type, current_batch))

    def test_homogeneous_batch_creation(self):
        # Test that batches contain only homogeneous tasks
        heterogeneous_tasks = [Task(task_id=i, task_type='type_A' if i % 2 == 0 else 'type_B', data_size=i) for i in range(1, 10)]
        self.batching.create_batch(heterogeneous_tasks)
        for batch_type, batch in self.batching.batches:
            self.assertTrue(all(task.task_type == batch_type for task in batch), f"All tasks in the batch should be of type {batch_type}")

    def test_batch_size_limit(self):
        # Test that no batch exceeds the maximum size limit
        tasks = [Task(task_id=i, task_type='data_processing', data_size=10) for i in range(20)]
        self.batching.create_batch(tasks)
        for _, batch in self.batching.batches:
            total_size = sum(task.data_size for task in batch)
            self.assertLessEqual(total_size, self.batching.max_batch_size, "Batch size should not exceed the maximum limit")

    def test_individual_attention_task_processing(self):
        # Test that attention tasks are executed individually
        tasks = [Task(task_id=i, task_type='attention', data_size=30) for i in range(5)]
        self.batching.create_batch(tasks)
        self.assertEqual(len(self.batching.batches), len(tasks), "Each attention task should be in its own batch")

    def execute_batches(self):
        """
        Execute each batch of tasks. Attention tasks are executed individually while 
        other task types are processed in batches.
        """
        for batch_type, batch in self.batches:
            if batch_type == "attention":
                # Attention tasks are executed individually
                for task in batch:
                    self.execute_task(task)
            else:
                # Non-attention tasks can be batch-processed
                self.process_batch(batch)

    def execute_task(self, task):
        """
        Simulate executing a single task. Actual implementation would involve complex
        logic and potentially asynchronous execution.
        """
        print(f"Executing {task.task_type} task with data size {task.data_size}.")

    def process_batch(self, batch):
        """
        Simulate batch processing of tasks. Actual implementation would depend on the 
        specifics of the tasks and could involve parallel computation frameworks.
        """
        print(f"Processing batch of {len(batch)} {batch[0].task_type} tasks.")

# Example usage
if __name__ == "__main__":
    # Define a list of tasks including both attention and non-attention types
    tasks = [
        Task("data_processing", 20), Task("model_inference", 10),
        Task("attention", 15), Task("model_inference", 5),
        Task("data_processing", 25), Task("attention", 30)
    ]

    # Instantiate the SelectiveBatching system and create batches
    batching_system = SelectiveBatching()
    batching_system.create_batch(tasks)

    # Execute the created batches
    batching_system.execute_batches()
