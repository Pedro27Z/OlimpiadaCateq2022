palavra=input("digite uma palavra:")
letra=str(input("digite uma letra: "))
def palavra_repetida(palavra,letra):
  count_letra = 0
  if len(letra) > 1:
    letra=letra[0]
  for i in palavra:
    if letra == i:
      count_letra += 1
  return count_letra
print(f"A letra {letra[0]} repete {palavra_repetida(palavra,letra)} vezes na palavra {palavra}" )
# deyvisson, eliete, roxanny, pedro
