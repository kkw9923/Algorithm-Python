import networkx as nx

while True:

    sysInput = input()

    if sysInput == '0':
        break

    else:
        G = nx.DiGraph()
        edge_index = 0
        i_sysInput = int(sysInput)
        return_count = 0
        find_count = 0

        while i_sysInput > 0:
            node = input()
            node_check = node.split()
            for i in node_check:
                G.add_edge(edge_index, int(i))

            i_sysInput -= 1
            edge_index += 1

        if 0 not in G.nodes():
            print(0)

        else:    
            descend = list(nx.descendants(G,0))
            descend.append(0)
            
            for G_node in G.nodes():
                if G_node not in descend:
                    G.remove_node(G_node)

            
            path_dict = {}
            for node in nx.topological_sort(G):
                node_pairs = [(path_dict[v][0] + 1, v) for v in G.pred[node]]
                if node_pairs:
                    path_dict[node] = max(node_pairs)
                else:
                    path_dict[node] = (0, node)
            node, (length, _) = max(path_dict.items(), key=lambda l: l[1])
            path_list = []
            while length > 0:
                path_list.append(node)
                length, node = path_dict[node]
            longest_path = list(reversed(path_list))

            if len(longest_path) == 0:
                print(0)

            else:
                print(len(longest_path)-1)
