import numpy as np

def moveHead(H,direction):
    if direction == 'R':
        H[0] += 1
    elif direction == 'L':
        H[0] -= 1
    elif direction == 'U':
        H[1] += 1
    elif direction == 'D':
        H[1] -= 1
    return H

def moveTail(H,T):
    HT_dist = H-T

    # Check if distance between H & T is larger than 2 in x-dir. If so, move T towards H
    if abs(HT_dist[0])>1:
        T[0] = T[0] +1*np.sign(HT_dist[0])
        # If T moves in x-dir, it should also move to the same y-pos as H
        if HT_dist[1] != 0:
            T[1] = H[1]
    
    # Check if distance between H & T is larger than 2 in y-dir. If so, move T towards H
    if abs(HT_dist[1])>1:
        T[1] = T[1] +1*np.sign(HT_dist[1])
        # If T moves in y-dir, it should also move to the same y-pos as H
        if HT_dist[0] != 0:
            T[0] = H[0]
    
    return T

filePath = 'Day09/moveOrders.txt'
# filePath = 'Day09/moveOrdersEx.txt'

H = np.array([0,0])
T = np.array([0,0])

T_hist = []

with open(filePath) as f:
    mylist = f.read().splitlines()

    for row in mylist:
        [direction, steps] = row.split(' ')

        for i in range(int(steps)):
            H = moveHead(H,direction)
        
            T = moveTail(H,T)
            
            T_hist.append(F"{T[0]},{T[1]}")

T_set = set(T_hist)
print(f"Number of places visited by Tail:{len(T_set)}")
        