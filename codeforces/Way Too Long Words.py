n = int(input())

for _ in range(n):
    ip = input()
    if len(ip) >= 11:
        s = ip[0]+ str(len(ip)-2) + ip[-1]
        print(s)
    else:
        print(ip)