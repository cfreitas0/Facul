# Sistema Simples de Gestão de Notas de Alunos

# 1. Variáveis Globais (para armazenar os dados)
notas = []  # Lista para armazenar as notas dos alunos

# ----------------------------------------------------
## 2. Função para Adicionar Notas (Estrutura de Repetição e Condicional)
# O usuário pode inserir quantas notas desejar até digitar 'sair' ou deixar vazio.
def adicionar_notas():
    """Permite ao usuário inserir notas e as armazena na lista 'notas'."""
    print("\n--- Cadastro de Notas ---")
    while True:
        # Pede a nota ao usuário
        entrada = input("Digite uma nota (ou 'sair' para finalizar): ").strip().lower()

        # Condicional para verificar a entrada do usuário
        if entrada == 'sair' or entrada == '':
            break  # Sai do loop se o usuário digitar 'sair' ou deixar em branco

        try:
            # Tenta converter a entrada para um número decimal (float)
            nota = float(entrada)

            # Condicional para garantir que a nota é válida (entre 0 e 10, por exemplo)
            if 0 <= nota <= 10:
                notas.append(nota)  # Adiciona a nota válida à lista
                print(f"Nota {nota} adicionada com sucesso.")
            else:
                print("ERRO: A nota deve estar entre 0 e 10.")

        except ValueError:
            # Captura o erro se o usuário digitar algo que não é um número
            print("ERRO: Por favor, digite um número válido para a nota ou 'sair'.")

# ----------------------------------------------------
## 3. Função para Calcular a Média (Função)
def calcular_media(lista_notas):
    """Calcula a média aritmética de uma lista de notas."""
    # Condicional: Verifica se a lista não está vazia para evitar erro de divisão por zero
    if not lista_notas:
        return 0.0  # Retorna 0.0 se não houver notas

    # A função sum() soma todos os elementos da lista.
    # len() retorna o número de elementos (quantidade de notas).
    media = sum(lista_notas) / len(lista_notas)
    return media

# ----------------------------------------------------
## 4. Função para Determinar a Situação (Função e Condicional)
def determinar_situacao(media):
    """Determina a situação do aluno (Aprovado ou Reprovado) com base na média."""
    # Estrutura Condicional (If/Else)
    if media >= 7.0:
        return "APROVADO"
    else:
        return "REPROVADO"

# ----------------------------------------------------
## 5. Função Principal para Exibir o Relatório Final (Função)
def exibir_relatorio():
    """Calcula a média, determina a situação e exibe o relatório completo."""
    print("\n" + "="*40)
    print("         RELATÓRIO FINAL DO ALUNO         ")
    print("="*40)

    # 5.1. Exibe as notas inseridas (Estrutura de Repetição - For)
    if not notas:
        print("Nenhuma nota foi inserida. Relatório indisponível.")
        print("="*40)
        return # Encerra a função se não houver notas

    print("Notas Inseridas:")
    # Loop 'for' para iterar sobre a lista e exibir cada nota
    for i, nota in enumerate(notas):
        print(f"- Nota {i+1}: {nota:.2f}") # Formatação para 2 casas decimais

    # 5.2. Cálculo da Média
    media_final = calcular_media(notas)
    print(f"\n- Média Final: {media_final:.2f}")

    # 5.3. Determinação da Situação
    situacao_aluno = determinar_situacao(media_final)

    # Condicional para exibir a situação de forma clara e destacada
    if situacao_aluno == "APROVADO":
        print(f"- Situação: {situacao_aluno} (Parabéns!)")
    else:
        print(f"- Situação: {situacao_aluno} (Estude mais na próxima!)")

    print("="*40)

# ----------------------------------------------------
## 6. Fluxo Principal do Programa (Chamada das Funções)

# 6.1. Adicionar as notas (o usuário interage aqui)
adicionar_notas()

# 6.2. Exibir o relatório final
exibir_relatorio()