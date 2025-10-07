🧠 Projeto: Perfil Econômico e Social das Cidades do Nordeste Brasileiro

📊 Este projeto tem como objetivo construir um perfil econômico e social das cidades do Nordeste do Brasil, utilizando dados abertos do Governo Federal e da API do IBGE.

🧩 Estrutura do Projeto

O projeto é composto por 4 códigos principais, cada um com uma função específica:

1️⃣ endpoints.py

🔹 Responsável por processar os endpoints da API do IBGE, obtendo dados sobre:

População em zonas urbana e rural

Acesso à internet

Escolaridade

Quantidade de famílias

Municípios

⚠️ Como a API do IBGE ainda não está totalmente atualizada com o Censo 2022, foi necessário complementar as informações com dados em formato CSV provenientes do portal de dados abertos do governo.

2️⃣ planilhas.py

📂 Processa os arquivos CSV, que trazem informações sobre:

Cadastro do Bolsa Família

Faixas salariais

Situação econômica geral por renda

💡 Esse código gera um DataFrame consolidado, que será utilizado posteriormente no código final.

3️⃣ processando_dados.py

🧹 Responsável por tratar e formatar todas as informações coletadas, garantindo consistência e qualidade dos dados.
O objetivo é deixar os dados prontos para análise e integração no DataFrame final.

4️⃣ censo2022agregados.py

🧾 Une todas as bases tratadas e gera o DataFrame final, que consolida os indicadores econômicos e sociais das cidades nordestinas.

🚀 Resultado Final

O produto final será apresentado em um dashboard interativo no Power BI, permitindo:

Uma visualização dinâmica das informações

Um entendimento mais profundo das características socioeconômicas da região

Aplicações práticas para futuros projetos de análise e tomada de decisão

✨ Em resumo:
Este projeto une dados públicos, Python e visualização interativa para transformar informações dispersas em insights valiosos sobre o Nordeste brasileiro 🇧🇷
