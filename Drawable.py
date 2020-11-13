import matplotlib.pyplot as plt
from matplotlib.axes import Axes


class Drawable:
    def plot(self):
        """
        Create and display matplotlib plot
        """
        raise NotImplementedError

    def draw(self, ax: Axes):
        """
        Given an axis - draw the item on the axis
        """
        raise NotImplementedError


if __name__ == '__main__':
    fig, my_ax = plt.subplots()
    x1, y1 = [-1, 12], [1, 4]
    x2, y2 = [1, 10], [3, 2]
    my_ax.plot(x1, y1, x2, y2, marker='o')
    plt.show()
