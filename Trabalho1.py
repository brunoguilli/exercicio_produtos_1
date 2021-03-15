lst_produtos = []

#--------------------------------------------------#

class Produto:

    def __init__(self, codigo,nome, preco, quantidade):
        self.codigo = codigo
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def get_nome(self):
        return self.nome

    def get_codigo(self):
        return self.codigo

    def get_preco(self):
        return self.preco

    def get_quantidade(self):
        return self.quantidade

#--------------------------------------------------#

def exibir_produtos():
    for p in lst_produtos:
      print("Nome: " ,p.get_nome()," Preco: ",p.get_preco()," Qtd: ",p.get_quantidade() )

#--------------------------------------------------#

def remover_produtos():

    if len(lst_produtos) > 0:

        for p in lst_produtos:
          print(p.get_codigo() ,"-", p.get_nome())

        codigo_produto = buscar_produto()

        for indice,produto in enumerate(lst_produtos):
            if produto.get_codigo() == codigo_produto:
                del lst_produtos[indice]
        print("\n Produto removido da lista!")

    else:
        print("Não existem mais produtos na lista!")

#--------------------------------------------------#

def buscar(list, metodo):
    for x in list:
        if metodo(x):
            return x
    return False

#--------------------------------------------------#

def buscar_produto():
    while True:
        codigo = int(input("Insira o codigo do produto: "))

        if buscar(lst_produtos, lambda x: x.get_codigo() == codigo):
            return codigo
        else:
            input(" Codigo inexistente. Pressione [Enter]")

#--------------------------------------------------#

# Produtos pré definidos
lst_produtos.append(Produto(len(lst_produtos),"Coca-Cola", 5, 10))
lst_produtos.append(Produto(len(lst_produtos),"Suco de Uva", 3.50, 4))
lst_produtos.append(Produto(len(lst_produtos),"Chocolate", 2.80, 30))
lst_produtos.append(Produto(len(lst_produtos),"Água ardente", 3.50, 60))

#--------------------------------------------------#

while True:
    try:
        print("\n")
        print("---------------PRODUTO---------------")
        print("*                                   *")
        print("*      0 - Finalizar o Programa     *")
        print("*      1 - Exibir Produtos          *")
        print("*      2 - Remover Produtos         *")
        print("*                                   *")
        print("-------------------------------------")
        opcao = int(input("\nDigite a opção desejada: "))

    except:
        continue

    if opcao == 0:
        print("\nVolte Sempre...")
        break
    if opcao == 1: exibir_produtos()
    if opcao == 2: remover_produtos()