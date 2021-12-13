import ListaClientes


def novoCliente():
    import clientes
    import main
    continuarClie = 0
    print("-" * 22)
    print("Choice : New Customer")
    print("-" * 22)
    # integrar o Id dos clientes
    clientes.idcli = idcli + 1
    print("Customer Id :", clientes.idcli)
    # inputs
    nomenovoClien = str(input("Customer's name:"))
    nomenovoClien.title()
    enderecClien = str(input("Customer's adress :"))
    idadeClien = int(input("Customer's Age :"))
    # pegar a lista dos imputs botar na lista clientes
    clientes.clientsList = listaClient(idcli,nomenovoClien,enderecClien,idadeClien)
    # pegar a lista clientes e colocar na lista clientes real fazendo com que fique todas as infos juntas em 1 index
    _itensClientes= ListaClientes.ListaCliente.addClie(clientes.clientsList)
    print("New Employee Listed")
    continuarClie = int(input("1. Continue / 2. Back to menu : "))
    if continuarClie == 1:
        clientes.novoCliente()
    elif continuarClie == 2:
        main.escolhaMenu()
    else:
        main.escolhaMenu()

def todosClient():
    import clientes
    import main
    print("-" * 22)
    print("Employees :")
    # exibir a lista de todos os clientes
    print(ListaClientes.ListaCliente.listaClie2(clientes._itensClientes))
    print("-" * 22)
    escolhaclienRegistrado = int(input("do you want to add a new Customer? 1. Yes // 2. No : "))
    if escolhaclienRegistrado == 1:
        clientes.novoCliente()
    elif escolhaclienRegistrado == 2:
        main.escolhaMenu()
    else:
        main.escolhaMenu()
def listaClient(idcli,name, adress, age):
    return [idcli,name, adress, age]

clientsList = []
idcli = 0
_itensClientes = []