import sys
import pprint

# Globals party!!! This is like, the algorithm specification. Sry.
finish_order = []     
current_leader = None
leader_counts = {}

def compute_strong_components(graph, reversed_graph):
    """
    Kosaraju's algorithm for computing strongly connected components 
    in a directed graph.
    """
    global finish_order
    global leader_counts
    depth_first_search_loop(reversed_graph, 
                            iteration_order=range(1, len(reversed_graph) +1),
                            track_finish_order=True)
    finish_order.reverse()
    depth_first_search_loop(graph, 
                            iteration_order=finish_order,
                            track_leader=True)
    # Return size of the five largest SCCs
    return sorted(leader_counts.values(), reverse=True)[:5]
    
def depth_first_search_loop(graph, iteration_order, track_finish_order=False, track_leader=False):
    """Discover all vertices in a graph"""
    global current_leader
    for vertex in iteration_order:
        if graph[vertex]['explored'] is False:
            current_leader = vertex
            depth_first_search(graph, vertex, track_finish_order, track_leader)

def depth_first_search(graph, start_vertex, track_finish_order, track_leader):
    """Discover all discoverable vertices from a specified vertex"""
    global finish_order
    global current_leader
    # Have to do this iteratively or Python explodes, 
    # even after increasing recursion limit
    stack = [start_vertex]
    while len(stack):
        tail = stack.pop()
        if graph[tail]['explored'] is False:
            graph[tail]['explored'] = True
            if track_finish_order: finish_order.append(tail)
            if track_leader:
                if current_leader in leader_counts:
                    leader_counts[current_leader] += 1
                else:
                    leader_counts[current_leader] = 1
            for head in graph[tail]['data']:
                if graph[head]['explored'] is False: stack.append(head)

def build_graph(list):
    """Convert list of 2-item lists [tail, head] into dict-based representation of graph"""
    graph = {}
    for item in list:
        tail, head = int(item[0]), int(item[1])
        if not head in graph: 
            add_new_vertex(graph, head)
        if not tail in graph: 
            add_new_vertex(graph, tail, head)
        else: 
            graph[tail]['data'].append(head)
    return graph

def transpose_graph(graph):
    """Reverses arcs in a directed graph"""
    reversed_graph = {}
    for tail, data in graph.iteritems():
        if not tail in reversed_graph: 
            add_new_vertex(reversed_graph, tail)
        for head in data['data']:
            if head in reversed_graph: reversed_graph[head]['data'].append(tail)
            else: add_new_vertex(reversed_graph, head, tail)
    return reversed_graph

def add_new_vertex(graph, key, val=None):
    """Fn name says it all!"""
    graph[key] = {}
    graph[key]['explored'] = False
    graph[key]['data'] = [val] if val else []

def tests():
    graph = {
        1: {'data': [2,3], 'explored': False}, 
        2: {'data': [4],   'explored': False},
        3: {'data': [4],   'explored': False},
        4: {'data': [],    'explored': False}
    }
    reversed_graph_target = {
        1: {'data': [], 'explored': False}, 
        2: {'data': [1],   'explored': False},
        3: {'data': [1],   'explored': False},
        4: {'data': [2,3],    'explored': False}    
    }
    reversed_graph = transpose_graph(graph)
    assert reversed_graph == reversed_graph_target, 'Transposed graph should have arcs reversed'
    assert len(graph) is len(reversed_graph), 'Graph size remains the same after transposition'

def main():
    # Pass input file to script as cmd line arg
    with open(sys.argv[1], 'r') as f: 
        lines = f.readlines()
    # Split data into list of 2-item lists
    items = [ line.replace('\n', '').split(' ') for line in lines ]
    graph = build_graph(items)
    reversed_graph = transpose_graph(graph)
    compute_strong_components(graph, reversed_graph)
    
if __name__ == '__main__':
    # tests()
    main()