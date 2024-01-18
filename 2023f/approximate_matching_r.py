def string_compare_r(p, t, i, j):
    """ελάχιστος αριθμός αλλαγών στο p για να γίνει t"""
    if i == 0:
        return j
    if j == 0:
        return i

    if p[i] == t[j]:        
        match_cost = string_compare_r(p, t, i - 1, j - 1) 
    else:
        match_cost = string_compare_r(p, t, i - 1, j - 1) + 1
    insert_cost = string_compare_r(p, t, i, j - 1) + 1
    delete_cost = string_compare_r(p, t, i - 1, j) + 1

    return min([match_cost, insert_cost, delete_cost])

def string_compare_r_wrapper(p, t):
    p = " " + p # για την περίπτωση που p[0] != t[0]
    t = " " + t # για την περίπτωση που p[0] != t[0]
    return string_compare_r(p, t, len(p) - 1, len(t) - 1)

if __name__ == "__main__":
    p = "thou-shalt"
    t = "you-should"
    print(string_compare_r_wrapper(p, t))
    
    p = "ABBC"
    t = "AXB"
    cost = string_compare_r(p, t, len(p)-1, len(t)-1)
    print(cost)