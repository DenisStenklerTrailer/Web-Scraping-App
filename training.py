import requests
import selectorlib
from datetime import datetime
import streamlit as st
import plotly.express as px

URL = "https://programmer100.pythonanywhere.com/"

# datetime object containing current date and time
now = datetime.now()

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
    with open("temperatures.txt", "r") as file:
        data = file.readlines()

    data.append(f"{now.strftime('%d-%m-%Y-%H-%M-%S')},{str(temperature)}\n")

    with open("temperatures.txt", "w") as file:
        file.writelines(data)

    return [date_temp.split(",") for date_temp in data]

if __name__ == "__main__":
    scraped = scrape(URL)
    extracted = extract(scraped)
    date_time = store(extracted)
    
    pos_figure = px.line(x=[date[0] for date in date_time], y=[temp[1] for temp in date_time],
                         labels={"x": "Date", "y": "Temperature"})
    st.plotly_chart(pos_figure)




