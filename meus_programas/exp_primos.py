noprimes = [j for i in range(2, 8) for j in range(i*2, 50, i)]
print(noprimes)

primes = [x for x in range(2, 50) if x not in noprimes]
print(primes)

#no primes
noprimes_normal = []
for i in range (2, 8):
    for j in range (i*2, 50, i):
        noprimes_normal.append(j)

print(noprimes_normal)

# Ele listou todos os multiplos de 2, 3, 4, 5, 6 e 7
# Depois ele criou uma lista com todos os números que não estão na lista dos múltiples
# E assim achou os números primos.