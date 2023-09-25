from nicegui import ui, Client
from nicegui.elements.progress import label
from vis import VisNetwork
@ui.page('/')
async def main_page(client: Client):
    # Create a Cytoscape component instance
    node_color = '#355E3B'
    initial_network_data = {
    "nodes": [
        {"id": 1, "label": "Node 1", 'color': node_color},
        {"id": 2, "label": "Node 2", 'color': node_color},
        {"id": 3, "label": "Node 3", 'color': node_color}
    ],
    "edges": [
        {"from": 1, "to": 2},
        {"from": 2, "to": 3}
    ]
}

    network = VisNetwork(initial_data=initial_network_data).classes('h-[50vh] w-full').style("background-color: #222222;")
    await client.connected()  # wait for websocket connection
    new_node = {"id": 4, "label": "Node 4", 'color': node_color}
    network.add_node(new_node)
    node_id = ui.input(label="Node Id")
    new_edge = {"from": 1, "to": 4}
    network.add_edge(new_edge)
    def add_node():
        data = {'id': node_id.value, 'label': f'Node {node_id.value}', 'color': node_color}
        network.add_node(data)
        node_id.value = ""
    ui.button("Add Node", on_click=add_node)
ui.run()
