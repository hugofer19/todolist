tarefa1 = input("Tarefa 1: ")
tarefa2 = input("Tarefa 2: ")
tarefa3 = input("Tarefa 3: ")
remove = 0
lista = [tarefa1, tarefa2, tarefa3]

acao = print("Quer remover alguma tarefa?")
acao_resultado = input("Escreve sim ou não: ")
if acao_resultado == "sim":
    remove = input("Escolha o número da tarefa que deseja remover (1, 2 ou 3): ")
    if remove == "1":
        lista.remove(tarefa1)
    elif remove == "2":
        lista.remove(tarefa2)
    elif remove == "3":
        lista.remove(tarefa3)
else: print("Nenha tarefa removida")

print(lista)

