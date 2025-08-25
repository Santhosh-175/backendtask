# def is_prime(n):
#     if n<=1:
#         return 'Not a Prime'
#     for i in range(2,n):
#         if n%i==0:
#             return 'Not a Prime'
#     return 'prime'  

# n=int(input("Enter Number:"))
# print(is_prime(n))



# def is_prime(n):
#     if n<=1:
#         return 'Not a Prime'
#     for i in range(2,(n//2)+1):
#         if n%i==0:
#             return 'Not a Prime'
#     return 'prime'  
    
# n=int(input("Enter Number:"))
# print(is_prime(n))







# def is_prime(n):
#     if n<=1:
#         return 'Not a Prime'
#     for i in range(2,int(n**0.5)+1):
#         if n%i==0:
#             return 'Not a Prime'
#     return 'prime'  
    
# n=int(input("Enter Number:"))
# print(is_prime(n))


for n in range(100,301):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            # print("Non Prime")
            break
    else:
        print(n)








