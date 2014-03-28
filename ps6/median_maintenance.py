from Queue import PriorityQueue
import sys

def median_maintenance(num_stream):
    q_left = PriorityQueue()
    q_right = PriorityQueue()
    first = num_stream[0]
    second = num_stream[1]
    if first <= second:
        q_left.put(-first)
        q_right.put(second)
    else:
        q_left.put(-second)
        q_right.put(first)
    for num in num_stream[2:]:
        if num <= -q_left.queue[0]: 
            q_left.put(-num)
        else: 
            q_right.put(num)
        if abs(q_right.qsize() - q_left.qsize()) > 1:
            if q_left.qsize() > q_right.qsize(): 
                q_right.put(-q_left.get())
            else: 
                q_left.put(-q_right.get())
    return -q_left.queue[0], q_right.queue[0]

def main():
    with open(sys.argv[1], 'r') as f:
        lines = [ int(line) for line in f.readlines() ]
    print median_maintenance(lines)

if __name__ == '__main__':
    main()