import sys
filename = sys.argv[1]
f = open(filename, 'r')
F = f.readlines()
A = []
for i in F:
    A.append(i.split())

people = A[0]
total = float(A[-1][0])
A = A[1:-1]
# print(A,total)
D = {}
for i in people:
    D[i] = {'items': [],
            'amount': 0,
            'tax': 0,
            'total': 0,
            }


for i in A:
    item = i[0]
    n_shares = 0
    cost = float(i[-1])
    for field,person in enumerate(people):
        field+=1
        share = float(i[field])
        n_shares+=share

    for field,person in enumerate(people):
        field+=1
        share = float(i[field])
        amount = (share/n_shares) * cost
        D[person]['items'].append((item, share, amount))
        D[person]['amount']+=amount


subtotal = 0
for p in people:
    subtotal+=D[p]['amount']

extra = total-subtotal
for p in people:
    D[p]['tax'] = (D[p]['amount']/subtotal)*extra
    D[p]['total'] = D[p]['amount'] + D[p]['tax']


for p in D:
    print(p, 'items:')
    for item in D[p]['items']:
        print(item)
    print(p,'subtotal',D[p]['amount'])
    print(p,'tax',D[p]['tax'])
    print(p,'total',D[p]['total'])
    print()

