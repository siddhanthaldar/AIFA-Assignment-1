from utils import shortest_path

class Robot:
	def __init__(self, name, optimal_paths, tasks_left, graph):

		self.name = name
		self.optimal_paths = optimal_paths
		self.tasks_left = tasks_left
		self.graph = graph
		self.task_idx = 0
		self.loc_idx = 0
		self.task_part_idx = 0
		# self.goal_idx = [self.optimal_paths[0][0][-1],self.optimal_paths[0][1][-1],self.optimal_paths[0][2][-1]]

		self.pos = (self.optimal_paths[0][0][0][0], self.optimal_paths[0][0][0][1])

		if len(self.optimal_paths)>1:
			self.add_path_to_new_tasks(graph)

		# Save goal indices
		self.goal_idx = []
		for i in range(len(optimal_paths)):
			goal = []
			for j in range(len(optimal_paths[i])):
				goal.append(self.optimal_paths[i][j][-1])
			self.goal_idx.append(goal)

	def add_path_to_new_tasks(self, graph):
		idx = 0
		while idx+1<len(self.optimal_paths):
			if self.optimal_paths[idx][-1][-1] != self.optimal_paths[idx+1][0][0]:
				path = shortest_path(graph, self.optimal_paths[idx][-1][-1], self.optimal_paths[idx+1][0][0])
				self.optimal_paths.insert(idx+1, [path])
				idx += 2
			else:
				idx += 1

	def reroute(self, new_loc):
		'''
		Reroute path if collision between multiple robots
		at task->self.task_idx and loc->self.loc_idx by ignoring
		collison block.
		(Take a step back, block current cell as other robot occupies it, 
		and find shortest path in the given scenario)
		'''
		
		new_path = shortest_path(self.graph, self.optimal_paths[self.task_idx][self.task_part_idx][self.loc_idx], self.goal_idx[self.task_idx][self.task_part_idx], addn_blocked = new_loc)
		self.optimal_paths[self.task_idx][self.task_part_idx] = self.optimal_paths[self.task_idx][self.task_part_idx][0:self.loc_idx] + new_path
