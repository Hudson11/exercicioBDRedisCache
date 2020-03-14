import redis

# TODOS OS VALORES FICAM ARMAZENADOS POR 2 MINUTOS EM CACHE

r = redis.Redis()

valueFatorial = int ( input('Digite o valor inteiro para calcular o seu fatorial -> ') )

print('valor digitado foi -> ', valueFatorial)
print('Tipo do Valor -> ', type(valueFatorial))

def calcFatorial(value):
    soma = 1
    for a in range(2, value+1):
        soma = soma * a
    return soma

result = r.get(str(valueFatorial))

if result is not None:
    print('Valor do Fatorial de ', valueFatorial, ' eh igual há -> ', int(result))
    print('Valor retornado do cache')
else:
    result = calcFatorial(valueFatorial)
    print('Valor do Fatorial de ', valueFatorial, ' eh igual há -> ', result)
    print('Valor foi calculado e armazenado em cache')
    r.set(str(valueFatorial), result, ex=120)

