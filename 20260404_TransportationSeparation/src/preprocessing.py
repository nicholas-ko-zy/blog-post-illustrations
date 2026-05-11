import osmnx as ox
import pickle

def network_to_gdf(ox_network):
    network_nodes, network_edges = ox.graph_to_gdfs(ox_network)
    network_nodes = network_nodes.reset_index()
    network_edges = network_edges.reset_index()
    return network_nodes, network_edges

def gdf_to_line_string_list(network_edges):
    line_strings = [line_strings for line_strings in network_edges['geometry']]
    return line_strings

def polygon_to_gdf(polygon, network_type):
    network = ox.graph.graph_from_polygon(polygon, network_type=network_type)
    network_nodes, network_edges = network_to_gdf(network)
    return network_nodes, network_edges

def place_to_gdf(place_name, network_type):
    network = ox.graph.graph_from_place(place_name, network_type=network_type)
    network_nodes, network_edges = network_to_gdf(network)
    return network_nodes, network_edges

def polygon_to_line_string(polygon, network_type):
    # For Singapore use
    network_nodes, network_edges = polygon_to_gdf(polygon, network_type)
    line_strings = gdf_to_line_string_list(network_edges)
    return line_strings

def place_to_line_string(place_name, network_type):
    # For Netherlands use
    network_nodes, network_edges = place_to_gdf(place_name, network_type)
    line_strings = gdf_to_line_string_list(network_edges)
    return line_strings

def pickle_object(object, fp):
    with open(fp, "wb") as fp:
        pickle.dump(object, fp)

def load_pickle_file(fp):
    with open(fp, "rb") as fp:
        pickled_file = pickle.load(fp)
    return pickled_file