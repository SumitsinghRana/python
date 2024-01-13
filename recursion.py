while(True):
    
    def recursion(n):
        if n==1:
          return 1
        elif n==0:
            return 1
        else:
            return n*recursion(n-1)
        
    a=int(input("Enter the number->"))
    if a==-1:
        break
    else:
        ans=recursion(a)
        print(ans)