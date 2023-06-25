'''
Question:
You have an array(A) of N integers where ith(0 <= i < N) index value denote the country NO of the ith person (O <= A[i] <= 1e9.
You have another array(B) which denotes the skill of the ith person.
You have to update the array B, such that B[i] = B[i]-X, where X = floor(Average skill of the country) where the ith person belongs.
You have to print the new array.
'''

def main(a,b):
    cont = {}
    cont_count ={}
    for i,v in enumerate(a):
        if v in cont.keys():
            cont[v] = (cont[v])+int(b[i])
            cont_count[v] = cont_count[v]+1
        else:
            cont[v] = int(b[i])
            cont_count[v]=1

    cont_avg = {}
    for i in cont.keys():
        cont_avg[i] = cont[i]//cont_count[i]

    deduct_b = []
    for i, v in enumerate(a):
        deduct_b.append(b[i]-cont_avg[v])
    return deduct_b

if __name__ == "__main__":
    a = [1, 1, 5, 3, 1, 3, 5]
    b = [10, 20, 30, 15, 17, 19, 7]
    print(main(a,b))