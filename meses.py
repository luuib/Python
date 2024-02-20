meses = input ("Escreva seu  mes:")

if meses in  ("dezembro","janeiro","fevereiro"):
    categoria = "Verao"
elif meses in ("marco"," abril","maio","junho"):
    categoria = " Outono"
elif meses in ("julho"," agosto"," setembro"):
    categoria = "Inverno"
else:
    categoria = "Primavera"

print(f"Você está na categoria: {categoria}.")
