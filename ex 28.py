from time import sleep
começo = str (input('Pronto para começar ?'))
def jogo_quiz():
    # Dicionário com perguntas e respostas
    perguntas_respostas = {
        "Qual é a capital da França?": "Paris",
        "Quantos continentes existem no mundo?": "7",
        "Qual é o maior planeta do sistema solar?": "Jusimpiter",
        "Quantas ligações faz o carbono?": "4",
        "Qual é a fórmula química da água?": "H2O"
    }

    # Variáveis para contar o número de acertos e perguntas totais
    total_perguntas = len(perguntas_respostas)
    acertos = 0


    # Loop pelas perguntas
    sleep (2)
    for pergunta, resposta_correta in perguntas_respostas.items():
        print(pergunta)
        resposta_usuario = input("Resposta: ")

        # Verifica se a resposta está correta
        sleep (2)
        if resposta_usuario.strip().lower() == resposta_correta.lower():
            print("Correto!\n")
            acertos += 1
        else:
            print(f"Errado! A resposta correta é: {resposta_correta}\n")

    # Exibe a pontuação final
    print(f"Fim do quiz! Você acertou {acertos} de {total_perguntas} perguntas.")

# Chama a função do jogo
jogo_quiz()
