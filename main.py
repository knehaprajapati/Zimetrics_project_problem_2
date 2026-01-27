import pandas as pd

USD_TO_INR = 83

df = pd.read_csv("sales.csv")

df["Product"] = df["Product"].astype(str).str.replace('"', '').str.strip()
df["Price"] = (
    df["Price"]
    .astype(str)
    .str.replace('$', '', regex=False)
    .str.strip()
    .astype(float)
)

df["Price_INR"] = df["Price"] * USD_TO_INR

df = df.drop_duplicates(subset=["Product", "Price_INR"])

final_df = df[["ID", "Product", "Price_INR", "Country"]]
final_df.to_json("clean_sales.json", orient="records", indent=4)

print("Clean sales data saved successfully!")
