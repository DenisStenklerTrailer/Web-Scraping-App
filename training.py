import requests
import selectorlib
from datetime import datetime
import streamlit as st
import plotly.express as px
import sqlite3

URL = "https://programmer100.pythonanywhere.com/"

# datetime object containing current date and time
now = datetime.now()

connection = sqlite3.connect("temperatures.db")

st.title("TEMPTERATURE CHART")

def scrape(url):
    response = requests.get(url)
    source = response.text
    return source

def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("training.yaml")
    value = extractor.extract(source)["temperature"]
    return value

def store(temperature=None):
    cursor = connection.cursor()
    data = (now.strftime("%d-%m-%Y-%H-%M-%S"), temperature)
    cursor.execute("INSERT INTO temperatures VALUES(?,?)", data)
    connection.commit()
    return data

def read_date():
    cursor = connection.cursor()
    cursor.execute("SELECT date from temperatures")
    date = cursor.fetchall()
    date = [item[0] for item in date]
    return date

def read_temp():
    cursor = connection.cursor()
    cursor.execute("SELECT temperature from temperatures")
    temp = cursor.fetchall()
    temp = [item[0] for item in temp]
    return temp

if __name__ == "__main__":
    scraped = scrape(URL)
    extracted = extract(scraped)
    print(extracted)
    date_time = store(extracted)

    date = read_date()
    temp = read_temp()
    print(date)
    print(temp)

    pos_figure = px.line(x=date, y=temp, labels={"x": "Date", "y": "Temperature"})

    st.plotly_chart(pos_figure)




