sample_hash = {1:[[2,4], [3, 5]], 2: [[1, 4],[3, 6], [4, 1]], 3: [[1, 5], [2, 6],[4, 2]], 4: [[2, 1],[3, 2]]}


def create_shortest_path(graph):
	
	seen_Array = [1]
	shortest_paths = {1:0}
	unseen_Array = graph.keys()
	#return unseen_Array
	n = 0
	#mainloop
	while seen_Array != unseen_Array and n <40 :
		shortest_path = 1000000
		print "shortest paths hash: " , shortest_paths
		n +=1 
		for vertex in seen_Array:   #look at all combinations of v --> w
			print "vertex looked at: ", vertex
			edges = graph[vertex]
			for edge in edges:
				print "edge looked at: ", edge
				if edge[0] in unseen_Array:
					if edge[1] <= shortest_path:
						shortest_path = edge[1]
						print "the vertex: ", vertex
						closest_vertex_length = [edge[0], edge[1]+shortest_paths[vertex]]
						print "closest vertex and length" , closest_vertex_length
					else:
						pass
				else:
					pass

			#update any paths from closest vertex
			for edge in graph[closest_vertex_length[0]]:  #look at all edges coming out of closest vertex
				w = edge[0]
				l_w = edge[1]
				if w in shortest_paths:
					if closest_vertex_length[1] + l_w < shortest_paths[w]:
						shortest_paths[w] = (closest_vertex_length[1] + l_w)
					else:
						pass
				else:
					pass
		seen_Array.append(closest_vertex_length[0])  #add closest unseen to seen
		print "closest_vertex: " , closest_vertex_length[0]
		unseen_Array.remove(closest_vertex_length[0]) #remove from unseen   
		shortest_paths[closest_vertex_length[0]] = closest_vertex_length[1]

	return shortest_paths

		

#print 
print create_shortest_path(sample_hash)
