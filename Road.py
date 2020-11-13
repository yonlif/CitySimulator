from matplotlib.axes import Axes
from typing import List

from Drawable import Drawable
from utils import Location, str_between


class Road(Drawable):
    def __init__(self, locations: List[Location]):
        self.locations = locations

    @classmethod
    def load_from_linestring(cls, linestring: str) -> "Road":
        linestring = str_between(linestring, '(', ')')
        linestring_spited = linestring.split(', ')
        locations = []
        for item in linestring_spited:
            lat, lon = item.split()
            locations.append(Location(float(lat), float(lon)))
        return Road(locations)

    def draw(self, ax: Axes):
        for first_loc, second_loc in zip(self.locations, self.locations[1:]):
            ax.plot([first_loc.lat, second_loc.lat], [first_loc.lon, second_loc.lon], c='blue')

    def __repr__(self) -> str:
        return "Road " + " ".join([str(loc) for loc in self.locations])
