# 🚢 Simulador de Operações Portuárias

Simulação de um sistema de gerenciamento portuário desenvolvida em **Python**, utilizando exclusivamente **Tipos Abstratos de Dados (TADs)** implementados do zero.

O projeto reproduz o fluxo de operação de um porto, controlando a chegada de navios, filas de prioridade, atracação em docas e movimentação de contêineres utilizando estruturas clássicas de Estruturas de Dados.

> Projeto desenvolvido para a disciplina de **Estruturas de Dados e Algoritmos**.

---

## 📌 Objetivos

* Aplicar conceitos de Estruturas de Dados na resolução de um problema real.
* Implementar TADs sem utilizar estruturas prontas da linguagem.
* Simular o fluxo operacional de um porto de cargas.
* Analisar a eficiência das estruturas utilizadas.

---

## ⚙️ Funcionalidades

* ✅ Geração automática de navios
* ✅ Geração automática de contêineres
* ✅ Cadastro de docas
* ✅ Controle de pátios de armazenamento
* ✅ Fila de prioridade para navios
* ✅ Simulação completa de carga e descarga
* ✅ Processamento por ciclos
* ✅ Relatórios resumidos da operação

---

# 🏗 Arquitetura

```
Porto
│
├── Docas
│   ├── Pátio
│   │    ├── Pilhas de Containers
│   │    └── Containers
│   │
│   └── Navio
│        ├── Pilhas
│        └── Containers
│
└── Fila de Prioridade
```

---

# 🧩 Estruturas de Dados Implementadas

Este projeto implementa todas as estruturas manualmente.

| Estrutura                  | Aplicação                     |
| -------------------------- | ----------------------------- |
| Lista Duplamente Encadeada | Base para todas as estruturas |
| Pilha (LIFO)               | Armazenamento de contêineres  |
| Fila                       | Estrutura auxiliar            |
| Fila de Prioridade         | Ordem de chegada dos navios   |

---

# 🚢 Funcionamento

1. O porto é inicializado.
2. As docas são criadas.
3. Os pátios recebem contêineres aleatórios.
4. Os navios são gerados e inseridos na fila de prioridade.
5. O navio de maior prioridade atraca.
6. Todos os contêineres são descarregados.
7. O navio recebe novos contêineres do pátio.
8. O navio deixa a doca.
9. O próximo navio é processado.

---

# 📊 Complexidade

## Lista Encadeada

| Operação | Complexidade |
| -------- | ------------ |
| Inserção | **O(1)**     |
| Remoção  | **O(1)**     |
| Busca    | **O(n)**     |

---

## Pilha

| Operação | Complexidade |
| -------- | ------------ |
| Push     | **O(1)**     |
| Pop      | **O(1)**     |
| Top      | **O(1)**     |

---

## Fila de Prioridade

| Operação | Complexidade |
| -------- | ------------ |
| Inserção | **O(1)**     |
| Remoção  | **O(1)**     |

A fila foi implementada utilizando quatro filas independentes (uma para cada nível de prioridade), garantindo acesso constante ao próximo navio a ser atendido.

---

## Complexidade da Simulação

Considerando:

* **N** = quantidade de navios
* **C** = quantidade média de contêineres por navio

Cada contêiner é movimentado apenas uma vez durante a simulação.

**Complexidade total:**

```
O(N × C)
```

---

# 📁 Estrutura do Projeto

```
.
├── main.py
├── simulador.py
├── gerador.py
│
├── entidades
│   ├── cContainer.py
│   ├── cNavio.py
│   ├── cPatio.py
│   ├── cDoca.py
│   └── cPorto.py
│
└── TAD
    ├── cNo.py
    ├── cListaEncad.py
    ├── cPilha.py
    ├── cFila.py
    └── cFilaPrioridade.py
```

---

# ▶️ Como executar

Clone o repositório:

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
```

Execute:

```bash
python main.py
```

Ou informe a quantidade de docas e navios:

```bash
python main.py 3 10
```

---

# 🛠 Tecnologias

* Python 3
* Programação Orientada a Objetos
* Tipos Abstratos de Dados (TAD)
* Estruturas de Dados
* Algoritmos

---

# 📚 Conceitos Aplicados

* Listas Encadeadas
* Pilhas
* Filas
* Filas de Prioridade
* Encapsulamento
* Abstração
* Modularização
* Simulação de Sistemas
* Análise de Complexidade

---

# Referências

[1] CORMEN, T. H.; LEISERSON, C. E.; RIVEST, R. L.; STEIN, C. Algoritmos: Teoria e Prática. 3. ed. Rio de Janeiro: Campus, 2012.

[2] CANNING, J.; BRODER, A.; LAFORE, R. Data Structures & Algorithms in Python. Addison-Wesley, 2022.

[3] VARTANIAN, Erica. 6 Coding Best Practices for Beginner Programmers. Disponível em: https://www.educative.io/blog/coding-best-practices

[4] CONE, Matt. Markdown Cheat Sheet - A Quick Reference to the Markdown Syntax. Disponível em: https://www.markdownguide.org/cheat-sheet/

---

## 👨‍💻 Autor

**Raphael Carneiro**

Estudante de Ciências e Tecnologia com foco em **Estruturas de Dados, Algoritmos, Desenvolvimento Backend e Inteligência Artificial**.

[GitHub](https://github.com/RaphaelCarneiroDev)