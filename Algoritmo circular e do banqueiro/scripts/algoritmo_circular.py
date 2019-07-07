import string

alfabeto = list(string.ascii_lowercase.upper())

def configurar_processos(quantidade_de_processos):
    nome_processos = []
    tempo_de_cpu_de_cada_processo = [] 
    tempo_de_turnaround_de_cada_processo = []
    dados_para_o_grafico = []
    for i in range(quantidade_de_processos):
        tempo_de_cpu = int(input("Qual o tempo de CPU do processo %s ?\n" % alfabeto[i]))
        nome_processos.append(alfabeto[i])
        tempo_de_cpu_de_cada_processo.append(tempo_de_cpu)
        tempo_de_turnaround_de_cada_processo.append(0)
        dados_para_o_grafico.append(alfabeto[i] + "|")
    return nome_processos, tempo_de_cpu_de_cada_processo, tempo_de_turnaround_de_cada_processo, dados_para_o_grafico


def algoritmo_circular():
    quantidade_processos = int(input("Quantos processos?:"))
    processos = configurar_processos(quantidade_processos)
    tempo_de_troca_de_contexto = int(input("Tempo de troca de contexto?:"))
    tempo_medio_de_espera = 0
    nome_processos = processos[0]
    tempo_de_cpu_de_cada_processo = processos[1]
    tempo_de_cpu_de_cada_processo_aux = processos[1].copy()
    tempo_de_turnaround_de_cada_processo = processos[2]
    dados_para_o_grafico = processos[3]
    quantum = int(input("Valor do Quantum?:"))
    auxiliar = len(tempo_de_cpu_de_cada_processo_aux) - 1
    while(True):
        if auxiliar < 0:
            break

        for indice in range(len(tempo_de_cpu_de_cada_processo_aux)):
            if (tempo_de_cpu_de_cada_processo_aux[indice] - quantum >= 0):
                tempo_medio_de_espera += (quantum + tempo_de_troca_de_contexto) * auxiliar
                for indice2 in range(len(tempo_de_cpu_de_cada_processo_aux)):
                    if tempo_de_cpu_de_cada_processo_aux[indice2] != 0:   
                        if indice2 != indice:
                            dados_para_o_grafico[indice2] += "-" * quantum + "-" * tempo_de_troca_de_contexto
                            tempo_de_turnaround_de_cada_processo[indice2] += quantum + tempo_de_troca_de_contexto
                        else:
                            if (tempo_de_cpu_de_cada_processo_aux[indice] - quantum == 0):
                                dados_para_o_grafico[indice2] += "O" * quantum
                                tempo_de_turnaround_de_cada_processo[indice2] += quantum
                            else:
                                dados_para_o_grafico[indice2] += "O" * quantum + "-" * tempo_de_troca_de_contexto
                                tempo_de_turnaround_de_cada_processo[indice2] += quantum + tempo_de_troca_de_contexto

                tempo_de_cpu_de_cada_processo_aux[indice] -= quantum
                if tempo_de_cpu_de_cada_processo_aux[indice] == 0:
                    auxiliar -= 1
            else:
                tempo_medio_de_espera += (tempo_de_cpu_de_cada_processo_aux[indice] + tempo_de_troca_de_contexto) * auxiliar
                for indice2 in range(len(tempo_de_cpu_de_cada_processo_aux)):
                    if tempo_de_cpu_de_cada_processo_aux[indice2] != 0:
                        tempo_de_turnaround_de_cada_processo[indice2] += tempo_de_cpu_de_cada_processo_aux[indice]
                        if indice2 != indice:
                            dados_para_o_grafico[indice2] += "-" * tempo_de_cpu_de_cada_processo_aux[indice] + "-" * tempo_de_troca_de_contexto
                        else:
                            if (tempo_de_cpu_de_cada_processo_aux[indice] - quantum < 0):
                                dados_para_o_grafico[indice2] += "O" * tempo_de_cpu_de_cada_processo_aux[indice]
                            else:
                                dados_para_o_grafico[indice2] += "O" * tempo_de_cpu_de_cada_processo_aux[indice] + "-" * tempo_de_troca_de_contexto

                tempo_de_cpu_de_cada_processo_aux[indice] = 0
                auxiliar -= 1

    for indice in range(len(tempo_de_cpu_de_cada_processo_aux)):
        if tempo_de_cpu_de_cada_processo_aux[indice] != 0:
            tempo_de_turnaround_de_cada_processo[indice] += tempo_de_cpu_de_cada_processo_aux[indice]
            dados_para_o_grafico[indice] += "O" * tempo_de_cpu_de_cada_processo_aux[indice]
            tempo_de_cpu_de_cada_processo_aux[indice] = 0

    tempo_medio_de_espera /= quantidade_processos
    tempo_medio_de_espera += 1
    print("\n**Dados**")
    print("Tempo de CPU:")
    for indice in range(len(nome_processos)):
        print("\t", nome_processos[indice], "=>", tempo_de_cpu_de_cada_processo[indice], "u.t")
    print("Tempo de turnaroud:")
    for indice in range(len(nome_processos)):
        print("\t", nome_processos[indice], "=>", tempo_de_turnaround_de_cada_processo[indice], "u.t")
    print("Tempo médio de espera => ", tempo_medio_de_espera, "u.t")
    print("Tempo médio de turnaroud =>", sum(tempo_de_turnaround_de_cada_processo) / quantidade_processos, "u.t")
    
    print("Tempo de troca de contexto =>", tempo_de_troca_de_contexto)

    print("*****Gráfico*****")
    for dados in dados_para_o_grafico:
        print(dados)
