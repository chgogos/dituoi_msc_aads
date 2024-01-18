from dataclasses import dataclass
from tabulate import tabulate


@dataclass
class Cell:
    cost: int
    parent: str

    def __lt__(self, other):
        return self.cost < other.cost

    def __repr__(self):
        if self.parent is None:
            return f"{self.cost}"
        else:
            return f"{self.cost},{self.parent}"


def print_table(m, p, t):
    """εκτύπωση πίνακα δυναμικού προγραμματισμού"""
    table = [[" "] * 3 + [c for c in t]]
    table.append([" "] * 3 + [str(i) for i in range(len(t))])
    for i, line in enumerate(m):
        if i == 0:
            table.append([" ", " "] + line)
        else:
            table.append([p[i - 1], i - 1] + line)
    print(tabulate(table))


def string_compare(p, t):
    # αρχικοποίηση πίνακα m |P|+1 x |T|+1
    m = [[Cell(cost=0, parent=None)] * (len(t) + 1) for _ in range(len(p) + 1)]
    for j in range(1, len(t) + 1):
        m[0][j] = Cell(cost=j, parent="I") # INSERT
    for i in range(1, len(p) + 1):
        m[i][0] = Cell(cost=i, parent="D") # DELETE
    for i in range(1, len(p) + 1):
        for j in range(1, len(t) + 1):
            if p[i - 1] == t[j - 1]:
                a = Cell(m[i - 1][j - 1].cost, "M")  # MATCH
            else:
                a = Cell(m[i - 1][j - 1].cost + 1, "S")  # SUBSTITUTION
            b = Cell(m[i][j - 1].cost + 1, "I")  # INSERT
            c = Cell(m[i - 1][j].cost + 1, "D")  # DELETE
            m[i][j] = min([a, b, c])
    return m


def reconstruct_path(p, t, i, j, m):
    if m[i][j].parent is None:
        return
    if m[i][j].parent in "MS":
        reconstruct_path(p, t, i - 1, j - 1, m)
        print(m[i][j].parent, end="")
        return
    if m[i][j].parent == "I":
        reconstruct_path(p, t, i, j - 1, m)
        print(m[i][j].parent, end="")
        return
    if m[i][j].parent == "D":
        reconstruct_path(p, t, i - 1, j, m)
        print(m[i][j].parent, end="")
        return


def reconstruct_path_wrapper(p, t, m):
    reconstruct_path(p, t, len(p), len(t), m)


if __name__ == "__main__":
    p = "thou-shalt"
    t = "you-should"
    m = string_compare(p, t)
    print_table(m, p, t)
    reconstruct_path_wrapper(p, t, m)
