perguntas = {
    "perguntas 1": {
        'pergunta': 'Quanto é 2 + 2?',
        'respostas': {'a': '1', 'b': '4', 'c': '5',},
        'resposta certa': 'b',
    },
    "perguntas 2": {
        'pergunta': 'Quanto é 3 * 2?',
        'respostas': {'a': '4', 'b': '10', 'c': '6',},
        'resposta certa': 'c',
        },
}
print()
acertos=0
for pk, pv in perguntas.items():
    print(f'{pk}: {pv["pergunta"]}')
    for vk, vv in pv['respostas'].items():
        print(f'{vk}: {vv}')
    ans = input('Sua resposta: ')
    if ans == pv['resposta certa']:
        print("Boaaa! Você acertou!")
        acertos += 1
    else:
        print("QUE PENA! Você ERROU!")

c1 = len(perguntas)
porc = acertos / c1 * 100

print()
print(f"Você acertou {acertos} perguntas")
print(f"Sua porcentagem de acertos é {porc}%")