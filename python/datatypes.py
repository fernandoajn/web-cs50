#  PRINT FORMAT EXAMPLE
print("Hello, what's your name?")
name = input()
print(f"Hello, {name}!")

# TUPLES
x = 10
y = 20
coordenadas = (x,y)
print(coordenadas)

# LISTS
nomes = ["Fernando", "Guilhermina", "João"]
print(nomes)
print(nomes[0])
print(nomes[1:3])

# ELSE/IF
x = 0
if x>0:
    print("x é positivo")
elif x<0:
    print("x é negativo")
else:
    print("x é zero")

# FOR LOOP
for i in range(10):
    print(i)
names = ["Alice", "Bob", "Charlie"]
for name in names:
    print(name)

# SET
s = set()
s.add(1)
s.add(3)
s.add(5)
s.add(3)
print(s)

# DICTIONARIES
ages = {"Alice":22, "Bob":27}
ages["Charlie"] = 30
ages["Alice"] += 1
print(ages)
