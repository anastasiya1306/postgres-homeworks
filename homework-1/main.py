"""Скрипт для заполнения данными таблиц в БД Postgres."""
import csv
import psycopg2

with psycopg2.connect(
    host="localhost",
    database="north",
    user="postgres",
    password="simba2106"
) as conn:
    with conn.cursor() as cur:
        with open('../homework-1/north_data/employees_data.csv', 'r', encoding='utf-8') as file:
            reader_file = csv.DictReader(file)
            i = 1
            for row in reader_file:
                cur.execute("INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)", (i, row['first_name'], row['last_name'],
                                                                                      row['title'], row['birth_date'], row['notes']))
                i += 1
        with open('../homework-1/north_data/customers_data.csv', 'r', encoding='utf-8') as file:
            reader_file = csv.DictReader(file)
            for row in reader_file:
                cur.execute("INSERT INTO customers VALUES (%s, %s, %s)", (row['customer_id'], row['company_name'], row['contact_name']))

        with open('../homework-1/north_data/orders_data.csv', 'r', encoding='utf-8') as file:
            reader_file = csv.DictReader(file)
            for row in reader_file:
                cur.execute("INSERT INTO orders VALUES (%s, %s, %s, %s, %s)", (row['order_id'], row['customer_id'],
                                                                                  row['employee_id'], row['order_date'], row['ship_city']))

conn.close()