# 📊 Dashboard de Desempenho de Estudantes

Um dashboard interativo criado em Python com Streamlit para visualizar e analisar dados de desempenho de estudantes.

## 🎯 Funcionalidades

O dashboard inclui as seguintes visualizações e análises:

### 📊 Visão Geral
- Estatísticas gerais (total de estudantes, médias por disciplina)
- Distribuição de notas em Matemática, Leitura e Escrita
- Box plots comparativos entre disciplinas

### 📈 Análise por Gênero
- Comparação de desempenho entre gêneros
- Distribuição de notas por gênero
- Estatísticas detalhadas

### 🎓 Impacto da Preparação para Testes
- Análise do impacto de cursos de preparação
- Cálculo de melhoria percentual
- Comparação antes/depois

### 👥 Análise por Raça/Etnia
- Desempenho por grupo étnico
- Comparação entre grupos
- Estatísticas por grupo

### 🔗 Correlações
- Matriz de correlação entre disciplinas
- Scatter plots com linhas de tendência
- Análise de relações entre variáveis

## 🚀 Como Usar

### 1. Instalação de Dependências

```bash
pip install -r requirements.txt
```

### 2. Executar o Dashboard

```bash
streamlit run app.py
```

O dashboard será aberto automaticamente no seu navegador padrão em `http://localhost:8501`

## 🔍 Filtros Disponíveis

Use a barra lateral para filtrar os dados por:
- **Gênero**: Selecione "female", "male" ou ambos
- **Raça/Etnia**: Escolha entre Group A, B, C, D ou E
- **Preparação para Testes**: Veja dados com ou sem preparação

## 📁 Estrutura do Projeto

```
sad=atv/
├── app.py                      # Arquivo principal do dashboard
├── requirements.txt            # Dependências do projeto
└── README.md                   # Este arquivo
```

## 🔧 Requisitos do Sistema

- Python 3.8+
- pip (gerenciador de pacotes Python)

## 📊 Dados

O dashboard utiliza o arquivo `StudentsPerformance.csv` localizado em:
```
/home/ian/Downloads/archive/StudentsPerformance.csv
```

### Colunas do Dataset
- `gender`: Gênero do estudante (female/male)
- `race/ethnicity`: Raça/etnia (Group A-E)
- `parental level of education`: Nível de educação dos pais
- `lunch`: Tipo de almoço (standard/free/reduced)
- `test preparation course`: Preparação para testes (none/completed)
- `math score`: Nota em Matemática (0-100)
- `reading score`: Nota em Leitura (0-100)
- `writing score`: Nota em Escrita (0-100)

## 💡 Dicas

1. **Filtros**: Use os filtros da sidebar para criar visualizações personalizadas
2. **Hover**: Passe o mouse sobre os gráficos para ver detalhes
3. **Abas**: Navegue entre as diferentes análises usando as abas no topo
4. **Responsividade**: O dashboard se adapta a diferentes tamanhos de tela

## 📈 Interpretação dos Dados

- **Correlação**: Valores próximos a 1 indicam forte relação positiva
- **Distribuição**: Histogramas mostram a concentração de notas
- **Box plots**: Revelam mediana, quartis e outliers
- **Linhas de tendência**: Mostram a relação linear entre variáveis

## 🎨 Cores Utilizadas

- Matemática: Azul (#1f77b4)
- Leitura: Laranja (#ff7f0e)
- Escrita: Verde (#2ca02c)

## 📝 Notas

- Os dados são carregados em cache para melhor performance
- Todas as visualizações são interativas (zoom, pan, download)
- Os filtros afetam todos os gráficos em tempo real

## ✨ Melhorias Futuras

- Exportar relatórios em PDF
- Análise de regressão mais avançada
- Previsão de desempenho
- Comparação de períodos

---

**Criado com ❤️ usando Streamlit**
# SAD_atividade
