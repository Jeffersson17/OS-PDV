#!/bin/bash

echo "Iniciando correção automática de linting..."

# Organizar importações com isort
echo "Organizando importações com isort..."
isort .

# Formatar código com black
echo "Formatando código com black..."
black --line-length 79 .

# Remover importações e código não utilizado com autoflake
echo "Removendo importações e código não utilizado com autoflake..."
autoflake --remove-all-unused-imports --recursive --remove-unused-variables --in-place .

# Rodar flake8 para verificar problemas restantes
echo "Verificando problemas com flake8..."
flake8 .

echo "Correção automática concluída!"
