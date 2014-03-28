import sys
import random

def random_contraction(adj_list):
    """
    Repeatedly pick a random edge in an adjacency list and merge the two 
    adjacent nodes until two nodes remain. Then return minimum cut length.
    """
    while (len(adj_list) > 2):
        # First pick a random edge, represented by two nodes
        node_a = random.choice(adj_list.keys())
        node_b = random.choice(adj_list[node_a])
        # In a's values, remove references to b
        adj_list[node_a] = filter(lambda x: x != node_b, adj_list[node_a])
        # Merge b's values into a's
        adj_list[node_a] += adj_list[node_b]
        # Iterate through all b was connected to, replace refs to b with a
        for key in adj_list[node_b]:
            adj_list[key] = [ node_a if x == node_b else x for x in adj_list[key] ]
        # Remove any self loops created in a
        adj_list[node_a] = filter(lambda x: x != node_a, adj_list[node_a])
        del adj_list[node_b]
    # Grab one of two remaining dictionary items, who cares which!
    _, min_cut = adj_list.popitem()
    return len(min_cut)

def tests():
    adj_list = {'1': ['2', '3', '4'], 
                '2': ['1', '4'],
                '3': ['1', '4'],    
                '4': ['1','2','3']}
    random_contraction(adj_list)

def main():
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()
    # Split lines on tabs, put nodes in dictionary where key=node, value=adj list
    items = { item[0]: item[1:-1] for item in [ line.split('\t') for line in lines ] }
    print random_contraction(items)

if __name__ == '__main__':
    tests()
    main()