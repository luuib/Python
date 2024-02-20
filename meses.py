
meses = float(input ("Escreva seu  mes:"))

if meses  ("dezembro,janeiro,fevereiro"):
    categoria = "Verao"
elif meses ("marco, abril,maio,junho"):
    categoria = " Outono"
elif meses ("julho, agosto, setembro"):
    categoria = "Inverno"
else: meses ("outubro, novembro")
    categoria = "Primavera"

print(f"Você está na categoria: {categoria}.")