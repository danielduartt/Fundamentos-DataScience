
#Decoradores
#1-Definindo variáveis como funções 
def soma_um(num):
    return num + 1
#f1 = soma_um 
#f1(1) #=> retorna o 2 
#2-Definir Funções dentro de outras Funções 
def soma_um(num): 
    def add_1(num):
        return num + 1
    return add_1(num) 
#3- Passar Funções como argumentos de outras funções 
def function_call(function): 
    num_to_add = 5
    return function(num_to_add)
function_call(soma_um)
#4- Funções tbm podem ser retornada dentro de funções 
def func_dia(): 
    def hello():
        return 'Hi'
    return hello
ola = func_dia()

#decorators são funções que alteram outras funções 
def decorador_maiusculo(function):
    def wrapper():
        func = function()
        maiusculo = func.upper()
        return maiusculo
    return wrapper 
#Exemplo 
def diga_oi():
    return "Hello World"

func = decorador_maiusculo(diga_oi)#aqui 
func()# e aqui 


@decorador_maiusculo
def diga_oi():
    return "Hello World"
diga_oi() #agora vai equivaler ao código da linha 42 e 42
