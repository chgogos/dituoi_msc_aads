# λεξικό με κλειδιά αριθμούς κορυφών και τιμές πλειάδες με τις συντεταγμένες τους {1:(34816.6667,24100.0000), ...}
vertex_coords = {}

fn = "gr9882_10.tsp"

print("READ GRAPH DATA")
with open(fn) as f:
    # αγνόηση των 7 πρώτων γραμμών του αρχείου
    for _ in range(7):
        ignore = f.readline()
    for line in f:
        if line == "EOF\n":
            break
        vertex, x, y = line.split()
        vertex_coords[int(vertex)] = (float(x), float(y))

# δημιουργία adjacency list για το γράφο
print("CREATE EDGES")
k = 5
a_graph = {}  # adjacency list
# το a_graph είναι λεξικό με κλειδιά, τους αριθμούς κορυφών και τιμές, λίστες με πλειάδες τιμών (ζεύγη)
# κάθε ζεύγος τιμών διατηρεί πρώτα την απόσταση από την κορυφή κλειδί και μετά την κορυφή με την οποία συνδέεται απευθείας η κορυφή κλειδί
# π.χ. a_graph = {1:[(23.57020246943049, 2), (37.26778471790277, 4), (37.26778471790277, 5), (52.70463821040851, 6), (60.092502767732135, 3)], 2:[...], ...}
for vertex in vertex_coords:
    all_edges = []
    for other_vertex in vertex_coords:
        if vertex == other_vertex:
            continue
        distance = (
            (vertex_coords[vertex][0] - vertex_coords[other_vertex][0]) ** 2
            + (vertex_coords[vertex][1] - vertex_coords[other_vertex][1]) ** 2
        ) ** 0.5  # απόσταση ανάμεσα στις κορυφές vertex και other_vertex
        all_edges.append((distance, other_vertex))
    all_edges.sort()  # ταξινόμηση κορυφών κατά απόσταση (αυξουσα) από την vertex
    # διατήρηση των k κορυφών με τις μικρότερες αποστάσεις
    a_graph[vertex] = all_edges[:k]
    print(f"{vertex} -> {a_graph[vertex]}")


from graphviz import Digraph

# σχεδίαση του γράφου με το graphviz
print("DRAW GRAPH")
dot = Digraph(comment="hellas")
for vertex in vertex_coords:
    # dot.node(str(vertex), label=f'[{} {vertex_coords[vertex][0]:.1f}, {vertex_coords[vertex][1]:.1f}]')
    dot.node(str(vertex), label=f"{vertex}")

for vertex in a_graph:
    for distance, other_vertex in a_graph[vertex]:
        dot.edge(str(vertex), str(other_vertex), label=f"{distance:.1f}")

# print(dot.source)
dot.render("hellas.gv", view=True)

