# Respostas da Base de Dados

## 1. Escolha e Contexto da Base

**Dataset:** StudentsPerformance.csv - Base de dados sobre desempenho acadêmico de estudantes

**Contexto:** Dados de 1.000 estudantes com notas em três disciplinas (matemática, leitura e escrita) e informações sociodemográficas.

**Organizações que usariam:** Escolas, secretarias de educação, instituições de pesquisa educacional, plataformas de ensino online.

**Decisões apoiadas:** Identificar fatores que afetam o desempenho, priorizar intervenções educacionais, direcionar preparação para testes, ajustar políticas de acesso a alimentos.

---

## 2. Problema de Decisão

**Problema:** Como melhorar o desempenho acadêmico dos estudantes identificando fatores socioeconômicos e de preparação que influenciam as notas?

**Usuário interessado:** Diretores de escolas, professores, gestores educacionais, pais.

**Pergunta inicial:** Quais fatores (gênero, renda, preparação para testes, educação parental) mais impactam o desempenho acadêmico?

**Tipo de análise:** Descritiva e Diagnóstica. Justificativa: Primeiro descrevemos os padrões observados (médias, distribuições); depois investigamos por que ocorrem (correlações entre variáveis e fatores socioeconômicos).

---

## 3. Conhecimento Inicial da Base

| Aspecto | Valor |
|--------|-------|
| **Linhas** | 1.000 estudantes |
| **Colunas** | 8 variáveis |
| **O que cada linha representa** | Um estudante individual |
| **O que cada coluna representa** | Características do estudante ou notas |
| **Unidade de investigação** | Estudante |
| **Identificador** | Não existe (índice implícito) |

---

## 4. Classificação das Variáveis

| Variável | Descrição | Classificação |
|----------|-----------|----------------|
| gender | Gênero do estudante | Qualitativa nominal |
| race/ethnicity | Grupo étnico | Qualitativa nominal |
| parental level of education | Escolaridade dos pais | Qualitativa ordinal |
| lunch | Tipo de almoço (indicador de renda) | Qualitativa nominal |
| test preparation course | Realização de curso de preparação | Qualitativa nominal |
| math score | Nota de matemática (0-100) | Quantitativa discreta |
| reading score | Nota de leitura (0-100) | Quantitativa discreta |
| writing score | Nota de escrita (0-100) | Quantitativa discreta |

---

## 5. Qualidade dos Dados

| Problema | Variável | Tratamento |
|----------|----------|-----------|
| Sem valores ausentes | Todas | Dados completos, nenhum tratamento necessário |
| Sem registros duplicados | Todas | Integridade mantida |
| Nomes um pouco abreviados | race/ethnicity, lunch | Documentação adequada esclarece significado |
| Categorias consistentes | Todas qualitativas | Sem inconsistências detectadas |
| Valor mínimo suspeito | math score (0) | Possível estudante não compareceu; manter como está |
| Nenhuma data presente | Dados | Não aplicável |

---

## 6. Análise de Variáveis Qualitativas

### Variável 1: Gênero

| Métrica | Valor |
|---------|-------|
| **Frequência absoluta - Feminino** | 518 (51,8%) |
| **Frequência absoluta - Masculino** | 482 (48,2%) |
| **Categoria mais frequente** | Feminino |
| **Frequência relativa - Feminino** | 51,8% |
| **Frequência relativa - Masculino** | 48,2% |
| **Categorias raras/inconsistentes** | Nenhuma |
| **Gráfico utilizado** | Bar Chart (gráfico de barras agrupadas) |

### Variável 2: Tipo de Almoço (Indicador de Renda)

| Métrica | Valor |
|---------|-------|
| **Frequência absoluta - Standard** | 645 (64,5%) |
| **Frequência absoluta - Free/Reduced** | 355 (35,5%) |
| **Categoria mais frequente** | Standard |
| **Frequência relativa - Standard** | 64,5% |
| **Frequência relativa - Free/Reduced** | 35,5% |
| **Categorias raras/inconsistentes** | Nenhuma |
| **Gráfico utilizado** | Pie Chart (gráfico de pizza) |

---

## 7. Análise de Variáveis Quantitativas

### Variável 1: Nota de Matemática

| Métrica | Valor |
|---------|-------|
| **Média** | 66,09 |
| **Mediana** | 66,00 |
| **Mínimo** | 0 |
| **Máximo** | 100 |
| **Desvio padrão** | 15,16 |
| **Valores extremos** | Sim (nota 0 é suspeita) |
| **Distribuição** | Aproximadamente simétrica (média ≈ mediana) |
| **Gráficos utilizados** | Box Plot, Bar Chart |

### Variável 2: Nota de Leitura

