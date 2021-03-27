from utils import shortest_path

class Robot:
	def __init__(self, name, optimal_paths, tasks_left, graph):

		self.name = name
		self.optimal_paths = optimal_paths
		self.tasks_left = tasks_left
		self.graph = graph
		self.task_idx = 0
		self.loc_idx = 0

		self.pos = (self.optimal_paths[0][0][0], self.optimal_paths[0][0][1])

		if len(self.optimal_paths)>1:
			self.add_path_to_new_tasks(graph)

	def add_path_to_new_tasks(graph):
		idx = 0
		while idx+1<len(self.optimal_paths):
			if self.optimal_paths[idx][-1] != self.optimal_paths[idx+1][0]:
				path = shortest_path(graph, self.optimal_paths[idx][-1], self.optimal_paths[idx+1][0])
				self.optimal_paths.insert(idx+1, path)
				idx += 2
			else:
				idx += 1

	def reroute():
		'''
		Reroute path if collision between multiple robots
		at task->self.task_idx and loc->self.loc_idx by ignoring
		collison block.
		'''
		pass