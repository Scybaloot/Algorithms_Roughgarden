import string
import sys

sample_hash = {1:[[2,4], [3, 5], [5, 2]], 2: [[1, 4],[3, 6], [5, 1], [4, 1]], 3: [[1, 5], [2, 6],[4, 2]], 4: [[2, 1],[3, 2]], 5: [[1, 2],[2, 1]]}


def makeGraph(filename):
	graph_array = []
	graph = {}
	f = open(filename, 'r')
	for line in f:
		line_formatted = []
		line_formatted = line.split("\t")
		#line_formatted = line_formatted.split("\t")
		for edge in line_formatted[1:]:
			new_edge = edge.split(",")
			

			#something here!
			for each_string in new_edge:
				#print "new_edge is: " , new_edge
				#print each_string
				if each_string == '\r\n':   #not removing a blank element! hmmm
					#new_edge.remove(each_string)
					#line_formatted.pop()
					pass
				#elif each_string == "":
				#	new_edge.remove(each_string)
				else:
					integer_rep = int(each_string)     #Make all vertex names and weights into integers 
					new_edge[new_edge.index(each_string)] = integer_rep
			line_formatted[line_formatted.index(edge)] = new_edge

		graph[int(line_formatted[0])] = line_formatted[1:]   #hashtable of keys = vertices, value = string of end vertices, weight
		graph_array.append(line_formatted[0])   #array of vertices
	return graph

def create_shortest_path(graph):
	
	seen_Array = [1]
	shortest_paths = {1:0}
	unseen_Array = graph.keys()
	unseen_Array.remove(1)
	#return unseen_Array
	n = 0
	#mainloop
	while sum(seen_Array) != sum(graph.keys()) and len(unseen_Array) >0:
		#print "seen_Array ", seen_Array
		#print "unseen_Array ", unseen_Array
		shortest_path = 1000000
		#print "shortest paths hash: " , shortest_paths
		n +=1 
		for vertex in seen_Array:   #look at all combinations of v --> w
			#print "\n" , "vertex looked at: ", vertex 
			edges = graph[vertex]
			for edge in edges:

				#print "edge looked at: ", edge, "unseen_Array", unseen_Array
				if edge == "\r\n":
					pass
				elif edge[0] in unseen_Array:
					#print "type of graph[vertex] : ", type(graph[vertex])
					if edge[1] + shortest_paths[vertex] <= shortest_path:  #l_sv + l_vw
						shortest_path = edge[1] + shortest_paths[vertex]
						#print "the vertex: ", vertex
						closest_vertex_length = [edge[0], edge[1]+shortest_paths[vertex]]
						#print "closest vertex and length" , closest_vertex_length
					else:
						pass
				else:
					pass

			#new problem here with resetting closest values 
			#print "closest vertex: ", closest_vertex_length
			#update any paths from closest vertex
			for edge in graph[closest_vertex_length[0]]:  #look at all edges coming out of closest vertex
				#print "the edge in 75 is:  ", edge
				if edge[0] == "\r\n":
					pass
				else:
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
		#print "closest_vertex: " , closest_vertex_length[0]
		unseen_Array.remove(closest_vertex_length[0]) #remove from unseen   
		shortest_paths[closest_vertex_length[0]] = closest_vertex_length[1]

	return shortest_paths
 
graph = makeGraph("D_data.txt")
shortest_paths = create_shortest_path(graph)
print shortest_paths
print len(shortest_paths)

			#7,37,59,82,99,115,133,165,188,197

end_spots = [7,37,59,82,99,115,133,165,188,197]
print "spots"
for spot in end_spots:
	if spot in shortest_paths:
		print shortest_paths[spot]
		#sys.stdout.write(shortest_paths[spot])
	else:
		sys.stdout.write("1000000, ")







