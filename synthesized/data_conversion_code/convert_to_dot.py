import os
from pathlib import Path
import json
from pogg.data_handling.pogg_dataset import POGGDataset
from pogg.data_handling.graph_util import POGGGraphUtil

pogg_dataset = POGGDataset("bitsybakery_dataset.yml")

graphs = []

for item in os.listdir(pogg_dataset.graph_json_dir):
    graph_json = json.load(open(os.path.join(pogg_dataset.graph_json_dir, item)))
    print(graph_json)

    graph_name = Path(item).stem
    print(graph_name)

    graph = POGGGraphUtil.build_graph(graph_json)
    POGGGraphUtil.write_graph_to_dot(graph, os.path.join(pogg_dataset.graph_dot_dir, f"{graph_name}.dot"))