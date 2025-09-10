## ETL Project: parsing Wikipedia articles

## This project implements an ETL process for processing data on Wikipedia articles
 - Parsing HTML page data
 - Extracting raw data to a Json file
 - Transformation (cleaning, normalization, aggregation) and uploading data to CSV
 - Uploading ready-made data from CSV to MS SQL Server database

---

## Task execution sequence
- scraper_task >> transform_task >> load_task
- **scraper_task** — parsing HTML Wikipedia pages, saving "raw" data in JSON.  
- **transform_task** — cleaning, normalization and aggregation of data in Pandas, saving in CSV.  
- **load_task** — loading processed data from CSV to MS SQL Server via SQLAlchemy.

---

## Technologies used
- Python 3.12.2
- Airflow
- MS SQL Server (ODBC Driver 18)
- Pandas, SQLAlchemy, BeautifulSoup
- Docker / Docker Compose 

----

## Architecture
 **Airflow** task Orchestrator (DAG)
 **Docker Compose** elevates the Airflow environment
 **Pandas** performs transformations
 **SQLAlchemy** It is used for connecting and writing data to a database.
 **BeautifulSoup** HTML page parsing

---

## Structure

``` LG/ ├── dags/ │ └── etl_pipeline.py # основной DAG ├── etl/ │ ├── load.py # загрузка в MS SQL Server │ ├── scraper.py # парсинг и сохранение JSON │ └── transform.py # обработка и трансформация ├── docker-compose.yml # окружение Docker ├── requirements.txt # зависимости Python └── logs/ # логи задач ```


