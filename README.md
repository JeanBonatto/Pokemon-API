# 🎮 Pokemon API

Uma API RESTful para consultar informações sobre Pokémons utilizando FastAPI e Docker.

## 📋 Descrição

Esta API permite consultar informações detalhadas sobre Pokemons utilizando a PokeAPI como fonte de dados. Construída com FastAPI, oferece uma interface rápida e eficiente para buscar dados como nome, peso, altura, habilidades e muito mais.

## 🚀 Tecnologias Utilizadas

- Python 3.9
- FastAPI
- Pytest
- Docker
- Uvicorn
- Requests

## 📦 Pré-requisitos

- Python 3.10+
- Docker
- Docker Compose (opcional)

## 🛠️ Instalação e Execução

### Usando Docker

1. **Construa a imagem:**
```bash
docker build -t pokemon-api .
```

2. **Execute o container:**
```bash
docker run -p 8000:8000 pokemon-api
```

### Usando Docker Compose

```bash
docker-compose up --build
```

### Instalação Local

1. **Clone o repositório:**
```bash
git clone https://github.com/JeanBonatto/Pokemon-API.git
cd Pokemon-API
```

2. **Crie e ative um ambiente virtual:**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
.\venv\Scripts\activate   # Windows
```

3. **Instale as dependências:**
```bash
pip install -r requirements.txt
```

4. **Execute a aplicação:**
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

## 🎯 Endpoints

### GET `/pokemon/`

Retorna informações sobre um Pokémon específico.

**Parâmetros:**
- `identifier` (string/int): Nome ou ID do Pokémon
- `field` (string, opcional): Campo específico a ser retornado

**Exemplos:**

```bash
# Buscar todas as informações do Pikachu
curl "http://localhost:8000/pokemon/?identifier=pikachu"

# Buscar apenas o peso do Pikachu
curl "http://localhost:8000/pokemon/?identifier=pikachu&field=weight"
```

## 🧪 Testes

Para executar os testes:

```bash
pytest test/test_get_query_pokemon.py -v
```

## 📐 Estrutura do Projeto

```
Pokemon-API/
├── src/
│   ├── core/
│   │   └── external/
│   │       └── api_pokemon.py
│   ├── processor/
│   │   ├── data_processor.py
│   │   └── validator.py
│   └── service/
│       └── pokemon_service.py
├── test/
│   └── test_get_query_pokemon.py
├── main.py
├── requirements.txt
├── Dockerfile
└── docker-compose.yml
```


## 👥 Contribuição

Contribuições são sempre bem-vindas! Por favor, sinta-se à vontade para submeter um Pull Request.

1. Faça um Fork do projeto
2. Crie sua Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a Branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📞 Contato

Jean Bonatto - [GitHub](https://github.com/JeanBonatto)

Link do projeto: [https://github.com/JeanBonatto/Pokemon-API](https://github.com/JeanBonatto/Pokemon-API)
