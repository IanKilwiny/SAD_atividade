#!/bin/bash

# Script para instalar dependências e executar o dashboard

echo "======================================="
echo "Dashboard de Desempenho de Estudantes"
echo "======================================="
echo ""

# Verificar se Python está instalado
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 não está instalado!"
    echo "Por favor, instale Python 3.8 ou superior"
    exit 1
fi

echo "✅ Python encontrado: $(python3 --version)"
echo ""

# Criar ambiente virtual se não existir
if [ ! -d "venv" ]; then
    echo "📦 Criando ambiente virtual..."
    python3 -m venv venv
    echo "✅ Ambiente virtual criado"
    echo ""
fi

# Ativar ambiente virtual
echo "🔌 Ativando ambiente virtual..."
source venv/bin/activate
echo "✅ Ambiente ativado"
echo ""

# Instalar dependências
echo "📥 Instalando dependências..."
pip install -q -r requirements.txt
echo "✅ Dependências instaladas"
echo ""

# Executar Streamlit
echo "🚀 Iniciando dashboard..."
echo "O dashboard será aberto em: http://localhost:8501"
echo ""
streamlit run app.py
