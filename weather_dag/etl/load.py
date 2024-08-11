def load_city():
    import os
    import pandas as pd
    from sqlalchemy import create_engine

    conn = create_engine(os.getenv("DB_URL"))
    
    cities_df = pd.read_json(f'{os.getenv("OUTPUT_FILES_PATH")}/city_data.json')
    
    cities_df.set_index('id_city', inplace=True)
    cities_df.to_sql('city', conn, if_exists='replace')
    
    
def load_weather_conditions():
    import os
    import pandas as pd
    from sqlalchemy import create_engine, types
    
    conn = create_engine(os.getenv("DB_URL"))
    conditions_df = pd.read_json(f'{os.getenv("OUTPUT_FILES_PATH")}/weather/conditions.json')
    
    conditions_df.set_index('weather_code', inplace=True)
    conditions_df.to_sql('weather_conditions', conn, if_exists='replace')


def load_air_pollution_data():
    import os
    import pandas as pd
    from sqlalchemy import create_engine
    
    conn = create_engine(os.getenv("DB_URL"))
    air_pollution_df = pd.read_json(f'{os.getenv("OUTPUT_FILES_PATH")}/transform.json')
    
    air_pollution_df.to_sql('air_data', conn, index=False, if_exists='append')