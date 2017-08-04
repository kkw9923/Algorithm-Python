"""
Exam Creation

This assignment will test your understanding of applying network flow to solve a constrained
selection problem. We want to decide if we have enough questions (in a database)
of a particular type and difficulty level to create a good exam to assess an algorithms
course.

Your teacher’s main goals, as designer, is to provide a range of difficulty (such as
Easy, Medium, Hard) and a diversity of topics (such as Brute Force, Divide and Conquer,
Dynamic Programming). For example, the exam should have a couple very easy questions
and should have at least one really hard question. At disposal is a database of questions
of various topics and difficulty levels. We have a requirement to (hopefully) pick a subset
of these questions to use as the composition of a final exam. Your task for this assignment
is to write a program that checks if we can fulfill the requirements for a good exam to
assess the class. If not, your teacher will be forced to develop a few new questions for the
database.


Sample input and output

Input

2
7 6
Easy Easy Medium Medium Hard Hard
Graphs Brute AdHoc Brute Geometry Math
SexyLife Brute Medium
BottomFeeder Graphs Hard
BadCase AdHoc Easy
Dominos Graphs Medium
Elephant Brute Hard
Flash Geometry Medium
Geography Math Easy
2 2
Easy Medium
Graph AdHoc
Funny AdHoc Medium
NotSoFun Graph Hard

Output

Yes
No




"""


# You need to install networkx
import networkx as nx



loop = int(input())

for i in range(loop):
    G = nx.DiGraph()

    
    noQ = input().split()

    noQ_DB = int(noQ[0])
    noQ_exam = int(noQ[1])

    G.add_node('s')
    G.add_node('t')
    

    diff = input().split()
    for j in diff:
        G.add_node(j)
        if j not in G.edge['s']:
            G.add_edge('s', j, capacity = 1)
        else:
            G.edge['s'][j]['capacity'] += 1


    topic = input().split()
    for k in topic:
        G.add_node(k)
        if 't' not in G.edge[k]:
            G.add_edge(k, 't', capacity = 1)
        else:
            G.edge[k]['t']['capacity'] += 1





    for l in range(noQ_DB):
        question = input().split()

        if question[2] in G.node:
            if question[1] in G.node:
                if question[1] not in G.edge[question[2]]:
                    G.add_edge(question[2], question[1], capacity = 1)
                else:
                    G.edge[question[2]][question[1]]['capacity'] += 1
            else:
                G.add_node(question[1])
                if question[1] not in G.edge[question[2]]:
                    G.add_edge(question[2], question[1], capacity = 1)
                else:
                    G.edge[question[2]][question[1]]['capacity'] += 1
        else:
            if question[1] in G.node:
                G.add_node(question[2])
                if question[1] not in G.edge[question[2]]:
                    G.add_edge(question[2], question[1], capacity = 1)
                else:
                    G.edge[question[2]][question[1]]['capacity'] += 1
            else:
                G.add_node(question[2])
                G.add_node(question[1])
                if question[1] not in G.edge[question[2]]:
                    G.add_edge(question[2], question[1], capacity = 1)
                else:
                    G.edge[question[2]][question[1]]['capacity'] += 1

        #print(G.edge,'edge')
                
            
    flow = nx.maximum_flow_value(G, 's', 't')
    #print(flow)


    #print(G.edge, 'EDGE')
    #print(G.node, 'NODE')



    if flow < noQ_exam:
        print('No')
    else:
        print('Yes')

