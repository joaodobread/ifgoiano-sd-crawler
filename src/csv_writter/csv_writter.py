import uuid


class CSVWritter:
    def __init__(self, graph_node_file_name:  str, graph_edges_file_name:  str, links_with_refers: list, links: list):
        self.__graph_node_file_name = graph_node_file_name
        self.__graph_edges_file_name = graph_edges_file_name
        self.__links_with_refers = links_with_refers
        self.__links = links
        self.__pair_link_id = {}

    def __make_pair(self):
        for link in self.__links:
            self.__pair_link_id[link] = str(uuid.uuid4())
        return self.__pair_link_id

    def __write_graph_node(self):
        with open(self.__graph_node_file_name, 'w+') as graph_node_file:
            graph_node_file.write('ID, Label\n')
            for key in self.__pair_link_id.keys():
                graph_node_file.write(f"{self.__pair_link_id[key]}, {key}\n")

    def __write_graph_edges(self):
        with open(self.__graph_edges_file_name, 'w+') as graph_node_file:
            graph_node_file.write('Source, Target\n')
            for key in self.__links_with_refers:
                graph_node_file.write(
                    f"{self.__pair_link_id[key['link']]}, {self.__pair_link_id[key['refers_to']]}\n")

    def run(self):
        self.__make_pair()
        self.__write_graph_node()
        self.__write_graph_edges()
