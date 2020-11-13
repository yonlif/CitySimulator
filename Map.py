from tqdm import tqdm
from matplotlib.axes import Axes
from typing import List

from Drawable import Drawable
from Road import Road


class Map(Drawable):
    def __init__(self, roads: List[Road]):
        self.roads = roads

    def draw(self, ax: Axes):
        for road in tqdm(self.roads):
            road.draw(ax)
