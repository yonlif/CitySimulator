
class Location:
    def __init__(self, lat: float, lon: float):
        self.lat = lat
        self.lon = lon

    def __repr__(self) -> str:
        return f"({self.lat}, {self.lon})"


def str_between(input_str: str, left: str, right: str) -> str:
    return input_str.split(left)[1].split(right)[0]
