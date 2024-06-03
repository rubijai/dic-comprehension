# Uso de dictionary comprehension
# Prueba de uso de github
l = [1,2,3,4,5,6,7,8,9]
nl = [x**3 for x in l if x % 2 == 1]
print(f' nl = {nl}')
dicc = {x: x**3  if x % 2 == 1 else x**2  for x in l}
print(f' dicc = {dicc}')
dicc1 = {i:l[i]**3 if l[i] % 2 == 1 else l[i]**2 for i in range(len(l))}
print(f' dicc1 = {dicc1}')
