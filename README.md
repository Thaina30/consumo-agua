# 💧 Classificador de Consumo de Água

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)
![VS Code](https://img.shields.io/badge/VS%20Code-007ACC?style=for-the-badge&logo=visualstudiocode&logoColor=white)
![Sustentabilidade](https://img.shields.io/badge/Sustentabilidade-2E7D32?style=for-the-badge&logo=leaflet&logoColor=white)
![Licença MIT](https://img.shields.io/badge/Licença-MIT-yellow?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Concluído-success?style=for-the-badge)

## 🌱 Sobre o projeto

Sistema desenvolvido para a campanha de conscientização ambiental da companhia de
saneamento. O programa recebe o **tipo do imóvel** e o **consumo mensal de água**
em metros cúbicos (m³), classifica o perfil de consumo e exibe um **alerta
educativo** orientando o morador sobre economia de água e possíveis vazamentos.

**Objetivo:** estimular o uso consciente da água por meio de um retorno imediato
e simples sobre o padrão de consumo de cada imóvel.

## 🛠️ Tecnologia

- **Linguagem:** Python 3 🐍
- **Dependências:** nenhuma (apenas a biblioteca padrão)
- **Execução:** terminal / linha de comando

## 📋 Regras de negócio

| Tipo do imóvel | Consumo mensal | Mensagem exibida |
|---|---|---|
| 🏢 Comercial | qualquer valor | Tarifa comercial aplicada – consulte o plano corporativo. |
| 🏬 Apartamento | menor que 10 m³ | Consumo econômico – excelente controle de água! |
| 🏬 Apartamento / 🏠 Casa | até 25 m³ | Consumo moderado – dentro do padrão residencial. |
| 🏬 Apartamento / 🏠 Casa | acima de 25 m³ | Consumo excessivo – adote medidas de economia e verifique vazamentos. |

## ▶️ Como executar

1. Instale o [Python 3](https://www.python.org/downloads/) (versão 3.8 ou superior).
2. Clone o repositório:
   ```bash
   git clone https://github.com/SEU-USUARIO/SEU-REPOSITORIO.git
   ```
3. Acesse a pasta do projeto:
   ```bash
   cd SEU-REPOSITORIO/consumo-agua
   ```
4. Execute o programa:
   ```bash
   python app.py
   ```

## 💻 Exemplo de uso

```text
=== Classificação de Consumo de Água ===
Tipo do imóvel (comercial / casa / apartamento): apartamento
Consumo mensal de água (m3): 8.5

--- Resultado ---
Imóvel: Apartamento
Consumo: 8.50 m3
Consumo econômico - excelente controle de água!
```

## 📁 Estrutura do repositório

```text
.
└── consumo-agua/
    ├── app.py       # código-fonte do programa
    └── README.md    # documentação do projeto
```

## 🚿 Dicas de economia de água

- Reduza o tempo de banho para até 5 minutos.
- Feche a torneira ao escovar os dentes ou ensaboar a louça.
- Verifique periodicamente vazamentos em caixas d'água e válvulas.
- Reaproveite a água da máquina de lavar para limpeza de áreas externas.

## 👤 Autora
Thaina Rodrigues de Almeida

---

<p align="center">💧 Água é vida. Use com consciência. 🌍</p>