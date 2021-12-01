'''Παράδειγμα αναδρομικού κώδικα αντίστροφης καταμέτρησης'''

def countdown(i):
    if i <= 0:
        print("Blastoff!")
    else:
        print(i)
        countdown(i - 1)
        
countdown(10)

# 10
# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1
# Blastoff!