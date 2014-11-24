import string

#convert text file into array of lines. 
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
			for each_string in new_edge:
				#print each_string
				if each_string == '\r\n':
					pass
				else:
					integer_rep = int(each_string)     #Make all vertex names and weights into integers 
					new_edge[new_edge.index(each_string)] = integer_rep
			line_formatted[line_formatted.index(edge)] = new_edge

		graph[int(line_formatted[0])] = line_formatted[1:]   #hashtable of keys = vertices, value = string of end vertices, weight
		graph_array.append(line_formatted[0])   #array of vertices
	return graph

graph = makeGraph("D_data.txt")

print graph
#print graph_array
print type(graph[1][1][0])
#print type(adj_matrix[0])
