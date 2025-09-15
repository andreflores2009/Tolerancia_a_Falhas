import random


def consenso_bizantino(processos, falhos):
    votos = []
    for i in range(processos):
        if i < falhos:
            # Os primeiros 'falhos' processos são bizantinos e podem enviar 
            # votos imprevisíveis, incluindo valores inválidos como 2,3 e 4.
            votos.append(random.choice([3, 4, 2]))
        else:
            # Os demais processos são corretos e votam apenas 0 ou 1.
            votos.append(random.choice([0, 1]))
    
    print("Votos (incluindo bizantinos):", votos)

    # Esta linha filtra a lista 'votos' para considerar apenas os valores válidos 0 e 1,
    # ignorando o valor 2, que representa votos inválidos ou arbitrários gerados pelos processos bizantinos.
    # Como o consenso deve ser tomado apenas com base em votos legítimos, esta filtragem é necessária.
    votos_validos = [v for v in votos if v in (0, 1)]   #list comprehension em python
    ''' faz o mesmo que 
    votos_validos = []
    for v in votos:
      if v in (0, 1):
        votos_validos.append(v)
    '''

    # A decisão final é o valor (0 ou 1) que aparece com mais frequência na lista de votos válidos.
    decisao = max(set(votos_validos), key=votos_validos.count)
    
    print("Decisão final ignorando falhas bizantinas:", decisao)


# Exemplo: 7 processos, 2 bizantinos
consenso_bizantino(7, 2)

