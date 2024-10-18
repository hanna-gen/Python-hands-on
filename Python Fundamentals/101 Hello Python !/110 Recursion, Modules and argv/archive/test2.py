def fact(n):
    if n<2:
        return 1
    else:
        return n*int(fact(n-1))
  
            
        
fact(5)

#n-1*n-2*n-3*n-4*n-5