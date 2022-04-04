a=int(input("numero"))
r=input("escolha qual será a base de conversão:\n1 para binário\n2 para octal\n3 para hexadecimal.")
if r=="1":
    print(bin(a))
elif r=="2":
    print(oct(a))
elif r=="3":
    print(hex(a))