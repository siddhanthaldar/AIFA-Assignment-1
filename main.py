from utils import *
from robot import Robot

JSON_PATH = './graph.json'
TASK_PATH = './task.txt'

graph = create_graph(JSON_PATH)
tasks = read_task(TASK_PATH) # [init, final, pickup, delivery]

# Find optimal path for each task
optimal_paths = {}
for robot in tasks:
	optimal_paths[robot] = []
	for task in tasks[robot]:
		path1 = shortest_path(graph, task[0], task[1])
		path2 = shortest_path(graph, task[1], task[2])
		path3 = shortest_path(graph, task[2], task[3])
		path = path1 + path2 + path3
		optimal_paths[robot].append(path)

# Tasks left per robots
tasks_left = {}
for robot in optimal_paths:
	tasks_left[robot] = len(optimal_paths[robot])

# List of robots
robots = []
for robot in optimal_paths:
	robots.append(Robot(name=robot, optimal_paths=optimal_paths[robot], tasks_left=tasks_left[robot]))

time = 0
# while(tasks_remaining(tasks_left)):
# 	points_occupied = {}
# 	for robot in optimal_paths:
