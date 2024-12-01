from pprint import pprint, pformat
from datetime import datetime

from elasticsearch import Elasticsearch, helpers

from sqlalchemy import Column, Integer, String, Text, Date, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Define the Elasticsearch connection
es = Elasticsearch(
    "https://localhost:9200",  # Elasticsearch URL
    ca_certs="/tmp/ca.crt",    # Path to the certificate
    basic_auth=("elastic", "changeme"),  # Username and password
)

Base = declarative_base()

class Knowinfo(Base):
    __tablename__ = 'knowinfo'  # Replace with your table name

    knowinfo_id = Column(Integer, primary_key=True)
    kor_name = Column(String(100))
    eng_name = Column(String(100))
    expln = Column(Text)
    smummary = Column(String(1000))
    resource_code = Column(String(100))
    download_count = Column(Integer)
    department_id = Column(Integer)
    lcategory_name = Column(String(100))
    mcategory_name = Column(String(100))
    scategory_name = Column(String(100))
    del_yn = Column(String(1))
    create_dt = Column(Date)
    modified_dt = Column(Date)

class KnowinfoContent(Base):
    __tablename__ = 'knowinfo_content'  # Replace with your table name

    knowinfo_id = Column(Integer, primary_key=True)
    page_content = Column(Text)
    page_num = Column(Integer, primary_key=True)
    create_dt = Column(Date)
    modified_dt = Column(Date)


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

def gen_index_child_data(rows):
    """
    Indexes child documents into Elasticsearch.
    """
    for row in rows:
        # Generate child_id by combining page_cnt and knowinfo_id
        child_id = f"{row.page_num}-{row.knowinfo_id}"

        # Ensure modified_dt is set
        modified_dt = row.modified_dt or row.create_dt

        # Document to index
        yield {
            "page_num": row.page_num,
            "page_content": row.page_content,
            "knowinfo_id": row.knowinfo_id,
            "create_dt": row.create_dt,
            "modified_dt": modified_dt,
            "join_field": {
                "name": "child",
                "parent": row.knowinfo_id,
            },
        }


def gen_index_parent_data(rows):
    """
    Indexes parent documents into Elasticsearch.
    """
    for row in rows:
        # Ensure modified_dt is set
        modified_dt = row.modified_dt or row.create_dt

        # Document to index
        yield {
            "knowinfo_id": row.knowinfo_id,
            "kor_name": row.kor_name,
            "eng_name": row.eng_name,
            "expln": row.expln,
            "smummary": row.smummary,
            "resource_code": row.resource_code,
            "download_count": row.download_count,
            "department_id": row.department_id,
            "lcategory_name": row.lcategory_name,
            "mcategory_name": row.mcategory_name,
            "scategory_name": row.scategory_name,
            "del_yn": row.del_yn,
            "create_dt": row.create_dt,
            "modified_dt": modified_dt,
            "join_field": "parent",
        }

def gen_parent_bulk_action(index_name, docs):
    for doc in docs:
        yield {
            '_index': index_name,
            '_id': str(doc['knowinfo_id']),
            '_source': doc
        }

def gen_child_bulk_action(index_name, docs):
    for doc in docs:
        yield {
            '_index': index_name,
            '_id': f"{doc['page_num']}-{doc['knowinfo_id']}",
            '_source': doc
        }

def parent_db_to_index():
    engine = get_engine()
    Session = sessionmaker(bind=engine)
    with Session() as session:
        results = session.query(Knowinfo).all()
        _parent_docs = gen_parent_bulk_action('knowinfo', gen_index_parent_data(results))
        response = helpers.bulk(es, _parent_docs)
        pprint(response)

def child_db_to_index():
    engine = get_engine()
    Session = sessionmaker(bind=engine)
    with Session() as session:
        results = session.query(KnowinfoContent).all()
        _child_docs = gen_child_bulk_action('knowinfo', gen_index_child_data(results))
        response = helpers.bulk(es, _child_docs)
        pprint(response)

def child_db_to_index_naive():
    """
    Indexes child documents into Elasticsearch.
    """
    engine = get_engine()
    Session = sessionmaker(bind=engine)
    with Session() as session:
        rows = session.query(KnowinfoContent).all()
        for row in rows:
            # Generate child_id by combining page_cnt and knowinfo_id
            child_id = f"{row.page_num}-{row.knowinfo_id}"
            # Ensure modified_dt is set
            modified_dt = row.modified_dt or row.create_dt

            # Document to index
            doc = {
                "page_num": str(row.page_num),
                "page_content": row.page_content,
                "knowinfo_id": row.knowinfo_id,
                "create_dt": row.create_dt,
                "modified_dt": modified_dt,
                "join_field": {
                    "name": "child",
                    "parent": str(row.knowinfo_id),
                },
            }

            # Index the document
            es.index(
                index="knowinfo",
                id=child_id,
                routing=row.knowinfo_id,
                document=doc,
            )
            print(f"Indexed child document: {child_id}")

def parent_db_to_index_naive():
    engine = get_engine()
    Session = sessionmaker(bind=engine)
    with Session() as session:
        rows = session.query(Knowinfo).all()
        for row in rows:
            # Generate child_id by combining page_cnt and knowinfo_id
            modified_dt = row.modified_dt or row.create_dt

            # Document to index
            doc = {
                "knowinfo_id": row.knowinfo_id,
                "kor_name": row.kor_name,
                "eng_name": row.eng_name,
                "expln": row.expln,
                "smummary": row.smummary,
                "resource_code": row.resource_code,
                "download_count": row.download_count,
                "department_id": row.department_id,
                "lcategory_name": row.lcategory_name,
                "mcategory_name": row.mcategory_name,
                "scategory_name": row.scategory_name,
                "del_yn": row.del_yn,
                "create_dt": row.create_dt,
                "modified_dt": modified_dt,
                "join_field": "parent",
            }

            # Index the document
            es.index(
                index="knowinfo",
                id=row.knowinfo_id,
                routing=row.knowinfo_id,
                document=doc,
            )
            print(f"Indexed parent document: {row.knowinfo_id}")
            break

if __name__ == '__main__':
    parent_db_to_index_naive()
    # child_db_to_index()
    # child_db_to_index_naive()
