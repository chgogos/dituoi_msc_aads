'''Παράδειγμα αναδρομικού κώδικα αντίστροφης καταμέτρησης'''

def countdown(i):
    if i <= 0:
        print("Blastoff!")
    else:
        print(i)
        countdown(i - 1)
        
countdown(10)