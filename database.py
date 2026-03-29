from sqlalchemy import create_engine

def save_to_mysql(df):
    engine = create_engine("mysql+pymysql://root:mysql@localhost:3306/housing_db")
    df.to_sql('housing_data', con=engine, if_exists='replace', index=False)
    return engine