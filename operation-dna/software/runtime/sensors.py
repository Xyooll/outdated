"""Passive sensing primitives; AI decides when and what to sense."""
from dataclasses import dataclass
from typing import Any, Callable
import time

@dataclass(frozen=True)
class Observation:
    source: str
    topic: str
    payload: Any
    observed_at: float

class Sensor:
    def __init__(self, name: str, reader: Callable[[], Any]):
        self.name, self.reader = name, reader

    def read(self, topic: str = "") -> Observation:
        return Observation(self.name, topic, self.reader(), time.time())

class SensorRegistry:
    def __init__(self): self._sensors: dict[str, Sensor] = {}
    def register(self, sensor: Sensor):
        if sensor.name in self._sensors: raise ValueError(f"sensor already registered: {sensor.name}")
        self._sensors[sensor.name] = sensor
    def catalog(self): return list(self._sensors)
    def read(self, name: str, topic: str = ""): return self._sensors[name].read(topic)
