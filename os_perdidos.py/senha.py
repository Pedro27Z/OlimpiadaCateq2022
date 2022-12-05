repetir = True
def verificar_senha(senha):
  global repetir
  if len(senha) >=4 and len(senha)<=8:
    if senha.isnumeric():
      repetir=False
      print(" OK , senha valida")
    else:
      print(" A senha só pode conter numeros, por favor digite outra senha")
  else:
      print("Vc digitou uma quantidade de numeros invalidos, por favor digite outra senha.")
  

while (repetir):
  senha=(input("Digite uma senha de no (min:4 ,max: 8):"))
  verificar_senha(senha)
      
