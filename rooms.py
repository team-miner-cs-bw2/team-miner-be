import json
from utils.queue_stack import Queue, Stack

class Graph:

    """Represent a graph as a dictionary of rooms mapping labels to doors."""

    def __init__(self):
        self.rooms = {}
        self.vertices = {}

    def load_graph(self, filename):
        """
        Load graph from file.
        """
        try:
            with open(filename) as json_file:
                data = json.load(json_file)
                print(len(data))
                for room in data:
                    self.add_room(data[room], from_file=True)
        except IOError as e:
            print(e)
        finally:
            print("Graph loaded successfully!")

    def add_room(self, room, from_file=False):
        """
        Add a room to the graph.
        """
        if from_file:
            self.rooms[room["room_id"]] = room
            self.vertices[room["room_id"]] = set(
                [room_id for room_id in room["exits"].values()])
        elif room["room_id"] not in self.rooms:
            self.rooms[room["room_id"]] = room
            self.rooms[room["room_id"]]["exits"] = {
                x: '?' for x in room["exits"]}
            self.vertices[room["room_id"]] = set()

        return room

    def get_room(self, room_id):
        """
        Get a room from the graph.
        """
        if room_id in self.rooms:
            return self.rooms[room_id]

        return None

    def connect_rooms(self, room1_id, room2_id, direction):
        """
        Add a directed edge to the graph.
        """
        reverse_dir = {'n': 's', 'e': 'w', 's': 'n', 'w': 'e'}[direction]

        if room1_id in self.rooms and room2_id in self.rooms:
            self.rooms[room1_id]["exits"][direction] = room2_id
            self.rooms[room2_id]["exits"][reverse_dir] = room1_id
            self.vertices[room1_id].add(room2_id)
            self.vertices[room2_id].add(room1_id)
        else:
            raise IndexError("That room does not exist.")

    def get_connected_rooms(self, room_id, visited=False):
        """
        Get exits from a room.
        """
        if visited:  # return only previously visited neighboring rooms
            return [exit for exit in self.rooms[room_id]["exits"] if self.rooms[room_id]["exits"][exit] != '?']
        # return unvisited neighboring rooms
        return [exit for exit in self.rooms[room_id]["exits"] if self.rooms[room_id]["exits"][exit] == '?']

    def path_to_directions(self, path):
        traversal = []
        current_room = path.pop(0)
        while len(path) > 0:
            next_room = path.pop(0)
            reverse_keys = {value: key for key,
                            value in self.rooms[current_room]["exits"].items()}
            traversal.append((reverse_keys[next_room], next_room))
            current_room = next_room
        return traversal

    def explore_bfs(self, starting_room):
        """
        Return a list containing the shortest path from
        starting_room to unexplored room.
        """

        # Create an empty queue and enqueue the starting room ID
        q = Queue()
        q.enqueue([starting_room])

        # Create an empty Set to store visited rooms
        visited = set()

        # While the queue is not empty...
        while q.size():
            # Dequeue the first path
            path = q.dequeue()
            # Look at the last room in the path...
            current_room = path[-1]
            # And if we've found a room with an unopened door, return our path to that room
            if '?' in self.rooms[current_room]["exits"].values():
                # Return path as directions
                return self.path_to_directions(path)

            # If the room has not been visited
            if current_room not in visited:
                # Mark it as visited
                visited.add(current_room)
                # Add a path to each room to the queue
                for room in self.get_connected_rooms(current_room, visited=True):
                    new_path = path.copy()
                    new_path.append(self.rooms[current_room]["exits"][room])
                    q.enqueue(new_path)

        return None

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """

        # Create an empty stack and push the starting vertex ID
        s = Stack()
        s.push(starting_vertex)

        # Create a Set to store visited vertices
        visited = set()
        path = []

        # While the stack is not empty...
        while s.size():
            # Pop the first vertex
            v = s.pop()
            # If that vertex has not been visited...
            if v not in visited:
                # Mark it as visited...
                # print(v)
                if len(path):
                    path += self.bfs(path[-1], v)[1:]
                else:
                    path.append(v)
                visited.add(v)
                # Then add all of its neighbors to the top of the stack
                # neighbors = list(self.get_neighbors(v))
                # random.shuffle(neighbors)
                for neighbor in self.get_neighbors(v):
                    s.push(neighbor)

        return self.path_to_directions(path)
        # return path

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """

        # Create an empty queue and enqueue the starting vertex ID
        q = Queue()
        q.enqueue([starting_vertex])

        # Create an empty Set to store visited vertices
        visited = set()

        # While the queue is not empty...
        while q.size():
            # Dequeue the first path
            path = q.dequeue()
            # Look at the last vertex in the path...
            current_vertex = path[-1]
            # And if it is the current vertex, we're done searching
            if current_vertex == destination_vertex:
                return self.path_to_directions(path)

            # print(current_vertex, visited)
            # If the vertex has not been visited
            if current_vertex not in visited:
                # Mark it as visited
                visited.add(current_vertex)
                # Add a path to each neighbor to the queue
                for neighbor in self.get_neighbors(current_vertex):
                    new_path = path.copy()
                    new_path.append(neighbor)
                    q.enqueue(new_path)

        return None



graph = Graph()


# TEST FILE LOADING
graph.load_graph('map.json')