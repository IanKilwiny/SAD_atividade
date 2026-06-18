import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

# Configurar página
st.set_page_config(
    page_title="Dashboard - Desempenho de Estudantes",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Carregar dados
@st.cache_data
def load_data():
    df = pd.read_csv('/home/ian/Downloads/archive/StudentsPerformance.csv')
    return df

df = load_data()

# Sidebar com informações
st.sidebar.title("📊 Dashboard de Desempenho")
st.sidebar.divider()

# Estatísticas Gerais
st.sidebar.subheader("📈 Informações do Dataset")
total_students = len(df)
total_columns = len(df.columns)
avg_math = df['math score'].mean()
avg_reading = df['reading score'].mean()
avg_writing = df['writing score'].mean()

st.sidebar.metric("Total de Estudantes", total_students)
st.sidebar.metric("Total de Colunas", total_columns)
st.sidebar.divider()

st.sidebar.subheader("📊 Médias de Desempenho")
st.sidebar.metric("Média de Matemática", f"{avg_math:.1f}")
st.sidebar.metric("Média de Leitura", f"{avg_reading:.1f}")
st.sidebar.metric("Média de Escrita", f"{avg_writing:.1f}")

st.sidebar.divider()
st.sidebar.subheader("📋 Distribuição de Dados")
st.sidebar.write(f"**Gêneros:** {df['gender'].nunique()}")
st.sidebar.write(f"**Etnias:** {df['race/ethnicity'].nunique()}")
st.sidebar.write(f"**Níveis de Educação Parental:** {df['parental level of education'].nunique()}")
st.sidebar.write(f"**Tipos de Almoço:** {df['lunch'].nunique()}")
st.sidebar.write(f"**Preparação para Testes:** {df['test preparation course'].nunique()}")

# Filtros
st.sidebar.divider()
st.sidebar.subheader("🔍 Filtros")
selected_gender = st.sidebar.multiselect(
    "Gênero",
    options=df['gender'].unique(),
    default=df['gender'].unique()
)

selected_race = st.sidebar.multiselect(
    "Raça/Etnia",
    options=df['race/ethnicity'].unique(),
    default=df['race/ethnicity'].unique()
)

selected_prep = st.sidebar.multiselect(
    "Preparação para Testes",
    options=df['test preparation course'].unique(),
    default=df['test preparation course'].unique()
)

# Aplicar filtros
df_filtered = df[
    (df['gender'].isin(selected_gender)) &
    (df['race/ethnicity'].isin(selected_race)) &
    (df['test preparation course'].isin(selected_prep))
]

# Título principal
st.title("📊 Dashboard de Desempenho de Estudantes")
st.markdown("---")

# Coluna principal com abas
tab1, tab2, tab3 = st.tabs([
    "👥 Notas por Gênero",
    "💰 Notas por Renda",
    "🎓 Notas por Preparação"
])

# TAB 1: Notas por Gênero
with tab1:
    col1, col2 = st.columns(2)
    
    with col1:
        # Média de notas por gênero
        gender_stats = df_filtered.groupby('gender')[['math score', 'reading score', 'writing score']].mean()
        fig_gender = px.bar(
            gender_stats,
            barmode='group',
            title='Média de Notas por Gênero',
            labels={'value': 'Nota Média', 'gender': 'Gênero'},
            color_discrete_sequence=['#1f77b4', '#ff7f0e', '#2ca02c']
        )
        fig_gender.update_xaxes(title_text='Gênero')
        fig_gender.update_yaxes(title_text='Nota Média')
        st.plotly_chart(fig_gender, use_container_width=True)
    
    with col2:
        # Box plot por gênero
        df_melted_gender = df_filtered.melt(
            id_vars=['gender'],
            value_vars=['math score', 'reading score', 'writing score'],
            var_name='Disciplina',
            value_name='Nota'
        )
        fig_box_gender = px.box(
            df_melted_gender,
            x='gender',
            y='Nota',
            color='Disciplina',
            title='Distribuição de Notas por Gênero e Disciplina',
            color_discrete_map={
                'math score': '#1f77b4',
                'reading score': '#ff7f0e',
                'writing score': '#2ca02c'
            }
        )
        fig_box_gender.update_xaxes(title_text='Gênero')
        fig_box_gender.update_yaxes(title_text='Nota')
        st.plotly_chart(fig_box_gender, use_container_width=True)

# TAB 2: Notas por Renda
with tab2:
    st.subheader("💰 Análise de Notas por Tipo de Almoço (Indicador de Renda)")
    
    col1, col2 = st.columns(2)
    with col1:
        lunch_counts = df_filtered['lunch'].value_counts()
        fig_lunch_pie = px.pie(
            values=lunch_counts.values,
            names=lunch_counts.index,
            title='Distribuição de Tipo de Almoço',
            color_discrete_map={'standard': '#636EFA', 'free/reduced': '#EF553B'}
        )
        st.plotly_chart(fig_lunch_pie, use_container_width=True)
    
    with col2:
        lunch_performance = df_filtered.groupby('lunch')[['math score', 'reading score', 'writing score']].mean()
        fig_lunch_bar = px.bar(
            lunch_performance,
            title='Média de Notas por Tipo de Almoço',
            barmode='group',
            color_discrete_sequence=['#1f77b4', '#ff7f0e', '#2ca02c'],
            labels={'value': 'Nota Média', 'lunch': 'Tipo de Almoço'}
        )
        fig_lunch_bar.update_layout(height=400)
        st.plotly_chart(fig_lunch_bar, use_container_width=True)

# TAB 3: Notas por Preparação
with tab3:
    col1, col2 = st.columns(2)
    
    with col1:
        # Impacto da preparação para testes
        prep_stats = df_filtered.groupby('test preparation course')[['math score', 'reading score', 'writing score']].mean()
        fig_prep = px.bar(
            prep_stats,
            barmode='group',
            title='Média de Notas por Preparação para Testes',
            labels={'value': 'Nota Média'},
            color_discrete_sequence=['#d62728', '#2ca02c', '#9467bd']
        )
        fig_prep.update_xaxes(title_text='Preparação para Testes')
        fig_prep.update_yaxes(title_text='Nota Média')
        st.plotly_chart(fig_prep, use_container_width=True)
    
    with col2:
        # Scatter plot mostrando impacto
        df_comparison = df_filtered.groupby('test preparation course')[['math score', 'reading score', 'writing score']].mean().reset_index()
        
        fig_scatter = go.Figure()
        fig_scatter.add_trace(go.Scatter(
            x=df_comparison['test preparation course'],
            y=df_comparison['math score'],
            mode='lines+markers',
            name='Matemática',
            line=dict(color='#1f77b4', width=3),
            marker=dict(size=12)
        ))
        fig_scatter.add_trace(go.Scatter(
            x=df_comparison['test preparation course'],
            y=df_comparison['reading score'],
            mode='lines+markers',
            name='Leitura',
            line=dict(color='#ff7f0e', width=3),
            marker=dict(size=12)
        ))
        fig_scatter.add_trace(go.Scatter(
            x=df_comparison['test preparation course'],
            y=df_comparison['writing score'],
            mode='lines+markers',
            name='Escrita',
            line=dict(color='#2ca02c', width=3),
            marker=dict(size=12)
        ))
        fig_scatter.update_layout(
            title='Evolução de Desempenho pela Preparação',
            xaxis_title='Preparação para Testes',
            yaxis_title='Nota Média',
            hovermode='x unified',
            height=400
        )
        st.plotly_chart(fig_scatter, use_container_width=True)
    
    # Análise de melhoria
    none_group = df_filtered[df_filtered['test preparation course'] == 'none'][['math score', 'reading score', 'writing score']].mean()
    completed_group = df_filtered[df_filtered['test preparation course'] == 'completed'][['math score', 'reading score', 'writing score']].mean()
    
    st.divider()
    st.subheader("📈 Melhoria com Preparação")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        improvement = ((completed_group['math score'] - none_group['math score']) / none_group['math score'] * 100) if none_group['math score'] > 0 else 0
        st.metric("Melhoria em Matemática", f"{improvement:.1f}%")
    
    with col2:
        improvement = ((completed_group['reading score'] - none_group['reading score']) / none_group['reading score'] * 100) if none_group['reading score'] > 0 else 0
        st.metric("Melhoria em Leitura", f"{improvement:.1f}%")
    
    with col3:
        improvement = ((completed_group['writing score'] - none_group['writing score']) / none_group['writing score'] * 100) if none_group['writing score'] > 0 else 0
        st.metric("Melhoria em Escrita", f"{improvement:.1f}%")

# Footer
st.divider()
st.markdown("""
<div style='text-align: center; color: #888; font-size: 12px; margin-top: 20px;'>
    <p>Dashboard criado com Streamlit | Dados: StudentsPerformance.csv</p>
</div>
""", unsafe_allow_html=True)
