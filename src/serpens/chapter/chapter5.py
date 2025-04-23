from typing import NamedTuple


class Coordinate:
    def __init__(self, lat, lon) -> None:
        self.lat = lat
        self.lon = lon


class Coordinate3(NamedTuple):
    lat: float
    lon: float

    def __str__(self) -> str:
        ns = "N" if self.lat >= 0 else "S"
        we = "E" if self.lon >= 0 else "W"
        return f"{abs(self.lat):.1f}°{ns}, {abs(self.lon):.1f}°{we}"
