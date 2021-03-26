from utils import *

JSON_PATH = './graph.json'
TASK_PATH = './task.txt'

graph = create_graph(JSON_PATH)
tasks = read_task(TASK_PATH) # [init, final, pickup, delivery]

optimal_paths = {}
for robot in tasks:
	optimal_paths[robot] = []
	for task in tasks[robot]:
		path1 = shortest_path(graph, task[0], task[1])
		path2 = shortest_path(graph, task[1], task[2])
		path3 = shortest_path(graph, task[2], task[3])
		path = path1 + path2 + path3
		optimal_paths[robot].append(path)


