import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

connection = mysql.connector.connect(
    host = "localhost",
    user="root",
    password="Ch@r1z@rd",
    database = "anime_database"
)
query = """
SELECT
    a.title,
    w.status,
    w.rating
FROM Watchlist w
JOIN Anime a
ON w.anime_id = a.anime_id
"""
df = pd.read_sql(query,connection)

# print(df)
# print("Total Entries:",len(df))
# print("Average Rating:",df["rating"].mean())
# print("Highest rating:",df["rating"].max())
# print("Lowest rating:",df["rating"].min())

# print(df["status"].value_counts())

df.to_csv(
    "watchlist.csv",
    index=False
)
# print("CSV exported")
# print(df.info())
# print(df.describe())

# top rated anime
top_anime = df.sort_values(
    by="rating",
    ascending=False
)

# print(top_anime)
# print("\nTotal Anime:")
# print(len(df))

top_anime = df.sort_values(
    by="rating",
    ascending=False
)

# print(top_anime.to_string())
"""first matplot visualization graph"""
plt.figure(figsize=(7,5))

plt.bar(
    df["title"],
    df["rating"]
)

plt.title("Anime Ratings")

plt.xlabel("Anime")

plt.ylabel("Rating")

plt.show()
# """2nd graph"""
# status_count = df["status"].value_counts()

# plt.figure(figsize=(8,5))

# plt.bar(
#     status_count.index,
#     status_count.values
# )

# plt.title("Watch Status Distribution")

# plt.show()
