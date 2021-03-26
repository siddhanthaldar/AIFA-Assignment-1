from utils import create_graph, shortest_path

JSON_PATH = './graph.json'

graph = create_graph(JSON_PATH)
path = shortest_path(graph, (0,0), (graph['n']-1, graph['m']-1))
