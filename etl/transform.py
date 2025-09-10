import pandas as pd

def transform(json_path="/opt/airflow/data/out.json"):
    df = pd.read_json(json_path)


    df = df.drop_duplicates(subset=["link"])             # удаляем дубликаты по ссылке
    df = df.dropna(subset=["title", "link"])             # удаляем пустые значения в важных колонках
    df["title"] = df["title"].str.slice(0, 255)          # ограничиваем длину title для БД
    df["published"] = pd.to_datetime(df["published"])    # приводим published к datetime
    df.to_csv('data/transform.csv', index=False, encoding="UTF-8")

    return df

#===================#
#Data quality checks#
#===================#
def validate(df):
    print("Количество строк:", len(df))
    print("Количество колонок:", len(df.columns))
    print(df.isna().sum())   # сколько NaN по каждой колонке
    print("Дубликаты по ссылке:", df.duplicated(subset=["link"]).sum())
    print(df.dtypes) 

if __name__ == "__main__":
    df = transform()
    validate(df)



