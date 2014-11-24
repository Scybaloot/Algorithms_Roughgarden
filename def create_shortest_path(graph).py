sample_hash = {"1":[["2","4"], ["3", "5"]], "2": [["1", "4"],["3", "6"], ["4", "1"]], "3": [["1", "5"], ["2", "6"],["4", "2"]], "4": [["2", "1"],["3", "2"]]}


def create_shortest_path(graph):
	shortest_path = 1000000
	seen_Array = [1]
	seen_graph = {1:0}
	unseen_Array = graph.keys()
	return unseen_Array

	#mainloop
	for vertext in seen_Array:
		edges = graph[vertex]
		print edges

#print 
create_shortest_path(sample_hash)
