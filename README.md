# DoculA Parser API

Microsserviço responsável por analisar código-fonte e extrair informações estruturadas para geração de diagramas UML.

Este serviço faz parte do **Módulo 5 — Diagramas e Documentos Técnicos** da plataforma DoculA.

O Parser API recebe código-fonte, identifica classes, atributos e métodos e retorna esses dados em formato JSON para serem utilizados pela **Diagram API** na geração de diagramas UML.

## Arquitetura

```txt
Frontend
   ↓
Gateway API
   ↓
Parser API
   ↓
Diagram API
````

## Responsabilidades do Parser API

* Receber código-fonte enviado pelo Gateway API;
* Analisar a estrutura do código;
* Identificar classes;
* Identificar atributos;
* Identificar métodos;
* Retornar um JSON estruturado;
* Servir como base para geração automática de diagramas UML.

## Deploy em Produção

### Parser API

```txt
https://diagramas-parser-e6dzc7f5ateae3ce.canadacentral-01.azurewebsites.net
```

### Swagger/OpenAPI do Parser

```txt
https://diagramas-parser-e6dzc7f5ateae3ce.canadacentral-01.azurewebsites.net/docs
```

### Gateway API

```txt
https://docula-gateway-api-dzgfg8ghghadeedd.eastus-01.azurewebsites.net/
```

### Diagram API

```txt
https://diagramas-diagram-eugce0h0bygfdqhf.canadacentral-01.azurewebsites.net
```

## Requisitos

* Python 3.10+
* FastAPI
* Uvicorn
* Pydantic

## Instalação

```powershell
pip install -r requirements.txt
```

## Como executar localmente

Execute o serviço com:

```powershell
python -m uvicorn app.main:app --reload
```

A aplicação ficará disponível em:

```txt
http://127.0.0.1:8000
```

Swagger/OpenAPI local:

```txt
http://127.0.0.1:8000/docs
```

Caso esteja executando junto com o Gateway e o Diagram API, recomenda-se usar a porta `8001`:

```powershell
python -m uvicorn app.main:app --reload --port 8001
```

## Endpoints

### Health check

```http
GET /health
```

Exemplo de resposta:

```json
{
  "status": "ok",
  "service": "docula-parser-api"
}
```

### Analisar código-fonte

```http
POST /parse/class
```

Exemplo de entrada:

```json
{
  "source_code": "public class Usuario { private String nome; private String email; public void login() { } public void logout() { } }"
}
```

Exemplo de resposta:

```json
{
  "classes": [
    {
      "name": "Usuario",
      "attributes": ["nome", "email"],
      "methods": ["login", "logout"]
    }
  ]
}
```

## Fluxo de funcionamento

```txt
1. O usuário envia código-fonte pelo frontend.
2. O frontend chama o Gateway API.
3. O Gateway envia o código para o Parser API.
4. O Parser API identifica classes, atributos e métodos.
5. O Parser API retorna os dados estruturados para o Gateway.
6. O Gateway envia esses dados para a Diagram API.
7. A Diagram API gera o PlantUML.
8. O resultado retorna para o frontend.
```

## Papel na integração com outros microsserviços

Este microsserviço não é consumido diretamente pelo usuário final.

Ele é chamado pelo **Gateway API**, que centraliza a comunicação entre os serviços do Módulo 5.

```txt
Gateway API → Parser API → Dados estruturados
```

Os dados retornados pelo Parser API são utilizados pela Diagram API para gerar diagramas UML.

## Exemplo de integração

Entrada enviada pelo Gateway:

```json
{
  "source_code": "public class Produto { private String nome; private double preco; public void atualizarPreco() { } }"
}
```

Resposta do Parser API:

```json
{
  "classes": [
    {
      "name": "Produto",
      "attributes": ["nome", "preco"],
      "methods": ["atualizarPreco"]
    }
  ]
}
```

Essa resposta pode ser enviada para a Diagram API para gerar um diagrama UML em PlantUML.

## Tecnologias utilizadas

* Python
* FastAPI
* Uvicorn
* Pydantic
* Regex
* Azure App Service

## Deploy

O serviço está preparado para deploy em **Azure App Service**.

Startup command utilizado:

```bash
python -m uvicorn app.main:app --host 0.0.0.0 --port 8000
```

## Versionamento

O projeto utiliza versionamento semântico.

Versão atual:

```txt
v0.1.1
```

Histórico inicial:

```txt
v0.1.0 - Primeira versão funcional do Parser API com extração de classes, atributos e métodos
v0.1.1 - Preparação para deploy Azure
```

## Limitações atuais

Na versão atual, o Parser API utiliza uma estratégia simples baseada em expressões regulares.

Funciona melhor com códigos Java simples, como:

```java
public class Usuario {
    private String nome;
    private String email;

    public void login() { }
    public void logout() { }
}
```

## Funcionalidades futuras

* Melhorar suporte a múltiplas classes no mesmo arquivo;
* Identificar relacionamentos entre classes;
* Identificar herança e interfaces;
* Suportar outras linguagens, como Python e JavaScript;
* Extrair endpoints REST;
* Integrar IA para melhorar a análise semântica do código;
* Detectar padrões arquiteturais e padrões de projeto.
