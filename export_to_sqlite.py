
import sqlite3
import pandas as pd
from pathlib import Path

OUT_DIR = Path(r"C:\Users\amrel\Desktop\Data Analysis course\projects\fifa\outputs")

conn = sqlite3.connect("fifa.db")

# Load Top 20
top20 = pd.read_csv(OUT_DIR / "top20_players.csv")
top20.to_sql("top20_players", conn, if_exists="replace", index=False)

# Load full cleaned dataset
cleaned = pd.read_csv(OUT_DIR / "cleaned_players.csv")
cleaned.to_sql("cleaned_players", conn, if_exists="replace", index=False)

# Load teams summary
teams = pd.read_csv(OUT_DIR / "teams_summary.csv")
teams.to_sql("teams_summary", conn, if_exists="replace", index=False)

conn.commit()
conn.close()

print("All CSV files loaded into SQLite.")











    



