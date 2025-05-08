'''
=================================================
Milestone 3

Nama  : Dionisius Ray Susantio
Batch : FTDS-025-HCK

Program ini dibuat untuk melakukan automatisasi load data dari PostgreSQL, transform data, dan lalu diupload ke ElasticSearch. 
Adapun dataset yang dipakai adalah dataset mengenai penjualan produk Adidas.
=================================================
'''

import pandas as pd
from datetime import datetime
from sqlalchemy import create_engine
from airflow import DAG
from airflow.decorators import task
from airflow.operators.empty import EmptyOperator
from airflow.models import Variable
from elasticsearch import Elasticsearch, helpers

default_args= {
    'owner': 'Dion',
    'start_date': datetime(2024, 11, 1)
}

with DAG(
    'Saturday_Morning_Analytics',
    description = 'DAG ini bertanggung jawab untuk mengeksekusi tugas-tugas pemrosesan data mingguan pada jam 9 pagi setiap hari Sabtu.',
    schedule_interval = '10,20,30 9 * * 6',
    default_args = default_args,
    catchup=False
)as dag:
    
    start = EmptyOperator(task_id='start')
    end = EmptyOperator(task_id='end')
    
    @task
    def extract_from_postgresql():
        '''Function ini berfungsi untuk mengambil data dari postgresql'''
        database = "airflow"
        username = "airflow"
        password = "airflow"
        host = "postgres"
        
        url = f'postgresql+psycopg2://{username}:{password}@{host}/{database}'
        
        engine = create_engine(url)
        conn = engine.connect()
        
        df = pd.read_sql_query("SELECT * FROM table_m3", conn)
        df.to_csv('/opt/airflow/data/data_raw.csv', sep=',', index=False)
        
    @task
    def data_cleaning():
        '''Function ini berfungsi untuk membersihkan data dari file csv yang sudah diambil dari postgresql'''
        df = pd.read_csv('/opt/airflow/data/data_raw.csv')
        
        # Menghapus baris duplikasi
        df = df.drop_duplicates()
        
        # Menghapus baris yang memiliki nilai null
        df = df.dropna()
        
        # Memperbaiki penamaan kolom agar berhuruf kecil semua tanpa spasi
        df.columns = df.columns.str.lower().str.replace(' ', '_')
        
        # Membersihkan kolom numerik agar hanya berisi angka
        columns_to_clean = ['price_per_unit', 'units_sold', 'total_sales', 'operating_profit']
        for col in columns_to_clean:
            if col in df.columns:
                df[col] = df[col].astype(str).str.replace('[^0-9.-]', '', regex=True)
                df[col] = pd.to_numeric(df[col], errors='coerce')
        
        # Memnbuat kolom unique_id transaksi menggunakan kolom yang ada
        df["unique_transaction_key"] = (
            df["retailer_id"].astype(str) + "_" +
            df["invoice_date"].astype(str) + "_" +
            df["product"].astype(str) + "_" +
            df["sales_method"].astype(str) + "_" +
            df["city"].astype(str) + "_" +
            df["units_sold"].astype(str) + "_" +
            df["price_per_unit"].astype(str)
        )
        
        # Simpan hasil pembersihan ke file csv baru
        df.to_csv('/opt/airflow/data/data_clean.csv', sep=',', index=False)
    
    @task
    def post_to_elasticsearch():
        '''Function ini berfungsi untuk mengupload data ke elasticsearch'''
        
        es = Elasticsearch("http://elasticsearch:9200")
        
        df = pd.read_csv('/opt/airflow/data/data_clean.csv')
        
        # Convert DataFrame to a list of dictionaries
        records = df.to_dict(orient='records')
        
        # Menambahkan index
        actions = [
        {
            "_index": "adidas_dionisius_ray",
            "_source": record
        }
        for record in records
    ]
        
        # Bulk upload data to Elasticsearch
        helpers.bulk(es, actions)
    
    start >> extract_from_postgresql() >> data_cleaning() >> post_to_elasticsearch() >> end
