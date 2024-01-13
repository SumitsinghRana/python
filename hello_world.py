def solve():
    s = ""
    c = 'a'
    d = "hello world" 
    p = " "
    n = 12

    for i in range(n):
        for j in range(int(1e7)):
            if p[i] == d[i]:
                i += 1  # You should increment i if the characters match
                print(p)
                print()
                p = p[:i] + chr(ord(p[i]) + 1) + p[i+1:]  # Correct the slicing and updating p
                for x in range(int(1e5)):
                    h = 0
                    h += h
                    print()

solve()  