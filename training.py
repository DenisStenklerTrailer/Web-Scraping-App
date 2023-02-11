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

if __name__ == "__main__":
    scraped = scrape(URL)
    extracted = extract(scraped)
    print(extracted)
    date_time = store(extracted)
    print(date_time)

    pos_figure = px.line(x=[date[0] for date in date_time], y=[temp[1] for temp in date_time],
                         labels={"x": "Date", "y": "Temperature"})
    st.plotly_chart(pos_figure)




