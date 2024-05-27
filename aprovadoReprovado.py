nota1 = float(input("qual a primeira nota: "))
nota2 = float(input("qual a segunda nota: "))
nota3 = float(input("qual a terceira nota: "))

media = (nota1+nota2+nota3)/3

print(media)
if media <= 5: print("reprovado")
elif media <= 6.5: print("recuperacao")
else: print("Aprovado")