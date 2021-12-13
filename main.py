
def escolhaMenu():
    print("Type 1 to Create new Product")
    print("Type 2 to Show registered Product")
    print("Type 3 to Create new employee")
    print("Type 4 to Show registered employees")
    print("Type 5 to Create new customer")
    print("Type 6 to Show registered costumers")
    print("Type 7 to Create new sale")
    print("Type 8 to Show registered sales")
    print("-"*22)
    escolha = int(input("My Choice :"))
    validarEscolha(escolha)

def validarEscolha(escolha):
    import produtos
    import funcionarios
    import clientes
    import vendas
    if escolha == 1:
        produtos.novoProduto()
    elif escolha == 2:
        produtos.produtosRegistrados()
    elif escolha == 3:
        funcionarios.novoFuncionario()
    elif escolha == 4:
        funcionarios.todosFuncionarios()
    elif escolha == 5:
        clientes.novoCliente()
    elif escolha == 6:
        clientes.todosClient()
    elif escolha == 7:
        vendas.novaVenda()
    elif escolha == 8:
        vendas.todasVendas()
    else:
        print("-" * 22)
        print("Wrong number")
        print("-" * 22)
        escolhaMenu()


escolha= 0
print("-"*22)
print("Welcome to my market!")
print("-"*22)
escolhaMenu()

