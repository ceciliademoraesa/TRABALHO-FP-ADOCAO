# 🐾 ADOTA+ — Sistema de Adoção Facilitada

> Projeto desenvolvido para a disciplina de **Fundamentos de Programação**

---

## 📋 Sobre o Projeto

O **ADOTA+** é um sistema de adoção facilitadao desenvolvida em Python que facilita o gerenciamento de animais disponíveis. O sistema permite cadastrar animais, registrar cuidados, sugerir adotantes compatíveis, visualizar o banco de dados completo e acompanhar estatísticas do abrigo, tudo armazenado em arquivos CSV.

---

## ✅ Funcionalidades

| Opção | Funcionalidade | Status |
|---|---|---|
| `[1]` | 📝 Cadastrar animal | ✅ Implementado |
| `[2]` | 👁️ Visualizar animal | ✅ Implementado |
| `[3]` | ✏️ Editar animal | ✅ Implementado |
| `[4]` | 🗑️ Excluir animal | ✅ Implementado |
| `[5]` | 💊 Cadastrar cuidados | ✅ Implementado |
| `[6]` | ✨ Sugestões personalizadas | ✅ Implementado |
| `[7]` | 🔢 Contagem de animais | ✅ Implementado |
| `[8]` | 🤝 Sugerir adotantes | ✅ Implementado |

---

## 🗂️ Estrutura do Projeto

```
TRABALHO-FP-ADOCAO/
│
├── main.py               # Ponto de entrada do programa
├── animais.csv           # Base de dados dos animais
├── cuidados.csv          # Base de dados dos cuidados
├── adotantes.csv         # Base de dados dos adotantes
│
├── funcoes/
│   ├── cadastro.       # Funções de criação
│   ├── listagem.       # Funções de leitura
│   ├── edicao.         # Funções de edição
│   ├── remocao.       # Funções de remoção
│   ├── cuidados       # Gerenciamento de cuidados
│   ├── adotantes.     # Sugestão de adotantes
│   └── dashboard.     # Estatísticas e contagens
│   └── sugestões      #sugestões personalizadas
│
└── README.md
```


## ▶️ Como Executar

### Pré-requisitos

- Python 3.x instalado
- Nenhuma biblioteca externa necessária (uso apenas da biblioteca padrão)

### Passos

**1. Clone o repositório:**
```bash
git clone https://github.com/seu-usuario/TRABALHO-FP-ADOCAO.git
cd TRABALHO-FP-ADOCAO
```

**2. Execute o programa:**
```bash
python main.py
```

---

## 📖 Como Usar

Ao iniciar o sistema, um menu principal será exibido com as seguintes opções:

```
╔══════════════════════════════════╗
║             ADOTA+               ║
║   Sistema de adoção facilitada   ║
╠══════════════════════════════════╣
║  [1] - Cadastrar animal          ║
║  [2] - Visualizar animal         ║
║  [3] - Editar animal             ║
║  [4] - Excluir animal            ║
║  [5] - Cadastrar cuidados        ║
║  [6] - Sugestões personalizadas  ║
║  [7] - Contagem de animais       ║
║  [9] - Sugerir adotantes         ║
║  [9] - SAIR                      ║
╚══════════════════════════════════╝
```

Navegue pelo menu digitando o número da opção desejada.

---

## 💾 Armazenamento de Dados

Os dados são persistidos localmente em arquivos `.csv`:

- **`animais.csv`** — Armazena nome, espécie, raça, idade e status de cada animal
- **`cuidados.csv`** — Registra os cuidados associados a cada animal

---

## 👥 Equipe

| Nome | GitHub |
|---|---|
| Cecília de Moraes | [@ceciliademoraesa](https://github.com/ceciliademoraesa) |
| Letícia Carvalho | [@leticiacarvb](https://github.com/leticiacarvb) |
| Lívia Buonora | [@liviabuonora](https://github.com/liviabuonora) |
| Luiza Beltrão | [@luizabpm](https://github.com/luizabpm) |
| Suri Savitri | [@SuriSavitri](https://github.com/SuriSavitri) |
| Victor Bacelar | [@victorbpalazzin](https://github.com/victorbpalazzin) |

---

## 📚 Disciplina

- **Disciplina:** Fundamentos de Programação
- **Instituição:** *CESAR SCHOOL*


---

