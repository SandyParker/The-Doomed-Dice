def prob(a, A, B):
    occurrence = 0
    for i in A:
        for j in B:
            if a == i + j:
                occurrence += 1
    return occurrence


def printdice(A, B):
    for i in A:
        for j in B:
            print("{}{}".format(i, j), end=" ")
        print()
    print()


def check(A, B):
    s = posibilities(dice_A, dice_B)
    c = posibilities(A, B)
    return s, c


def posibilities(A, B):
    p = {}
    pos = list(range(2, 13))
    for i in pos:
        s = prob(i, A, B)
        p[i] = s
    return p


def undoom(dice_a, dice_b, t=0):
    A = list(dice_a)
    B = list(dice_b)
    for i in range(len(A)):
        if A[i] > 4:
            t += A[i] - 4
            A[i] = 4

    original_posibilities, new_posibilities = check(A, B)
    if (original_posibilities == new_posibilities) and t == 0:
        print("The undoomed dice are:\nDice A: {}\nDice B: {}".format(A, B))
    else:
        changed = False
        for i in range(12, 1, -1):
            if original_posibilities[i] > new_posibilities[i]:
                for k in range(6):
                    for j in range(6):
                        if A[j] + B[k] == i - 1 and not changed:
                            B[k] += 1
                            t -= 1
                            changed = True
                            break
            elif original_posibilities[i] < new_posibilities[i]:
                for j in range(6):
                    for k in range(6):
                        if A[j] + B[k] == i and not changed:
                            A[j] -= 1
                            t += 1
                            changed = True
                            break
            if changed:
                break
        undoom(A, B)


dice_A = [1, 2, 3, 4, 5, 6]
dice_B = [1, 2, 3, 4, 5, 6]
s = len(dice_A) * len(dice_B)
print("\n\t\t Part-A:")
print("Total combinations = Sum of possibilities of A X B = {} X {} = {}".format(len(dice_A),len(dice_B),s) , "\n")
printdice(dice_A,dice_B)
posi = posibilities(dice_A,dice_B)
for i in posi.keys():
    print("Probability of Sum {} = {}/{} = {}".format(i, posi[i], s, posi[i] / s))
print("\n\t\tPart-B:")
undoom(dice_A, dice_B)
