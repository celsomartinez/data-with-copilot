import argparse
import pandas as pd

def drop_notes(df):
    if 'notes' in df.columns:
        df = df.drop(columns=['notes'])
    return df

def select_high_ratings(df):
    if 'rating' in df.columns:
        df = df[df['rating'] >= 90]
    return df

def drop_and_one_hot_encode_red_wine(df):
    if 'variety' in df.columns:
        df['is_red_wine'] = (df['variety'] == 'Red Wine').astype(int)
        df = df.drop(columns=['variety'])
    return df

def remove_newlines_carriage_returns(df):
    for col in df.select_dtypes(include=['object']):
        df[col] = df[col].str.replace('\n', ' ').str.replace('\r', ' ')
    return df

def convert_ratings_to_int(df):
    if 'rating' in df.columns:
        df['rating'] = df['rating'].astype(int)
    return df

def main():
    parser = argparse.ArgumentParser(
        description="Ferramenta de linha de comando para manipulação de DataFrame."
    )
    subparsers = parser.add_subparsers(dest="command", help="Comando a ser executado")

    subparsers.add_parser("drop_notes", help="Remove a coluna 'notes' do DataFrame")
    subparsers.add_parser("select_high_ratings", help="Seleciona linhas com 'rating' >= 90")
    subparsers.add_parser("drop_and_one_hot_encode_red_wine", help="Codifica 'Red Wine' e remove 'variety'")
    subparsers.add_parser("remove_newlines_carriage_returns", help="Remove quebras de linha das colunas de texto")
    subparsers.add_parser("convert_ratings_to_int", help="Converte a coluna 'rating' para inteiro")

    args = parser.parse_args()

    df = pd.read_csv('workshop/train.csv')

    if args.command == "drop_notes":
        df = drop_notes(df)
    elif args.command == "select_high_ratings":
        df = select_high_ratings(df)
    elif args.command == "drop_and_one_hot_encode_red_wine":
        df = drop_and_one_hot_encode_red_wine(df)
    elif args.command == "remove_newlines_carriage_returns":
        df = remove_newlines_carriage_returns(df)
    elif args.command == "convert_ratings_to_int":
        df = convert_ratings_to_int(df)
    else:
        parser.print_help()
        return

    df.to_csv('workshop/transformed_train.csv', index=False)
    print("Transformação aplicada com sucesso. Arquivo salvo em 'workshop/transformed_train.csv'.")

if __name__ == "__main__":
    main()