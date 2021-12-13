import ListaFuncionarios
def novoFuncionario():
    import funcionarios
    import main
    continuarFunc = 0
    print("-" * 22)
    print("Choice : New Employee")
    print("-" * 22)
    # integrar o Id dos funcionarios
    funcionarios.idfun = idfun + 1
    print("Employee Id :", funcionarios.idfun)
    # inputs
    nomenovoFunc = str(input("Emplyees's name:"))
    nomenovoFunc.title()
    enderecFunc = str(input("Employees's adress :"))
    idadeFunc = int(input("Employees's Age :"))
    wageFunc = float(input("Employees's wage :"))
    # pegar a lista dos imputs botar na lista funcionarios
    funcionarios.funcionariosList = listaFunc(idfun,nomenovoFunc,enderecFunc,idadeFunc,wageFunc)
    # pegar a lista funcionarios e colocar na lista funcionarios real fazendo com que fique todas as infos juntas em 1 index
    _itensfunc = ListaFuncionarios.ListaFuncionarios.addFunc(funcionarios.funcionariosList)
    print("New Employee Listed")
    continuarFunc = int(input("1. Continue / 2. Back to menu : "))
    if continuarFunc == 1:
        funcionarios.novoFuncionario()
    elif continuarFunc == 2:
        main.escolhaMenu()
    else:
        main.escolhaMenu()

def todosFuncionarios():
    import funcionarios
    import main
    print("-" * 22)
    print("Employees :")
    # exibir a lista de todos os funcionarios
    print(ListaFuncionarios.ListaFuncionarios.listaFunc2(funcionarios._itensFunc))
    print("-" * 22)
    escolhaFuncRegistrado = int(input("do you want to add a new Employee? 1. Yes // 2. No : "))
    if escolhaFuncRegistrado == 1:
        funcionarios.novoFuncionario()
    elif escolhaFuncRegistrado == 2:
        main.escolhaMenu()
    else:
        main.escolhaMenu()
def listaFunc(idfun,name, adress, age , wage):
    return [idfun,name, adress, age, wage]

funcionariosList = []
idfun = 0
_itensFunc = []