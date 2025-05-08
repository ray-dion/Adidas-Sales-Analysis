# Judul Project

## Repository Outline
1. README.md - Penjelasan gambaran umum project
2. P2M3_Dionisius_Ray_conceptual.txt - Text file yang menjawab Conceptual Problem
3. P2M3_Dionisius_Ray_DAG_graph.jpg - File gambar yang memberikan gambaran alur pemrosesan data.
4. P2M3_Dionisius_Ray_ddl.txt - File text yang berisi command Query yang digunakan pada saat memasukan data kedalam PostgreSQL
5. P2M3_Dionisius_Ray_GX.ipynb - Notebook yang melakukan validasi atas data yang akan digunakan menggunakan Great Expectations
6. .env - File yang mengatur setting airflow
7. airflow_ES.yaml - File yang digunakan untuk compose docker container.
8. images - Folder yang berisi 6 gambar visualisasi dan insightnya berserta gambar perkenalan dan kesimpulan
9. dags
    1. P2M3_Dionisius_Ray_DAG.py - Script python yang digunakan airflow dalam pemrosesan data

## Problem Background
Sebagai salah satu pegawai data analytics pada Adidas, saya diminta untuk membuatkan sebuah strategi yang dapat diterapkan untuk meningkatkan performa toko yang kesulitan pada region Midwest. Dari hasil data analisis yang dilakukan, company berharap saya sebagai data analyst dapat membantu tim sales untuk meningkatkan keuntungan yang mereka dapatkan sebesar 10% dalam jangka waktu 6 bulan kedepan.

## Project Output
Projek ini akan menghasilkan 6 gambar visualisasi yang berserta insight untuk digunakan dalam membuat keputusan bisnis yang dapat membantu company berkembang.

## Data
Sumber Data: https://www.kaggle.com/datasets/ahmedabbas757/dataset<br><br>
Jumlah Kolom: 12 <br>
Jumlah Baris: 9639 <br>
Missing Value: 2 pada kolom Price per Unit <br>
Kategorikal Kolom: 8 <br>
Numerikal Kolom: 4<br><br>
**Deskripsi Kolom**
|Kolom|Deskripsi| 
|-----|---------|
|`Retailer`|Represents the business or individual that sells Adidas products directly to consumers..|
|`Retailer ID`|A unique identifier assigned to each retailer in the dataset.|
|`Invoice Date`|The date when a particular invoice or sales transaction took place.|
|`Region`|Refers to a specific geographical area or district where the sales activity or retail operations occur.|
|`State`|Represents a specific administrative division or territory within a country.|
|`City`|Refers to an urban area or municipality where the sales activity or retail operations are conducted.|
|`Product`|Represents the classification or grouping of Adidas products.|
|`Price per Unit`|The cost or price associated with a single unit of a product.|
|`Units Sold`|The quantity or number of units of a particular product sold during a specific sales transaction.|
|`Total Sales`|The overall revenue generated from the sales transactions.|
|`Operating Profit`|The profit earned by the retailer from its normal business operations.|
|`Sales Method`|The approach or channel used by the retailer to sell its products or services.|

## Method
Projek ini diselesaikan menggunakan Docker untuk menjalankan Elasticsearch, Kibana, airflow, dan postgreSQL.

## Stacks
Bahasa Pemrograman: Python\

Library:
1. pandas
2. great_expectations

\
Tools/Source Lain:
1. Docker

## Reference
[Adidas Sales Dataset](https://www.kaggle.com/datasets/ahmedabbas757/dataset)

---

**Referensi tambahan:**
- [Basic Writing and Syntax on Markdown](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
- [Contoh readme](https://github.com/fahmimnalfrzki/Swift-XRT-Automation)
- [Another example](https://github.com/sanggusti/final_bangkit) (**Must read**)
- [Additional reference](https://www.freecodecamp.org/news/how-to-write-a-good-readme-file/)