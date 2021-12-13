def novaVenda():
    import vendas
    import main
    continuarvendas = 0
    print("-" * 22)
    print("Choice : New Sale")
    print("-" * 22)
    vendas.idsale = idsale + 1
    print("Sale Id :", vendas.idsale)
    idprodu = int(input("Id Product:"))
    idclient = int(input("Id Customer :"))
    qntsale = int(input("Amount :"))
    vendas.salesList = listaSales(idsale,idprodu,idclient,qntsale)
    continuarVenda = int(input("1. Continue / 2. Back to menu : "))
    if continuarVenda  == 1:
        vendas.novaVenda()
    elif continuarVenda  == 2:
        main.escolhaMenu()
    else:
        main.escolhaMenu()

def todasVendas():
    import vendas
    import main
    print("-" * 22)
    print("Sales :")
    print(salesList)
    print("-" * 22)
    escolhasaleRegistrado = int(input("do you want to add a new sale? 1. Yes // 2. No : "))
    if escolhasaleRegistrado == 1:
        vendas.novaVenda()
    elif escolhasaleRegistrado == 2:
        main.escolhaMenu()
    else:
        main.escolhaMenu()

def listaSales(idsale,idpro, idcli, qntsale):
    return [idsale,idpro, idcli, qntsale]

salesList = []
idsale = 0
