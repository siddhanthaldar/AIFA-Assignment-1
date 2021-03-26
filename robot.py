class Robot:
	def __init__(self, name, optimal_paths, tasks_left):

		self.name = name
		self.optimal_paths = optimal_paths
		self.tasks_left = tasks_left
		self.task_idx = 0