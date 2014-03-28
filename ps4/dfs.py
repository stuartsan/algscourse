import sys
import pprint

def depth_first_search(graph, start_vertex):
    """Discover all discoverable vertices from a specified vertex"""
    # Mark start vertex as explored
    graph[start_vertex]['explored'] = True
    # Explore each unexplored vertex in adjacency list
    for vertex in graph[start_vertex]['data']:
        if graph[vertex]['explored'] is False: 
            depth_first_search(graph, vertex)

def depth_first_search_loop(graph):
    """Discover all vertices in a graph"""
    for vertex in graph:
        if graph[vertex]['explored'] is False: 
            depth_first_search(graph, vertex)

def main():
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()
    # Split data into list of 2-item lists
    items = [ line.replace('\n', '').split(' ') for line in lines ]
    graph = {}
    # Each item is [tail, head]
    for item in items:
        tail, head = item[0], item[1]
        if not tail in graph:
            graph[tail] = {}
            graph[tail]['data'] = [head]
            graph[tail]['explored'] = False
        else:
            graph[tail]['data'].append(head)    
    depth_first_search_loop(graph)
    # Eyeball result
    # pp = pprint.PrettyPrinter()
    # pp.pprint(graph)

if __name__ == '__main__':
    main()