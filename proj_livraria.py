import matplotlib.pyplot as plt
from collections import Counter

# --- PASSO 1: Definir a classe Livro ---
class Livro:
    """Representa um livro com título, autor, gênero e quantidade disponível."""
    def __init__(self, titulo, autor, genero, quantidade):
        self.titulo = titulo.strip().title() # Garante que o título e autor fiquem padronizados
        self.autor = autor.strip().title()
        self.genero = genero.strip().capitalize() # Padroniza o gênero
        try:
            self.quantidade = int(quantidade)
            if self.quantidade < 0:
                 self.quantidade = 0
        except ValueError:
            self.quantidade = 0 # Define 0 se a quantidade não for um número válido

    def __str__(self):
        """Retorna uma representação legível do objeto Livro."""
        return f"Título: {self.titulo} | Autor: {self.autor} | Gênero: {self.genero} | Disponível: {self.quantidade}"

# --- PASSO 2: Criar a lista de livros ---
biblioteca = []

# Adicionando alguns livros iniciais para facilitar o teste
biblioteca.append(Livro("A Sociedade do Anel", "J.R.R. Tolkien", "Fantasia", 5))
biblioteca.append(Livro("1984", "George Orwell", "Ficção Científica", 3))
biblioteca.append(Livro("O Hobbit", "J.R.R. Tolkien", "Fantasia", 7))
biblioteca.append(Livro("O Retrato de Dorian Gray", "Oscar Wilde", "Clássico", 2))
biblioteca.append(Livro("Neuromancer", "William Gibson", "Ficção Científica", 4))


# --- PASSO 3: Implementar funções para gerenciar os livros ---

def cadastrar_livro():
    """Solicita informações e cadastra um novo livro na biblioteca."""
    print("\n--- Cadastro de Novo Livro ---")
    titulo = input("Título do livro: ")
    autor = input("Autor: ")
    genero = input("Gênero: ")
    quantidade = input("Quantidade disponível: ")
    
    novo_livro = Livro(titulo, autor, genero, quantidade)
    biblioteca.append(novo_livro)
    print(f"\n✅ Livro '{novo_livro.titulo}' cadastrado com sucesso!")

def listar_todos_livros():
    """Exibe todos os livros presentes na biblioteca."""
    if not biblioteca:
        print("\nA biblioteca está vazia. Cadastre o primeiro livro!")
        return
        
    print("\n--- Todos os Livros Disponíveis ---")
    for i, livro in enumerate(biblioteca):
        print(f"[{i+1}] {livro}")

def buscar_livro_por_titulo(titulo_busca):
    """Busca e exibe livros que contêm a string de busca no título."""
    titulo_busca = titulo_busca.strip().title()
    encontrados = [livro for livro in biblioteca if titulo_busca in livro.titulo]
    
    if encontrados:
        print(f"\n--- Resultados da Busca por '{titulo_busca}' ---")
        for livro in encontrados:
            print(f"-> {livro}")
    else:
        print(f"\n❌ Nenhum livro encontrado com o título que contenha '{titulo_busca}'.")

# --- PASSO 4: Utilizar a biblioteca Matplotlib para gerar um gráfico ---

def gerar_grafico_generos():
    """Gera um gráfico de barras com a contagem de livros por gênero."""
    if not biblioteca:
        print("\n❌ Não há livros para gerar o gráfico. Cadastre alguns livros primeiro.")
        return
        
    # 1. Coleta e soma a quantidade de livros por gênero
    # Usamos o Counter para facilitar a contagem dos gêneros
    contagem_generos = Counter()
    for livro in biblioteca:
        contagem_generos[livro.genero] += livro.quantidade

    generos = list(contagem_generos.keys())
    quantidades = list(contagem_generos.values())

    # 2. Criação do Gráfico de Barras
    plt.figure(figsize=(10, 6)) # Define o tamanho da janela do gráfico
    plt.bar(generos, quantidades, color=['skyblue', 'lightcoral', 'lightgreen', 'gold', 'lightsalmon'])

    # Adiciona rótulos e título
    plt.xlabel("Gênero")
    plt.ylabel("Quantidade Total de Livros")
    plt.title("Quantidade Total de Livros por Gênero")
    
    # Adiciona a quantidade exata acima de cada barra
    for i, quantidade in enumerate(quantidades):
        plt.text(i, quantidade + 0.1, str(quantidade), ha='center', va='bottom')

    # Ajusta o layout e exibe o gráfico
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()
    print("\nGráfico de Quantidade de Livros por Gênero gerado com sucesso!")


# --- Exemplos de Uso das Funções ---

if __name__ == "__main__":
    print("Sistema de Gerenciamento de Livros da Biblioteca")
    print("------------------------------------------------")
    
    # 1. Listar todos os livros iniciais
    listar_todos_livros()
    
    # 2. Cadastrar um novo livro
    cadastrar_livro() # Execute a função para inserir os dados quando o script rodar
    
    # 3. Listar novamente (com o novo livro)
    listar_todos_livros()
    
    # 4. Buscar um livro
    # Você pode testar com títulos parciais como "O Anel" ou "19"
    buscar_livro_por_titulo(input("\nDigite parte do título do livro para buscar: "))
    
    # 5. Gerar o Gráfico
    # Esta função irá abrir uma janela com o gráfico de barras.
    gerar_grafico_generos()