import sys
import pandas as pd
import numpy as np

def inputZ():
    print(f'Simplex Method:\t[ Z = ax1 + bx2 + cx3 ]')
    try:
        A1 = list(map(int, input("\nEnter Value of a, b, c, Z : ").strip().split()))[:4]
    except ValueError:
        sys.exit("This is not a number.")
    return StandardForm(A1)

def StandardForm(A):
    n = len(A)
    result = A
    if A[n-1] < 0:
        result[n-1] *= -1 #= [i * -1 for i in A]
    else:
        result = [i * -1 for i in A]
        result[n - 1] *= -1
    n = A[n-1]
    if n > 1:
        result = [i/n for i in A]
    return result

def Constrs():
    print(f'Constraints : [ ax1 + bx2 + cx3 >= d ]')
    while True:
        constr = input(f'Enter number of constraints : ').strip()
        if constr.isdigit():
            constr = int(constr)
            if constr > 0:
                break
            else:
                print(f'Enter a number greater than zero')
        else:
            print(f'Enter a number.')
    C = [[]] * constr
    print("\nEnter Value of a, b, c, d : ")
    for i in range(0, constr):
        try:
            C[i] = list(map(int, input().strip().split()))[:4]
        except ValueError:
            sys.exit("This is not a number.")
    return C

def Tableau(A, C):
    A.pop(len(A) - 1)
    t = []
    for i in range(0, len(C)):
        A.append(0)
        t.append(0)
    t[0] = 1
    t.append(0)
    A.append(1)
    A.append(0)
    for i in range(0, len(C)):
        temp = C[i].pop()
        C[i].extend(t)
        C[i].append(temp)
        t = t[-1:] + t[:-1]
    X = []
    X.append(A)
    X.extend(C)
    return X
def CheckOptimality(df):
    X = df.head(1)
    print(X)
    for i in range(len(X)):
        if df.loc[i] < 0:
            return False
    return True

if __name__ == '__main__':
    A = inputZ() # Iput Standar for of Z
    C = Constrs() # Input Constraints
    X = Tableau(A, C) # Make Tableau
    df = pd.DataFrame(X)
    print(df)
    flag = CheckOptimality(df)
    print(flag)

