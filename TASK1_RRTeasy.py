import cv2
import numpy as np
import matplotlib.pyplot as plt

class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.parent = None

class RRT:
    def __init__(self, start, goal, obstacles, x_limit, y_limit, step_size, max_iterations):
        self.start = Node(start[0], start[1])
        self.goal = Node(goal[0], goal[1])
        self.obstacles = obstacles
        self.x_limit = x_limit
        self.y_limit = y_limit
        self.step_size = step_size
        self.max_iterations = max_iterations
        self.nodes = []

    def generate_random_node(self):
        x = np.random.uniform(0, self.x_limit)
        y = np.random.uniform(0, self.y_limit)
        return Node(x, y)

    def find_nearest_node(self, node):
        distances = [np.sqrt((n.x - node.x) ** 2 + (n.y - node.y) ** 2) for n in self.nodes]
        nearest_idx = np.argmin(distances)
        return self.nodes[nearest_idx]

    def is_collision_free(self, node):
        for obstacle in self.obstacles:
            if obstacle[0] <= node.x <= obstacle[1] and obstacle[2] <= node.y <= obstacle[3]:
                return False
        return True

    def is_goal_reached(self, node):
        return np.sqrt((self.goal.x - node.x) ** 2 + (self.goal.y - node.y) ** 2) < self.step_size

    def steer(self, from_node, to_node):
        if np.sqrt((from_node.x - to_node.x) ** 2 + (from_node.y - to_node.y) ** 2) < self.step_size:
            return to_node
        else:
            theta = np.arctan2(to_node.y - from_node.y, to_node.x - from_node.x)
            x = from_node.x + self.step_size * np.cos(theta)
            y = from_node.y + self.step_size * np.sin(theta)
            return Node(x, y)

    def construct_path(self, node):
        path = [(node.x, node.y)]
        while node.parent is not None:
            node = node.parent
            path.append((node.x, node.y))
        path.reverse()
        return path

    def rrt(self):
        self.nodes.append(self.start)

        for _ in range(self.max_iterations):
            random_node = self.generate_random_node()
            nearest_node = self.find_nearest_node(random_node)
            new_node = self.steer(nearest_node, random_node)

            if self.is_collision_free(new_node):
                new_node.parent = nearest_node
                self.nodes.append(new_node)

                if self.is_goal_reached(new_node):
                    path = self.construct_path(new_node)
                    return path

        return None

    def plot(self, path=None):
        plt.figure()
        for obstacle in self.obstacles:
            rect = plt.Rectangle((obstacle[0], obstacle[2]), obstacle[1] - obstacle[0], obstacle[3] - obstacle[2], color='r')
            plt.gca().add_patch(rect)

        for node in self.nodes:
            if node.parent is not None:
                plt.plot([node.x, node.parent.x], [node.y, node.parent.y], 'b')

        plt.plot(self.start.x, self.start.y, 'bs', label='Start')
        plt.plot(self.goal.x, self.goal.y, 'gs', label='Goal')

        if path is not None:
            path_x, path_y = zip(*path)
            plt.plot(path_x, path_y, 'g')

        plt.xlim(0, self.x_limit)
        plt.ylim(0, self.y_limit)
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('RRT Path Planning on Maze')
        plt.legend()
        plt.grid(True)
        plt.show()

maze = cv2.imread('/Users/apple/Desktop/maze 3.png', cv2.IMREAD_GRAYSCALE)
maze2=maze[20:335,8:446]
maze_image=cv2.flip(maze2,0)
maze_image = cv2.threshold(maze_image, 127, 255, cv2.THRESH_BINARY)[1]
obstacles = []
for i in range(maze_image.shape[0]):
    for j in range(maze_image.shape[1]):
        if maze_image[i, j] == 0:  # Wall
            obstacles.append((j, j + 1, i, i + 1))

start = (27,0)
goal = (90,0)
x_limit = maze_image.shape[1]
y_limit = maze_image.shape[0]
step_size = 5
max_iterations = 15000

rrt_planner = RRT(start, goal, obstacles, x_limit, y_limit, step_size, max_iterations)
path = rrt_planner.rrt()
rrt_planner.plot(path)
