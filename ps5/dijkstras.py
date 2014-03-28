import sys
import pdb

def dijkstras(graph, source_v):
    """Find shortest paths between source vertex and all vertices in graph."""
    graph_v = graph.keys()
    processed_v = [source_v]
    shortest_times = [None] * (len(graph) + 1)
    shortest_times[source_v] = 0        
    
    def compute_min(processed, graph):
        cur_min = (None, float("inf")) # Vertex, Dijkstra's greedy score
        for v in processed:
            filtered = [item for item in graph[v] if item['adj_vertex'] not in processed]
            for item in filtered:
                greedy_score = item['weight'] + shortest_times[v]
                if greedy_score < cur_min[1]:
                    cur_min = item['adj_vertex'], greedy_score
        return cur_min

    while set(processed_v) != set(graph_v):
        min_v = compute_min(processed_v, graph)
        processed_v.append(min_v[0])
        shortest_times[min_v[0]] = min_v[1]
    # These arbitrary return values are what the hwk wants
    x=shortest_times
    return x[7],x[37],x[59],x[82],x[99],x[115],x[133],x[165],x[188],x[197]


def build_graph(lines):
    # Note: course-provided test input files formatted differently (!) so to 
    # get correct result first strip trailing tabs on the main input file
    return { int(v_set[0]): [ make_adj_v(v) 
        for v in v_set[1].split('\t') ] 
        for v_set in [ parse_vs(line) for line in lines ] 
    }

def parse_vs(line): 
    return line.replace('\n', '').replace('\r', '').split('\t', 1)

def make_adj_v(v): 
    return { 'adj_vertex': int(v.split(',')[0]), 'weight': int(v.split(',')[1]) }

def main():
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()
    graph = build_graph(lines)
    print dijkstras(graph, 1)

if __name__ == '__main__':
    main()