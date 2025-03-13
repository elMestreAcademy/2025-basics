num = int(input("Introduce el primer sumando: "))
total = 0
contador = 1

while num != 0:
	total += num
	num = int(input("Intruduce otro sumando: "))
	contador += 1

print("SUMA:     ", total)
print("términos: ", contador)
print("MEDIA:    ", total/contador)
