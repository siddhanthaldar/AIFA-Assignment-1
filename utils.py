import json

def create_graph(json_path):
	'''
	Return graph in the form of a dictionary
	'''
	graph = {}

	f = open(json_path, 'r')
	data = json.load(f)

	graph['n'] = data['n']
	graph['m'] = data['m']

	graph['blocked'] = set()
	for indices in data['blocked']:
		graph['blocked'].add(tuple(indices))

	graph['TS'] = set()
	for indices in data['TS']:
		graph['TS'].add(tuple(indices))

	f.close()

	return graph

def read_task(txt_path):
	'''
	Return dict of tasks
	'''
	f = open(txt_path, 'r')
	data = f.read().split()

	tasks = {}
	for line in data:
		line = line.split(',')
		if line[0] not in tasks:
			tasks[line[0]] = []
		init = tuple([int(line[1]), int(line[2])])
		final = tuple([int(line[3]), int(line[4])])
		pickup = tuple([int(line[5]), int(line[6])])
		delivery = tuple([int(line[7]), int(line[8])])
		tasks[line[0]].append([init, pickup, delivery, final])

	return tasks

def shortest_path(graph, start, goal, addn_blocked = None):
	n, m = graph['n'], graph['m']

	# Set of visited points
	vis = set()
	if addn_blocked != None: vis.add(addn_blocked)

	# dict to store parents
	par = {}

	# Create queue for BFS
	queue = []

	queue.append(start)

	while queue:
		s = queue.pop(0)

		# If s has been visited before, continue
		if s in vis or s in graph['blocked']:
			continue

		# If goal reached, return path  
		if s[0]==goal[0] and s[1]==goal[1]:
			path = [goal]
			while s != start:
				path.append(par[s])
				s = par[s]
			path.reverse()
			return path

		# Add s to visited set
		vis.add(s)

		# Visit neighbours of s
		if (s[0]+1)<n and (s[0]+1)>=0:
			queue.append((s[0]+1, s[1]))
			if (s[0]+1, s[1]) not in par:
				par[(s[0]+1, s[1])] = s
		if (s[0]-1)<n and (s[0]-1)>=0:
			queue.append((s[0]-1, s[1]))
			if (s[0]-1, s[1]) not in par:
				par[(s[0]-1, s[1])] = s
		if (s[1]+1)<m and (s[1]+1)>=0:
			queue.append((s[0], s[1]+1))
			if (s[0], s[1]+1) not in par:
				par[(s[0], s[1]+1)] = s
		if (s[1]-1)<m and (s[1]-1)>=0:
			queue.append((s[0], s[1]-1))
			if (s[0], s[1]-1) not in par:
				par[(s[0], s[1]-1)] = s


def tasks_remaining(robots):
	'''
	Returning if any task remaining or not

	Input : 
		list of robot objects

	Output : 
		True -> Task remaining
		False -> Tasks over
	'''

	for robot in robots:
		if robot.task_idx < len(robot.optimal_paths) and (robot.task_idx!=-1):
			return True
	return False
