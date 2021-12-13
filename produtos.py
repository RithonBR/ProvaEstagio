def novoProduto():
    import produtos
    import testes
    import main
    print("-"*22)
    print("Choice : New Product")
    print("-"*22)
    produtos.idprod= idprod + 1
    print("Product Id :",produtos.idprod)
    nomenovoprod = str(input("Product's name:"))
    nomenovoprod.title()
    precoDoProduto = float(input("Product's price :"))
    qntDoProduto = int(input("Amount :"))
    if nomenovoprod in estoque:
        print("-" * 22)
        print("Already listed")
        novoProduto()
    else:
        continuarProd = 0
        produtos.estoque = listaProds(idprod,nomenovoprod,precoDoProduto,qntDoProduto)
        _itens = testes.Lista.addProd(produtos.estoque)
        print("New Product Listed")
        continuarProd = int(input("1. Continue / 2. Back to menu : "))
        if continuarProd == 1:
            produtos.novoProduto()

        elif continuarProd == 2:
            main.escolhaMenu()
        else:
            main.escolhaMenu()

def produtosRegistrados():
    import produtos
    import main
    import testes
    print("-" * 22)
    print("Products STOCK :")
    print(testes.Lista.listaProds2(produtos._itens))
    print("-" * 22)
    escolhaProdRegistrado= int(input("do you want to add a new product? 1. Yes // 2. No : "))
    if escolhaProdRegistrado == 1:
        produtos.novoProduto()
    elif escolhaProdRegistrado == 2:
        main.escolhaMenu()
    else:
        main.escolhaMenu()

def listaProds(idprod,name, price, amount):
    return [idprod,name, price, amount]


estoque = []
_itens = []
idprod=0