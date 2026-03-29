from dataload import load_data
from datacleaning import clean_data
from Feature_engg import add_features
from database import save_to_mysql
from analysis import run_queries

# Step 1: Load
df = load_data("C:\\Users\\hp\\OneDrive\\Desktop\\guvi\\Housing_Project\\Luxury_Housing_Bangalore.csv")
# Step 2: Clean
df = clean_data(df)
# Step 3: Feature Engineering
df = add_features(df)
# Step 4: Save cleaned data
df.to_csv("C:\\Users\\hp\\OneDrive\\Desktop\\guvi\\Housing_Project\\Cleaned_Housing_Bangalore.csv", index=False)
# Step 5: Store in MySQL
engine = save_to_mysql(df)
# Step 6: Run Analysis
run_queries(engine)
