import string

alfabeto = list(string.ascii_lowercase.upper())

def configurar_processos(quantidade_de_processos):
    nome_processos = []
    tempo_de_cpu_de_cada_processo = [] 
    tempo_de_turnaround_de_cada_processo = []
    for i in range(quantidade_de_processos):
        tempo_de_cpu = int(input("Qual o tempo de CPU do processo %s ?\n" % alfabeto[i]))
        nome_processos.append(alfabeto[i])
        tempo_de_cpu_de_cada_processo.append(tempo_de_cpu)
        tempo_de_turnaround_de_cada_processo.append(0)
    return nome_processos, tempo_de_cpu_de_cada_processo, tempo_de_turnaround_de_cada_processo


def algoritmo_circular():
    quantidade_processos = int(input("Quantos processos?:"))
    processos = configurar_processos(quantidade_processos)
    tempo_medio_de_espera = 0
    nome_processos = processos[0]
    tempo_de_cpu_de_cada_processo = processos[1]
    tempo_de_cpu_de_cada_processo_aux = processos[1].copy()
    tempo_de_turnaround_de_cada_processo = processos[2]
    quantum = int(input("Valor do Quantum?:"))
    auxiliar = len(tempo_de_cpu_de_cada_processo_aux) - 1
    while(True):
        if auxiliar < 0:
            break

        for indice in range(len(tempo_de_cpu_de_cada_processo_aux)):
            if (tempo_de_cpu_de_cada_processo_aux[indice] - quantum >= 0):
                tempo_medio_de_espera += quantum * auxiliar
                for indice2 in range(len(tempo_de_cpu_de_cada_processo_aux)):
                    if tempo_de_cpu_de_cada_processo_aux[indice2] != 0:
                        tempo_de_turnaround_de_cada_processo[indice2] += quantum

                tempo_de_cpu_de_cada_processo_aux[indice] -= quantum
                if tempo_de_cpu_de_cada_processo_aux[indice] == 0:
                    auxiliar -= 1
            else:
                tempo_medio_de_espera += tempo_de_cpu_de_cada_processo_aux[indice] * auxiliar
                for indice2 in range(len(tempo_de_cpu_de_cada_processo_aux)):
                    if tempo_de_cpu_de_cada_processo_aux[indice2] != 0:
                        tempo_de_turnaround_de_cada_processo[indice2] += tempo_de_cpu_de_cada_processo_aux[indice]
                tempo_de_cpu_de_cada_processo_aux[indice] = 0
                auxiliar -= 1

    for indice in range(len(tempo_de_cpu_de_cada_processo_aux)):
        if tempo_de_cpu_de_cada_processo_aux[indice] != 0:
            tempo_de_turnaround_de_cada_processo[indice] += tempo_de_cpu_de_cada_processo_aux[indice]
            tempo_de_cpu_de_cada_processo_aux[indice] = 0

    tempo_medio_de_espera /= quantidade_processos
    print("Tempo de CPU:")
    for indice in range(len(nome_processos)):
        print(nome_processos[indice], "=>", tempo_de_cpu_de_cada_processo[indice], "u.t")
    print("Tempo médio de espera => ", tempo_medio_de_espera, "u.t")
    for indice in range(len(nome_processos)):
        print("Tempo de turnround de", nome_processos[indice], "=>", tempo_de_turnaround_de_cada_processo[indice])
algoritmo_circular()