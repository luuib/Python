lista = ["banana", "maçã", "laranja", "pêra", "uva"]

while True:
  print("O que você deseja fazer com a lista?")
  print("1. Quer colocar algo?")
  print("2. tirar um item")
  print("3. mostrar a lista")
  print("4. Sair")

  opcao = int(input("Digite a sua opção: "))

  if opcao == 1:
    item = input("Digite o item que deseja adicionar: ")
    lista.append(item)
    print("Item adicionado com sucesso!")
  elif opcao == 2:
    item = input("Digite o item que deseja remover: ")
    if item in lista:
      lista.remove(item)
      print("Item removido com sucesso!")
    else:
      print("Item não encontrado na lista.")
  elif opcao == 3:
    print("Lista atual:")
    for item in lista:
      print(f"- {item}")
  elif opcao == 4:
    print("Adeus")
    break
  else:
    print("Opção inválida. Tente novamente.")
