import networkx as nx
while True:

    sysInput = input()
    
    if sysInput == '0':
        break
        
    else:
        G = nx.Graph()
        edge_index = 0
        i_sysInput = int(sysInput)
        
        while i_sysInput > 0:
            node = input()
            node_check = node.split()
            if len(node_check) == 0:
                G.add_edge(edge_index,edge_index)
            for i in node_check:
                G.add_edge(edge_index,int(i))

            i_sysInput -= 1
            edge_index += 1


        print(nx.number_connected_components(G))


    
