import os

def carregar_lista():
  """
  Carrega a lista de compras do arquivo "lista.txt".
  """
  try:
    with open("lista.txt", "r") as arquivo:
      lista = arquivo.read().splitlines()
  except FileNotFoundError:
    lista = []
  return lista

def salvar_lista(lista):
  """
  Salva a lista de compras no arquivo "lista.txt".
  """
  with open("lista.txt", "w") as arquivo:
    for item in lista:
      arquivo.write(f"{item}\n")

# Inicializa a lista de compras
lista = carregar_lista()

while True:
  # Exibe o menu de opções
  print("O que você deseja fazer com a lista?")
  print("1. Adicionar item")
  print("2. Remover item")
  print("3. Mostrar lista")
  print("4. Gravar arquivo")
  print("5. Ler arquivo")
  print("6. Sair")

  # Obtem a opção do usuário
  opcao = int(input("Digite a sua opção: "))

  # Trata cada opção do menu
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
    if lista:
      print("Lista atual:")
      for item in lista:
        print(f"- {item}")
    else:
      print("A lista está vazia.")
  elif opcao == 4:
    salvar_lista(lista)
    print("Lista salva com sucesso!")
  elif opcao == 5:
    lista = carregar_lista()
    print("Lista carregada com sucesso!")
  elif opcao == 6:
    print("Adeus!")
    break
  else:
    print("Opção inválida. Tente novamente.")
