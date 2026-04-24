import heapq
class Node:
    def __init__(self, name):
        self.name = name
        self.neighbors = {}
        self.distance = float('inf')
        self.previous = None

    def add_neighbor(self, neighbor, weight):
        self.neighbors[neighbor] = weight


class Edge:
    def __init__(self, node1, node2, weight):
        self.node1 = node1
        self.node2 = node2
        self.weight = weight


class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, name):
        if name not in self.nodes:
            self.nodes[name] = Node(name)

    def add_edge(self, a, b, weight):
        self.add_node(a)
        self.add_node(b)
        self.nodes[a].add_neighbor(b, weight)
        self.nodes[b].add_neighbor(a, weight)

class Pathfinder:
    def __init__(self, graph):
        self.graph = graph

    def compute_shortest_path(self, start, goal):

        # set all distances to infinity
        for node in self.graph.nodes.values():
            node.distance = float('inf')
            node.previous = None

        self.graph.nodes[start].distance = 0

        pq = PriorityQueue()
        pq.push(0, start)

        #track nodes that have already been visited:
        visited = set()

        while not pq.is_empty():
            current_dist, current = pq.pop()

            if current in visited:
                continue
            visited.add(current)

            if current == goal:
                break

            # relaxes neighboring nodes to see if shorter route possible
            current_node = self.graph.nodes[current]
            for neighbor, weight in current_node.neighbors.items():

                new_dist = current_node.distance + weight

                # update if shorter distance is possible
                if new_dist < self.graph.nodes[neighbor].distance:
                    self.graph.nodes[neighbor].distance = new_dist
                    self.graph.nodes[neighbor].previous = current

                    pq.push(new_dist, neighbor)

        return self.reconstruct_path(goal)


    def reconstruct_path(self, goal):
        path = []
        node = self.graph.nodes[goal]

        while node:
            path.insert(0, node.name)  # insert at front of list
            node = self.graph.nodes[node.previous] if node.previous else None

        return path


class PriorityQueue:
    def __init__(self):
        self.heap = []

    def push(self, distance, node):
        heapq.heappush(self.heap, (distance, node))

    def pop(self):
        return heapq.heappop(self.heap)

    def is_empty(self):
        return len(self.heap) == 0




class Parser:
    def __init__(self, filename):
        self.filename = filename

    def load_graph(self):
        graph = Graph()
        with open(self.filename, "r") as f:
            for line in f:
                a, b, w = line.split()
                graph.add_edge(a, b, int(w))
        return graph

def main():
    #
    filename = "Inputfile.txt"   #input file
    parser = Parser(filename)
    graph = parser.load_graph()


    start = input("Enter start node: ").strip().upper()
    end = input("Enter destination node: ").strip().upper()


    pathfinder = Pathfinder(graph)
    path = pathfinder.compute_shortest_path(start, end)
    # here
    total_distance = graph.nodes[end].distance


    print("\nShortest path:")
    print("→".join(path))
    print(f"Total distance: {total_distance}")

if __name__ == "__main__":
    main()