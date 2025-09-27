import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configuração de Estilo para Visualizações
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)
plt.rcParams['figure.dpi'] = 100

# ==============================================================================
# PASSO 1: Conectar ao banco de dados SQLite e criar uma tabela
# O código deste passo foi fornecido e ligeiramente adaptado para fechar a conexão
# ==============================================================================
try:
    conexao = sqlite3.connect('dados_vendas.db')
    cursor = conexao.cursor()

    # 1.3: Criar uma tabela (usando IF NOT EXISTS para ser seguro contra execuções repetidas)
    cursor.execute('''DROP TABLE IF EXISTS vendas1''') # Limpar para garantir dados novos
    cursor.execute('''
    CREATE TABLE vendas1 (
        id_venda INTEGER PRIMARY KEY AUTOINCREMENT,
        data_venda DATE,
        produto TEXT,
        categoria TEXT,
        valor_venda REAL
    )
    ''')

    # 1.4: Inserir dados
    dados_vendas = [('2023-01-01', 'Produto A', 'Eletrônicos', 1500.00),
                    ('2023-01-05', 'Produto B', 'Roupas', 350.00),
                    ('2023-02-10', 'Produto C', 'Eletrônicos', 1200.00),
                    ('2023-03-15', 'Produto D', 'Livros', 200.00),
                    ('2023-03-20', 'Produto E', 'Eletrônicos', 800.00),
                    ('2023-04-02', 'Produto F', 'Roupas', 400.00),
                    ('2023-05-05', 'Produto G', 'Livros', 150.00),
                    ('2023-06-10', 'Produto H', 'Eletrônicos', 1000.00),
                    ('2023-07-20', 'Produto I', 'Roupas', 600.00),
                    ('2023-08-25', 'Produto J', 'Eletrônicos', 700.00),
                    ('2023-09-30', 'Produto K', 'Livros', 300.00),
                    ('2023-10-05', 'Produto L', 'Roupas', 450.00),
                    ('2023-11-15', 'Produto M', 'Eletrônicos', 900.00),
                    ('2023-12-20', 'Produto N', 'Livros', 250.00),]
    cursor.executemany(''' 
    INSERT INTO vendas1 (data_venda, produto, categoria, valor_venda) VALUES (?,?,?,?)
    ''', dados_vendas)

    # 1.5: Confirmar as mudanças
    conexao.commit()

except sqlite3.Error as e:
    print(f"Erro no SQLite: {e}")

finally:
    if 'conexao' in locals() and conexao:
        conexao.close()


# ==============================================================================
# PASSO 2: Explorar e preparar os dados
# ==============================================================================

# Conectar novamente para leitura dos dados com Pandas
conexao = sqlite3.connect('dados_vendas.db')

# 2.1: Carregar dados para um DataFrame do Pandas
query = "SELECT * FROM vendas1"
df_vendas = pd.read_sql_query(query, conexao)

# Fechar a conexão após a leitura
conexao.close()

print("--- Passo 2: Exploração Inicial ---")
print(f"Número de Linhas e Colunas: {df_vendas.shape}")
print("\nPrimeiras 5 linhas do DataFrame:")
print(df_vendas.head())
print("\nInformações sobre Tipos de Dados e Valores Nulos:")
print(df_vendas.info())

# 2.2: Preparação de Dados
# Converter 'data_venda' para o tipo datetime
df_vendas['data_venda'] = pd.to_datetime(df_vendas['data_venda'])

# Criar coluna de Mês/Ano para análise temporal
df_vendas['Mes_Venda'] = df_vendas['data_venda'].dt.to_period('M')

print("\nTipos de Dados após Conversão:")
print(df_vendas.dtypes)

# ==============================================================================
# PASSO 3: Análise dos dados
# ==============================================================================

print("\n--- Passo 3: Análise de Dados ---")

# 3.1: Análise por Categoria
analise_categoria = df_vendas.groupby('categoria').agg(
    Total_Vendas=('valor_venda', 'sum'),
    Num_Transacoes=('id_venda', 'count'),
    Valor_Medio=('valor_venda', 'mean')
).sort_values(by='Total_Vendas', ascending=False)

print("\n3.1: Vendas Consolidadas por Categoria:")
print(analise_categoria.map('{:,.2f}'.format))


# 3.2: Análise de Tendência Temporal (Mensal)
analise_mensal = df_vendas.groupby('Mes_Venda')['valor_venda'].sum().to_frame('Vendas_Mensais')

print("\n3.2: Vendas Totais por Mês:")
print(analise_mensal.map('{:,.2f}'.format))

# ==============================================================================
# PASSO 4: Visualização dos dados
# ==============================================================================

print("\n--- Passo 4: Visualização de Dados ---")

# 4.1: Gráfico de Barras: Vendas Totais por Categoria
plt.figure(figsize=(10, 6))
sns.barplot(x=analise_categoria.index, y='Total_Vendas', data=analise_categoria.reset_index(), palette='viridis')
plt.title('Vendas Totais por Categoria de Produto (2023)', fontsize=16)
plt.xlabel('Categoria', fontsize=12)
plt.ylabel('Valor Total das Vendas (R$)', fontsize=12)
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# 4.2: Gráfico de Linha: Tendência de Vendas Mensais
df_mensal_plot = analise_mensal.reset_index()
# Converter 'Mes_Venda' de Period para datetime para plotagem correta de série temporal
df_mensal_plot['Mes_Venda'] = df_mensal_plot['Mes_Venda'].astype(str)

plt.figure(figsize=(12, 6))
sns.lineplot(x='Mes_Venda', y='Vendas_Mensais', data=df_mensal_plot, marker='o', color='darkblue', linewidth=2)
plt.title('Tendência de Vendas Totais Mensais (2023)', fontsize=16)
plt.xlabel('Mês de Venda', fontsize=12)
plt.ylabel('Valor Total das Vendas (R$)', fontsize=12)
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()