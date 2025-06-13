for _ in range(int(input())):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    ans = 0

    asuff = [a[n-1]]*n
    for i in range(n-2, -1, -1):
        asuff[i] = max(a[i], asuff[i+1])

    for i in range(n):
        if (i == n-1 or asuff[i+1] <= x-ans-1) and b[i] <= x-ans:
            ans += 1

    bans = '0'*n

    l = ans

    sops = [0]*(n+1)

    for i in range(n-1, -1, -1):
        curr = x-ans +1
        curr += sops[i+1]
        if b[i] <= x:
            bans[i] = '1'
            sops[i] = sops[i+1]+1
        else:
            sops[i] = sops[i+1]




    print(bans)
