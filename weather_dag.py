from __future__ import annotations
from datetime import datetime
from airflow.decorators import dag, task
from airflow.models.baseoperator import chain
from airflow.operators.python import PythonOperator, PythonVirtualenvOperator
from weather_dag.etl.extract import get_current_data_from_cities, extract_available_conditions
from weather_dag.etl.transform import gen_city_list, transform_data
from weather_dag.etl.load import load_city, load_weather_conditions, load_air_pollution_data

@dag(
    dag_display_name="Weather API dag",
    catchup=True,
    description="A simple dags to load airpollution data from OpenWeather API",
    schedule_interval="@daily",
    start_date=datetime(2024, 7, 26),
) 
def weather_dag():
    extract_cities = PythonOperator(
        python_callable=gen_city_list,
        task_id="gen_city_list"
    )
    
    extract_weather_conditions = PythonOperator(
        python_callable=extract_available_conditions,
        task_id="extract_weather_conditions"
    )
    
    load_cities = PythonVirtualenvOperator(
        task_id="load_cities",
        python_callable= load_city,
        requirements=[
            "sqlalchemy",
            "pandas",
            "psycopg2"
        ]
    )
    
    load_conditions = PythonVirtualenvOperator(
        task_id="load_weather_conditions",
        python_callable= load_weather_conditions,
        requirements=[
            "sqlalchemy",
            "pandas",
            "psycopg2"
        ]
    )
    
    extract = PythonOperator(
        python_callable= get_current_data_from_cities,
        task_id= "extract_weather_data"
    )
    
    transform = PythonOperator(
        python_callable= transform_data,
        task_id= "transform_data_to_model"
    )
    
    load_air_data = PythonVirtualenvOperator(
        task_id="load_air_data",
        python_callable= load_air_pollution_data,
        requirements=[
            "sqlalchemy",
            "pandas",
            "psycopg2"
        ]
    )
    
    cities_elt = [
        extract_cities,
        load_cities,
        load_air_data
    ]
    
    conditions_etl = [
        extract_weather_conditions,
        load_conditions,
        load_air_data
    ]
    
    chain(*cities_elt)
    chain(*conditions_etl)
    
    
    extract >> transform >> load_air_data
    
weather_air_pollution = weather_dag()
