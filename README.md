# Python Scripts para Transformações de Dados e Integração com a API Oruc

Este repositório contém uma coleção de scripts em Python projetados para realizar operações de transformação de dados, integração com a API da plataforma Oruc, e manipulação de arquivos CSV e banco de dados SQL Server.

## Estrutura dos Scripts

### 1. Conexão com o Banco de Dados
- **db_connection.py**: Estabelece uma conexão com um banco de dados SQL Server usando as variáveis de ambiente configuradas. Este módulo é utilizado para conectar-se ao banco e executar operações SQL.

### 2. Integração com a API Oruc
- **get_produtos_oruc.py**: Recupera uma lista de produtos da API da plataforma Oruc. A resposta é salva em um arquivo `json-response.txt` e também exibida no console.
  
- **upload_imagens_pcv.py**: Realiza o upload de imagens para produtos com variações de modelos (PVC) na loja da plataforma Oruc. As imagens são convertidas para base64 antes do upload. As pastas de imagens devem seguir o padrão `[código do produto]-[nome do modelo]`.
  
- **upload_imagens_psv.py**: Similar ao script anterior, mas destinado a produtos sem variações de modelos (PSV). As pastas de imagens devem ser nomeadas apenas com o código do produto.

### 3. Manipulação de Arquivos CSV
- **get_refs.py**: Lê um arquivo CSV e filtra itens baseados em condições específicas. As referências selecionadas são exibidas no console.
  
- **insert_maker.py**: Gera comandos SQL `INSERT` para adicionar novos registros na tabela `DEPARTAMENTO` com base em um arquivo CSV de produtos distintos.
  
- **update_maker.py**: Gera comandos SQL `UPDATE` para atualizar a tabela `PRODUTO`, associando produtos a seus respectivos departamentos com base em arquivos CSV.
