import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
    #  创建一个RandomWalk的实例
    rw = RandomWalk()
    rw.fill_walk()
    points_numbers = list(range(rw.num_points))

    plt.scatter(rw.x_values, rw.y_values, s=15)

    plt.show()
    keep_running = input("Go:")
    if keep_running == 'n' or keep_running == 'N':
        break
