from flask import Flask, jsonify
import psycopg2, json, os
import pandas as pd

app = Flask(__name__)

conn = psycopg2.connect(host='',dbname = '',user='',password='')

@app.route('/', methods=['GET'])
def get_all():    
    query = """select * from public.burgerstar"""

    df = pd.read_sql(query,conn)
    df = df.to_dict(orient='index')

    return jsonify(df)

@app.route('/date/<string:date>', methods=['GET'])
def get_date(date):
    """you can filter using multiple date with comma (,)
    ex /date/20200101,20200102,20200201"""
    date = date.split(',')
    date = "'" + "','".join(date) + "'"
    query = """select * from public.burgerstar
    where date in ({})""".format(date)

    df = pd.read_sql(query,conn)
    df = df.to_dict(orient='index')

    return jsonify(df)

@app.route('/location/<string:location>', methods=['GET'])
def get_location(location):
    """you can filter using multiple location with comma (,)
    ex /location/location1,location2,location3"""
    location = location.split(',')
    location = "'" + "','".join(location) + "'"

    query = """select * from public.burgerstar
    where location in ({})""".format(location)

    df = pd.read_sql(query,conn)
    df = df.to_dict(orient='index')

    return jsonify(df)

@app.route('/date/<string:date>/location/<string:location>', methods=['GET'])
@app.route('/location/<string:location>/date/<string:date>', methods=['GET'])
def get_date_location(location,date):
    """you can filter using multiple date and location with comma (,)
    ex /date/20200101,20200102,20200201/location/Puma,Sumbagut"""
    date = date.split(',')
    date = "'" + "','".join(date) + "'"
    location = location.split(',')
    location = "'" + "','".join(location) + "'"

    query = """select * from public.burgerstar
    where date in ({}) and location in ({})""".format(date,location)

    df = pd.read_sql(query,conn)
    df = df.to_dict(orient='index')

    return jsonify(df)

if __name__ == '__main__':
    app.run()

