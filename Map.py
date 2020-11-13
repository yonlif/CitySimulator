from typing import List

import matplotlib.pyplot as plt
from matplotlib.axes import Axes

from Drawable import Drawable
from Road import Road


class Map(Drawable):
    def __init__(self, roads: List[Road]):
        self.roads = roads

    def plot(self):
        fig, ax = plt.subplots()
        self.draw(ax)
        plt.show()

    def draw(self, ax: Axes):
        for road in self.roads:
            road.draw(ax)
