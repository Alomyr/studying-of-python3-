# 📄 Micro Projeto – Registro de Pessoas em Arquivo

Este micro projeto em **Python** grava nomes e idades em um arquivo de texto, mantendo **alinhamento e espaçamento padronizados** entre os dados para facilitar a leitura.

---

## 🎯 Objetivo

Garantir que todos os nomes ocupem a mesma largura no arquivo, fazendo com que as idades fiquem alinhadas em coluna, independentemente do tamanho do nome.

---

## 🛠️ Tecnologias e Conceitos

- Python 3
- Escrita em arquivos (`open`, `write`)
- Formatação de strings com **f-strings**
- Alinhamento de texto com largura fixa

---

## 📂 Estrutura do Projeto

```txt
├── venv/                  # Ambiente virtual (não versionar)
│
├── src/
│   └── micro-projeto-registro/
│       │
│       ├── Menu/
│       │   ├── __init__.py
│       │   └── menu.py
│       │
│       ├── Utils/
│       │   ├── __init__.py
│       │   ├── cadastradas.py
│       │   ├── cadastro.py
│       │   └── render.py
│       │
│       ├── main.py         # Arquivo principal do sistema
│       └── README.md       # Documentação do projeto

```

## 📊 Exemplo de Saída no Arquivo

        matheus        21
        bruna          21
        fulano         19

## 🚀 Vantagens

- Código simples e legível

- Saída organizada em formato de tabela

- Fácil adaptação para outros tipos de dados

## 🧠 Observação

## ▶️ Como Executar

- Certifique-se de ter o Python 3 instalado:

        python --version

- Clone este repositório:

        git clone <https://github.com/Alomyr/studying-of-python3-.git>

- Acesse a pasta do projeto:

        cd micro-projeto-registro

- Execute o programa:

        python main.py

Após a execução, o arquivo Cadastro.txt será criado ou atualizado com os registros formatados.