| Métrica | Valor |
|---------|-------|
| **Média** | 69,17 |
| **Mediana** | 70,00 |
| **Mínimo** | 17 |
| **Máximo** | 100 |
| **Desvio padrão** | 14,60 |
| **Valores extremos** | Não significativos |
| **Distribuição** | Aproximadamente simétrica |
| **Gráficos utilizados** | Box Plot, Bar Chart |

### Variável 3: Nota de Escrita

| Métrica | Valor |
|---------|-------|
| **Média** | 68,05 |
| **Mediana** | 69,00 |
| **Mínimo** | 10 |
| **Máximo** | 100 |
| **Desvio padrão** | 15,20 |
| **Valores extremos** | Não significativos |
| **Distribuição** | Aproximadamente simétrica |
| **Gráficos utilizados** | Box Plot, Bar Chart, Line Chart |

---

## 8. Relação entre Variáveis

### Relação 1: Preparação para Testes × Desempenho Acadêmico

**Variáveis:** test preparation course × math/reading/writing scores

| Métrica | Sem Preparação | Com Preparação | Melhoria |
|---------|---------------|----------------|----------|
| **Math Score Médio** | 64,70 | 69,70 | +7,7% |
| **Reading Score Médio** | 66,77 | 74,21 | +11,1% |
| **Writing Score Médio** | 64,66 | 74,91 | +15,8% |

**Gráfico utilizado:** Line Chart com marcadores

**Insights:** Estudantes que completam preparação para testes melhoram significativamente em todas as disciplinas, especialmente em escrita (15,8% de melhoria).

**Decisão apoiada:** Priorizar e incentivar a participação em cursos de preparação para testes.

**Causalidade:** Não se pode afirmar com certeza. Possível confundidor: estudantes mais motivados buscam preparação E melhoram naturalmente.

---

### Relação 2: Tipo de Almoço (Renda) × Desempenho

**Variáveis:** lunch × math/reading/writing scores

**Gráfico utilizado:** Bar Chart

**Insights:** Correlação clara entre indicador de renda e desempenho. Estudantes com almoço padrão (melhor situação econômica) têm notas superiores.

**Decisão apoiada:** Implementar programas de apoio para estudantes com almoço subsidiado.

**Causalidade:** Não é direto, mas fatores como nutrição, estabilidade econômica e acesso a recursos afetam o desempenho.

---

## 9. Relação com Sistemas de Apoio à Decisão

**Decisão apoiada:** Alocação de recursos educacionais e identificação de estudantes em risco de baixo desempenho.

**Usuário do sistema:** Diretores, coordenadores pedagógicos, professores, gestores educacionais.

**Indicadores no painel:**
- Média de desempenho por disciplina
- Taxa de participação em preparação para testes
- Distribuição de desempenho por gênero e etnia
- Relação entre nível educacional parental e desempenho
- Impacto de programas de almoço subsidiado

**Alertas:**
- Estudantes com nota abaixo de 50 em qualquer disciplina
- Baixa taxa de preparação para testes
- Disparidades de desempenho entre grupos
- Alunos com notas em matemática abaixo da média

**Cuidados éticos:**
- Não discriminar por gênero, etnia ou situação econômica
- Usar dados para melhorar oportunidades, não para segregar
- Proteger privacidade dos estudantes
- Considerar fatores sociais na interpretação de resultados

**Limitações da base:**
- Sem contexto temporal (quando foi coletada?)
- Sem informações sobre tipo de escola ou região
- Sem histórico individual de progresso
- Amostra limitada (1.000 estudantes)
- Sem dados sobre qualidade do ensino ou recursos disponíveis

---

## 10. Conclusão

### Principais Achados

✅ **Preparação para testes é decisiva:** Melhora de 7,7% a 15,8% no desempenho

✅ **Fatores socioeconômicos impactam:** Almoço subsidiado correlaciona-se com notas menores

✅ **Desempenho equilibrado:** Notas em leitura e escrita são mais altas que em matemática

✅ **Dados de qualidade:** Sem ausências, sem duplicatas, bem estruturados

✅ **Correlações fortes entre disciplinas:** Leitura e escrita têm correlação de 0,95

### Recomendações

1. **Ampliar acesso a preparação**
2. **Programas de suporte**
3. **Educação parental**
4. **Análise de disparidades** 
5. **Monitoramento contínuo** 

### Cuidados
Se deve analisar por completo cada caso e sua influência. Pode existir outros fatores que podem cuminar notas baixas ou altas.

---

## Conclusão Simples sobre a Base de Dados

Os dados evidenciam que o desempenho escolar não é determinado apenas por aptidão, mas também por fatores socioeconômicos e oportunidades de preparação.

Portanto, esta base é ótima para apoiar decisões educacionais baseadas em evidências, capaz de guiar gestores na alocação de recursos e desenho de políticas que promovam equidade e melhorem os resultados de aprendizagem.


