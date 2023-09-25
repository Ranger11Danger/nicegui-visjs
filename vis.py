from typing import Optional, Dict, List
from nicegui import ui

class VisNetwork(ui.element, component='vis.js'):
    def __init__(self, initial_data: Optional[Dict[str, List[Dict]]] = None) -> None:
        super().__init__()
        ui.add_head_html('<script src="https://unpkg.com/vis-data@8.6.0/dist/vis-data.min.js"></script>')
        ui.add_head_html('<script src="https://unpkg.com/vis-network@9.1.0/dist/vis-network.min.js"></script>')
        self._props['initialData'] = initial_data or {"nodes": [], "edges": []}
    def add_node(self, node: Dict) -> None:
        self.run_method('add_node', node)

    def delete_node(self, node_id: str) -> None:
        self.run_method('delete_node', node_id)

    def add_edge(self, edge: Dict) -> None:
        self.run_method('add_edge', edge)

    def delete_edge(self, edge_id: str) -> None:
        self.run_method('delete_edge', edge_id)
