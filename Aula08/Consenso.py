import random

# Função que simula um consenso entre um número dado de processos
def consenso(processos):
    # Cada processo "vota" randomicamente 0 ou 1, simulando uma proposta ou opinião de cada agente
    votos = [random.choice([0, 1]) for x in range(processos)]
    print("Votos recebidos:", votos)

    # O consenso é decidido pelo valor que aparece com maior frequência entre os votos (maioria)
    # max(set(votos), key=votos.count) seleciona o elemento na lista que tem a maior contagem
    decisao = max(set(votos), key=votos.count)
    print("Decisão final (consenso):", decisao)


# Exemplo de execução da função com 5 processos
consenso(5)

