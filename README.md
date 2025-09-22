# Sistema de Controle de Consumo de Insumos

Sistema para gestão e controle do consumo de insumos em unidades de diagnóstico, com registro preciso de retiradas e funcionalidades avançadas de busca e ordenação.

## 📋 Funcionalidades

- **Registro de Retiradas**: Controle completo das retiradas de insumos com data e quantidade
- **Visualização em Ordem Cronológica**: Histórico completo em ordem de ocorrência (Fila)
- **Visualização em Ordem Inversa**: Últimas retiradas realizadas (Pilha)
- **Ordenação Avançada**: Ordenação por quantidade ou data usando Merge Sort e Quick Sort
- **Busca Eficiente**: Busca sequencial e binária por insumos
- **Gestão de Estoque**: Controle de quantidades disponíveis

## 🚀 Como Executar

1. Certifique-se de ter Python 3.7+ instalado
2. Clone ou baixe os arquivos do projeto
3. Execute o comando:
   ```bash
   python main.py
   ```

## 🏗️ Estrutura do Projeto

```
/
├── models/
│   └── insumo.py          # Classe Insumo para representação dos dados
├── services/
│   ├── generator.py       # Geração de dados simulados
│   ├── registro_consumo.py # Gerenciamento de filas e pilhas
│   └── busca_ordenacao.py # Implementações de busca
├── structures/
│   ├── queue.py          # Implementação de Fila
│   ├── stack.py          # Implementação de Pilha
│   ├── sort.py           # Algoritmos de ordenação
│   └── search.py         # Algoritmos de busca
└── main.py               # Interface principal do sistema
```

## 📊 Complexidade dos Algoritmos

### 1. Merge Sort - O(n log n)
**Arquivo**: `structures/sort.py` (linhas 1-20)
- Algoritmo de ordenação por divisão e conquista
- Divide a lista recursivamente até listas unitárias e depois as combina ordenadamente

### 2. Busca Binária - O(log n)
**Arquivo**: `services/busca_ordenacao.py` (linhas 15-40)
- Busca eficiente em listas ordenadas
- Reduz o espaço de busca pela metade a cada iteração

### 3. Registro na Fila - O(1)
**Arquivo**: `structures/queue.py` (linhas 5-7)
- Inserção constante no final da fila
- Operação de tempo constante independente do tamanho da fila

### 4. Busca Sequencial - O(n)
**Arquivo**: `services/busca_ordenacao.py` (linhas 1-8)
- Percorre todos os elementos até encontrar o desejado
- Simples mas ineficiente para grandes volumes de dados

## 🧩 Onde Cada Estrutura/Algoritmo é Utilizado

### Fila (Queue)
**Arquivo**: `structures/queue.py`
- Utilizada para manter o histórico completo de retiradas em ordem cronológica
- Simula o fluxo natural de consumo (primeiro a entrar, primeiro a sair)
- Implementada no registro de consumo em `services/registro_consumo.py`

### Pilha (Stack)
**Arquivo**: `structures/stack.py`
- Utilizada para visualizar as últimas retiradas realizadas (ordem inversa)
- Permite consulta rápida das operações mais recentes
- Implementada no registro de consumo em `services/registro_consumo.py`

### Busca Binária
**Arquivo**: `services/busca_ordenacao.py` (linhas 15-40)
- Utilizada para localizar rapidamente insumos no registro ordenado
- Requer que os dados estejam previamente ordenados por nome
- Acessada através da opção 7 no menu principal

### Merge Sort e Quick Sort
**Arquivo**: `structures/sort.py`
- Merge Sort: utilizado para ordenar insumos por quantidade (opção 2)
- Quick Sort: utilizado para ordenar insumos por data (opção 3)
- Ambos permitem organização eficiente dos dados para análise e tomada de decisão

## 👨‍💻 Utilização do Sistema

1. Ao iniciar, o sistema pergunta se deseja carregar um histórico simulado
2. O menu principal oferece 7 opções:
   - Registrar nova retirada de insumo
   - Ordenar e visualizar por quantidade (Merge Sort)
   - Ordenar e visualizar por data (Quick Sort)
   - Visualizar histórico completo (Fila)
   - Visualizar últimas retiradas (Pilha)
   - Buscar por insumo (Busca Sequencial)
   - Buscar por insumo (Busca Binária)

## 🎯 Objetivo do Projeto

Este sistema foi desenvolvido para resolver o problema de falta de precisão no registro de consumo diário de insumos em unidades de diagnóstico, facilitando o controle de estoque e a previsão de reposição através de estruturas de dados e algoritmos clássicos.

## 📝 Notas de Desenvolvimento

- Implementado em Python com orientação a objetos
- Interface amigável para usuários finais
- Formatação de datas no padrão brasileiro (dd/mm/aaaa)
- Mensagens claras e informativas em português