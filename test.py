import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
from pymongo import MongoClient

# MongoDB Connection
MONGO_URI = "mongodb+srv://admin:admin@cluster0.qa6yj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(MONGO_URI)

# Select Database and Collection
db = client["Test1234"]
collection = db["sample"]

# Streamlit App
st.title("📚 Genshin Weapon Stats")

# Fetch Data
cards = list(collection.find({}, {"_id": 0}))  # Exclude ObjectId
