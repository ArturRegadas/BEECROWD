def maxprice(price, weight, size, repeat) -> int:

    maxinum=[0 for i in range(0, size+1, +1)]

    for i in range(0, repeat):
        value_p=price[i]
        value_w=weight[i]

        for w in range(size, value_w-1, -1):
            maxinum[w]=max(maxinum[w], maxinum[w-value_w]+value_p)
        
    return maxinum[size]


tests=int(input())
for r in range(0, tests, +1 ):
    repeats=int(input())
    size=int(input())

    prices=[]
    weights=[]
    for i in range(0,repeats,+1):
        data=input().split(' ')
        prices.append(int(data[0]))
        weights.append(int(data[1]))
    
    print(f"Galho {r+1}:")
    print("Numero total de enfeites:",maxprice(prices, weights, size, repeats))
    print()