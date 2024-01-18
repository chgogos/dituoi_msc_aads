from ortools.algorithms.python import knapsack_solver

def main():
    n = 4  # πλήθος αντικειμένων
    v = [3, 2, 4, 4] # αξίες αντικειμένων
    w = [4, 3, 2, 3] # βάρη αντικειμένων
    C = 6  # χωρητικότητα

    # Create the solver.
    solver = knapsack_solver.KnapsackSolver(
        knapsack_solver.SolverType.KNAPSACK_MULTIDIMENSION_BRANCH_AND_BOUND_SOLVER,
        "KnapsackExample",
    )
    solver.init(v, [w], [C])
    computed_value = solver.solve()

    packed_items = []
    packed_weights = []
    total_weight = 0
    print("Total value =", computed_value)
    for i in range(n):
        if solver.best_solution_contains(i):
            packed_items.append(i+1)
            packed_weights.append(w[i])
            total_weight += w[i]
    print("Total weight:", total_weight)
    print("Packed items:", packed_items)
    print("Packed_weights:", packed_weights)


if __name__ == "__main__":
    main()