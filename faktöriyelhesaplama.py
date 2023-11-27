def faktoriyel(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * faktoriyel(n-1)

sayi = int(input("Faktöriyeli hesaplanacak sayıyı girin: "))
result = faktoriyel(sayi)
print(f"{sayi}! = {result}")