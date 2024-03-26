
lista = ["banana", "maçã", "laranja", "pêra", "uva"]

while True:
  print("O que você deseja fazer com a lista?")
  print("1. Adicionar um item")
  print("2. Remover um item")
  print("3. Exibir a lista")
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
    print("Saindo...")
    break
  else:
    print("Opção inválida. Tente novamente.")

