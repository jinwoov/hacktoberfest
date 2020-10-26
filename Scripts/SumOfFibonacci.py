## Effective Algorithm for Fibonnaci.
## To print the sum of fibonnaci numbers upto n digits.

n = int(input())
fibo_arr = [0, 1]

for _ in range(2, n+1):
    fibo_arr.append(fibo_arr[-1] + fibo_arr[-2])  
    
print(fibo_arr[-1])
    
    
    
