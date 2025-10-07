# 🧠 Projeto: Perfil Econômico e Social das Cidades do Nordeste Brasileiro  

📊 Este projeto tem como objetivo **construir um perfil econômico e social** das cidades do **Nordeste do Brasil**, utilizando **dados abertos do Governo Federal** e da **API do IBGE**.  

A iniciativa busca reunir, tratar e consolidar informações sobre população, educação, renda e acesso a serviços, oferecendo uma **visão abrangente e interativa** da realidade socioeconômica da região.  

---

## 🧩 Estrutura do Projeto  

O projeto é composto por **4 códigos principais**, cada um com uma função específica:  

### 1️⃣ `endpoints.py`  
🔹 Responsável por **processar os endpoints da API do IBGE**, obtendo dados sobre:  
- População em **zonas urbana e rural**  
- **Acesso à internet**  
- **Escolaridade**  
- **Quantidade de famílias**  
- **Municípios**  

⚠️ Como a API do IBGE ainda **não está totalmente atualizada com o Censo 2022**, o código foi complementado com dados em **formato CSV**, provenientes do portal de **dados abertos do governo**.  

---

### 2️⃣ `planilhas.py`  
📂 Processa os arquivos CSV que contêm informações sobre:  
- **Cadastro do Bolsa Família**  
- **Faixas salariais**  
- **Situação econômica geral por renda**  

💡 Esse código gera um **DataFrame consolidado**, posteriormente utilizado no código final.  

---

### 3️⃣ `processando_dados.py`  
🧹 Responsável por **tratar e padronizar** todas as informações coletadas, garantindo consistência e qualidade dos dados.  
O objetivo é deixar as tabelas **limpas, organizadas e prontas** para a análise.  

---

### 4️⃣ `censo2022agregados.py`  
🧾 Une todas as bases tratadas e gera o **DataFrame final**, consolidando os indicadores econômicos e sociais das cidades nordestinas.  

---

## 🚀 Resultado Final  

O produto final será apresentado em um **dashboard interativo no Power BI**, permitindo:  
- Uma **visualização dinâmica e intuitiva** das informações  
- Um **entendimento aprofundado** das características socioeconômicas da região  
- Aplicações práticas em **projetos futuros de análise e tomada de decisão**  

---

## 🛠️ Tecnologias Utilizadas  

| Tecnologia | Descrição |
|-------------|------------|
| 🐍 **Python** | Linguagem principal utilizada para coleta, tratamento e integração dos dados |
| 📦 **Pandas** | Manipulação e análise de dados |
| 🌐 **Requests** | Acesso à API do IBGE |
| 📊 **Power BI** | Criação do dashboard interativo |
| 🧾 **CSV / Dados Abertos** | Fontes complementares ao Censo IBGE |

