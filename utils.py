import json
import numpy as np

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

def shortest_path(graph, start, goal):
	n, m = graph['n'], graph['m']

	# Set of visited points
	vis = set()

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