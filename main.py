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
		optimal_paths[robot].append([path1,path2,path3])

# List of robots
robots = []
for robot in optimal_paths:
	robots.append(Robot(name=robot, optimal_paths=optimal_paths[robot], tasks_left=len(optimal_paths[robot]), graph=graph))

while(tasks_remaining(robots)):
	loc = {} # Dict of (location, robot) to keep track of collisions
	for robot in robots:

		# Continue to next robot if all tasks for robot completed.
		if robot.task_idx == -1:
			continue
		
		if robot.loc_idx + 1 < len(robot.optimal_paths[robot.task_idx][robot.task_part_idx]): # Continue the same task
			robot.loc_idx = robot.loc_idx+1 # Go to next location
			new_loc = robot.optimal_paths[robot.task_idx][robot.task_part_idx][robot.loc_idx]

			# Collision occurs
			if new_loc in loc: 
				existing_robot = loc[new_loc]
				dist2end_existing = len(existing_robot.optimal_paths[existing_robot.task_idx][existing_robot.task_part_idx]) - existing_robot.loc_idx
				dist2end_new = len(robot.optimal_paths[robot.task_idx][robot.task_part_idx]) - robot.loc_idx

				# Letting the robot closer to the end of its task to go through
				if dist2end_existing <= dist2end_new: 
					while new_loc in loc:
						robot.loc_idx -=1
						if robot.loc_idx<0:
							robot.task_part_idx -=1 
						robot.reroute(new_loc)
						new_loc = robot.optimal_paths[robot.task_idx][robot.task_part_idx][robot.loc_idx]
				else:
					loc[new_loc] = robot
					while new_loc in loc:
						existing_robot.loc_idx -=1
						if existing_robot.loc_idx<0:
							existing_robot.task_part_idx -=1 
						existing_robot.reroute(new_loc)
						new_loc = existing_robot.optimal_paths[existing_robot.task_idx][existing_robot.task_part_idx][existing_robot.loc_idx]

			# If no collision
			else:
				# Add to dict only if not a TS. If TS, others can come in, so don't need to check for collisions.
				if new_loc not in graph['TS']:
					loc[robot.optimal_paths[robot.task_idx][robot.task_part_idx][robot.loc_idx]] = robot

		else: # Go to next task if that exists
			robot.task_part_idx+=1
			robot.loc_idx = 0
			
			if (len(robot.optimal_paths[robot.task_idx]) > 1 and robot.task_part_idx >= 3) or (len(robot.optimal_paths[robot.task_idx]) == 1 and robot.task_part_idx >= 1):
				robot.task_idx = (robot.task_idx+1) if ((robot.task_idx+1)<len(robot.optimal_paths)) else -1 # task id = -1 if all tasks completed
				robot.tasks_left -= 1
				robot.loc_idx = 0
				robot.task_part_idx = 0

for robot in robots:
	print("\n")
	print("------------------------------------------")
	print(robot.name)
	for idx, path in enumerate(robot.optimal_paths):
		print("Task",idx,"->", path)