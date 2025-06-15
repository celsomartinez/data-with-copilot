# CLI de Manipulação de DataFrame

Este projeto fornece uma interface de linha de comando (CLI) para manipular e transformar dados tabulares armazenados em arquivos CSV, utilizando apenas Python e a biblioteca padrão.

## Sumário

- [Objetivo](#objetivo)
- [Natureza dos Dados](#natureza-dos-dados)
- [Instalação](#instalação)
- [Uso](#uso)
- [Comandos Disponíveis](#comandos-disponíveis)
- [Exemplos](#exemplos)
- [Contribuindo](#contribuindo)
- [Licença](#licença)

## Objetivo

Facilitar a transformação e preparação de dados para pipelines de dados e ambientes CI/CD, utilizando comandos simples e diretos via terminal.

## Natureza dos Dados

Os dados utilizados estão nos arquivos [`train.csv`](../train.csv) (original) e [`transformed_train.csv`](../transformed_train.csv) (transformado), ambos localizados na pasta `workshop/`. As principais colunas são:

- **notes**: Notas de texto sobre os dados.
- **rating**: Classificações numéricas.
- **variety**: Tipo ou variedade (ex: 'Red Wine').

## Instalação

1. Clone o repositório:
    ```sh
    git clone https://github.com/seu-usuario/seu-repo.git
    cd seu-repo/workshop
    ```
2. (Opcional) Crie e ative um ambiente virtual:
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```
3. Instale as dependências:
    ```sh
    pip install -r requirements.txt
    ```

## Uso

Execute os comandos a partir do diretório `workshop`:

```sh
python main.py <comando>
```

Para ver o menu de ajuda:

```sh
python main.py -h
```

## Comandos Disponíveis

- `drop_notes`: Remove a coluna `notes` do DataFrame.
- `select_high_ratings`: Seleciona linhas onde `rating` é 90 ou superior.
- `drop_and_one_hot_encode_red_wine`: Codifica a categoria 'Red Wine' e remove a coluna `variety`.
- `remove_newlines_carriage_returns`: Remove quebras de linha das colunas de texto.
- `convert_ratings_to_int`: Converte a coluna `rating` para inteiro.

## Exemplos

Remover a coluna `notes`:
```sh
python main.py drop_notes
```

Selecionar linhas com classificações altas:
```sh
python main.py select_high_ratings
```

Codificação one-hot para 'Red Wine':
```sh
python main.py drop_and_one_hot_encode_red_wine
```

Remover quebras de linha:
```sh
python main.py remove_newlines_carriage_returns
```

Converter `rating` para inteiro:
```sh
python main.py convert_ratings_to_int
```

## Contribuindo

Contribuições são bem-vindas! Abra um pull request ou issue para sugerir melhorias.

## Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](../../LICENSE) para mais detalhes.