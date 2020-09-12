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
        amount = round((share/n_shares) * cost , 2)
        D[person]['items'].append((item, amount, str(int(share) if share.is_integer else share) + ' of ' + str(int(n_shares) if n_shares.is_integer else n_shares)))
        D[person]['amount']+=amount

subtotal = 0
for p in people:
    subtotal+=D[p]['amount']

extra = total-subtotal
for p in people:
    D[p]['tax'] = round((D[p]['amount']/subtotal)*extra, 2)
    D[p]['total'] = round(D[p]['amount'] + D[p]['tax'] , 2)

final_total = 0
for p in D:
    print(p, 'items:')
    for item in D[p]['items']:
        print('%s $%s (%s)' % item)
    print(p,'subtotal', round(D[p]['amount'],2))
    print(p,'tax/discount',D[p]['tax'])
    print(p,'total', D[p]['total'])
    final_total+=D[p]['total']
    print()

for p in people:
    print(p, "total:", D[p]['total'])

print()
print('final_total',final_total)

