def fact(n):
    
    if(n>0):
       
        return n * fact(n-1)
        
    else:
        return 1
    

numero=int(input("entrer numero :"))
print(fact(numero))




