import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
from pymongo import MongoClient

# MongoDB Connection
MONGO_URI = "mongodb+srv://Cluster0:123@cluster0.wi9dl.mongodb.net/"
client = MongoClient(MONGO_URI)

# Select Database and Collection
db = client["Test1234"]
collection = db["sample"]

# Streamlit App
st.title("📚 Genshin Weapon Stats")

# Fetch Data
sample = list(collection.find({}, {"_id": 0}))  # Exclude ObjectId

def display_data_from_mongodb():
    """Displays data from MongoDB in Streamlit."""
    try:
        collection = db.get_collection("sample")  # Replace with your collection name
        data = list(collection.find())
        if data:
            df = pd.DataFrame(data)
            df = df.drop(columns=['_id'], errors='ignore') #remove mongodb's _id
            st.dataframe(df)
        else:
            st.info("No data found in MongoDB.")
    except Exception as e:
        st.error(f"Error retrieving data from MongoDB: {e}")

    # def main():
    #     st.title("Data from MongoDB")
    #     display_data_from_mongodb()

    # if __name__ == "__main__":
    #     main()

# def main():
#     st.title("📚 Genshin Weapon Stats visual")

#     collection_name = "sample"  # Replace with your collection name
#     df = pd.DataFrame(sample)

#     if df is not None:
#         # Example: Simple line plot (assuming 'x' and 'y' columns exist)
#         if 'x' in df.columns and 'y' in df.columns:
#             st.subheader("Line Plot")
#             fig, ax = plt.subplots()
#             ax.plot(df['x'], df['y'])
#             st.pyplot(fig)

#         # Example: Bar chart (assuming 'category' and 'value' columns exist)
#         if 'category' in df.columns and 'value' in df.columns:
#             st.subheader("Bar Chart")
#             fig, ax = plt.subplots()
#             ax.bar(df['category'], df['value'])
#             plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels
#             st.pyplot(fig)

#         #Add more plot types as needed.
#         #Example using plotly
#         if 'category' in df.columns and 'value' in df.columns:
#             import plotly.express as px
#             st.subheader("Plotly Bar Chart")
#             fig = px.bar(df, x='category', y='value')
#             st.plotly_chart(fig)

#     else:
#         st.info("No data to plot.")

# if __name__ == "__main__":
#     main()

# Fetch Data
sample = list(collection.find({}, {"_id": 0}))  # Exclude ObjectId

if sample:
    df = pd.DataFrame(sample)
    st.dataframe(df)

    # 📊 Bar Chart: Weapons type
    st.subheader("📊 Weapon type")
    fig, ax = plt.subplots()
    df["type"].value_counts().sort_index().plot(kind="bar", ax=ax, color="skyblue")
    ax.set_xlabel("weapon_name")
    ax.set_ylabel("type")
    st.pyplot(fig)

    # # 🏫 Pie Chart: Course Distribution
    # st.subheader("🏫 Course Distribution")
    # fig, ax = plt.subplots()
    # df["course"].value_counts().plot(kind="pie", autopct="%1.1f%%", ax=ax, startangle=90, colors=["lightcoral", "lightblue", "lightgreen"])
    # st.pyplot(fig)

    # st.title("Stacked Bar Chart from MongoDB")

    # if df is None:
    #     st.stop()  # Stop if MongoDB connection failed

    # # --- Data Preparation ---
    # # Assuming your DataFrame has 'category', 'segment1', and 'segment2' columns
    # # if 'category' not in df.columns or 'segment1' not in df.columns or 'segment2' not in df.columns:
    # #     st.error("Missing required columns: 'category', 'segment1', 'segment2'")
    # #     st.stop()

    # # If needed, perform data transformations or grouping here
    # # Example (if your data requires grouping):
    # # grouped_df = df.groupby('category')[['segment1', 'segment2']].sum().reset_index()
    # # Otherwise, use the original DataFrame:
    # # grouped_df = df.copy() # Make a copy to avoid modification warnings.
    # grouped_df = df.groupby('category')[['weapon_name', 'type']].sum().reset_index()

    # # --- Stacked Bar Chart (Matplotlib) ---
    # st.subheader("Stacked Bar Chart (Matplotlib)")
    # try:
    #     fig, ax = plt.subplots()
    #     grouped_df.plot(x='category', kind='bar', stacked=True, ax=ax)
    #     st.pyplot(fig)
    # except Exception as e:
    #     st.error(f"Error creating Matplotlib chart: {e}")

    # # --- Stacked Bar Chart (Seaborn) ---
    # st.subheader("Stacked Bar Chart (Seaborn)")
    # try:
    #     melted_df = grouped_df.melt(id_vars='category', var_name='segment', value_name='value')
    #     fig, ax = plt.subplots()
    #     sns.barplot(x='category', y='value', hue='segment', data=melted_df, ax=ax)
    #     st.pyplot(fig)
    # except Exception as e:
    #     st.error(f"Error creating Seaborn chart: {e}")

    if df is not None:
        # Assuming you have a column for categories and a column for values
        category_column = st.selectbox("Types", df.columns)
        value_column = st.selectbox("Values", df.columns)

        if category_column and value_column:
            try:
                # Group by category and sum the values
                grouped_df = df.groupby(category_column)[value_column].sum().reset_index()

                # Create the pie chart
                fig = px.pie(grouped_df, values=value_column, names=category_column, title=f"Pie Chart of {value_column} by {category_column}")
                st.plotly_chart(fig)

            except KeyError:
                st.error("Selected columns not found in DataFrame.")
            except Exception as e:
                st.error(f"An error occurred: {e}")

    else:
        st.warning("No value was found")
