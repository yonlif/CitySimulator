import pandas as pd
from pathlib import Path

from Map import Map
from Road import Road
from paths import NYC_DATA_PATH


def load_map(path: Path):
    map_df = pd.read_csv(path, usecols=['the_geom'])
    print(f"Read dataframe of shape {map_df.shape}")
    roads = []
    for road in map_df['the_geom']:
        roads.append(Road.load_from_linestring(road))
    return Map(roads)


if __name__ == '__main__':
    map = load_map(NYC_DATA_PATH)
    map.plot()
