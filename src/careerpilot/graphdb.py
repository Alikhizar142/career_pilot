from __future__ import annotations

from dataclasses import dataclass


@dataclass
class GraphDBClient:
    url: str = "http://localhost:7200"
    repository: str = "careerpilot"
    username: str = ""
    password: str = ""

    def ping(self) -> bool:
        return bool(self.url)

    def query(self, sparql: str) -> list[dict]:
        if not sparql:
            return []
        return [{"query": sparql, "status": "simulated"}]
