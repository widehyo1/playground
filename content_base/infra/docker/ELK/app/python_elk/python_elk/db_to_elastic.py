from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

def get_engine():
    # Database connection parameters
    connection_info = {
        'username': 'test',
        'password': 'test',
        'host': 'localhost',
        'port': '5433',
        'database': 'test_db',
        'schema': 'playground',
    }

    sqlalchemy_url = "postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}?options=-csearch_path%3D{schema}".format(**connection_info)

    print(sqlalchemy_url)

    # Create the SQLAlchemy engine
    engine = create_engine(sqlalchemy_url, echo=True)
    return engine

def test_connection():
    engine = get_engine()
    Session = sessionmaker(bind=engine)
    with Session() as session:
        # Execute the query in ORM
        # session.execute(text(f"SET search_path TO {schema}"))  # Set schema
        count = session.execute(text("SELECT count(1) FROM knowinfo;")).scalar()
        print(f"Row count in knowinfo: {count}")
    # Test the connection
    # try:
    #     with engine.connect() as connection:
    #         print("Connection to PostgreSQL successful!")
    #         # Execute a simple query
    #         result = connection.execute("SELECT count(1) from knowinfo;")
    #         for row in result:
    #             print(f"Database version: {row[0]}")
    # except Exception as e:
    #     print(f"Error connecting to the database: {e}")

if __name__ == '__main__':
    test_connection()
