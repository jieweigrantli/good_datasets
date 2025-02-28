import json

import numpy as np

from .graph import graph_from_nlg

# Building a graph to use as a Network input

def build_graph(assets, lines, profiles, **kwargs):

    nodes = build_nodes(assets, profiles)

    graph = graph_from_nlg({'nodes': nodes, 'links': lines}, directed = True)

    return graph

def build_nodes(assets, profiles):

    # Getting unique regions
    regions = np.unique([p['region'] for p in assets])

    nodes = []

    for region in regions:

        node = {'id': region, '_class': 'Region'}

        # Adding assets
        node['assets'] = [p for p in assets if p['region'] == region]

        # Adding profiles
        node['profiles'] = (
            {k: v for k, v in profiles.items() if k.split(':')[0] == region}
            )

        nodes.append(node)

    return nodes