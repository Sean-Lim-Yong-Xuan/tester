import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
from pymongo import MongoClient

# MongoDB Connection
MONGO_URI = "mongodb+srv://Sean:12345@magicdahtebahse.lfcpi.mongodb.net/"
client = MongoClient(MONGO_URI)

# Select Database and Collection
db = client["mtgdb"]
collection = db["cards"]

# Streamlit App
st.title("📚 Genshin Weapon Stats")

# Fetch Data
cards = list(collection.find({}, {"_id": 0}))  # Exclude ObjectId
