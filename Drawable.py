import matplotlib.pyplot as plt
from matplotlib.axes import Axes


class Drawable:
    def plot(self):
        """
        Create and display matplotlib plot
        """
        _, ax = plt.subplots()
        self.draw(ax)
        plt.show()

    def draw(self, ax: Axes):
        """
        Given an axis - draw the item on the axis
        """
        raise NotImplementedError
