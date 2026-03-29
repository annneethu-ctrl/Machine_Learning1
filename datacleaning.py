def clean_data(df):
    

    # Remove duplicates
    df = df.drop_duplicates()

    # Clean price column
    df['Ticket_Price_Cr'] = df['Ticket_Price_Cr'].replace('[₹,Cr]', '', regex=True).astype(float)

    # Handle missing values
    df['Amenity_Score'] = df['Amenity_Score'].fillna(df['Amenity_Score'].median())
    df['Buyer_Comments'] = df['Buyer_Comments'].fillna("No Comment")

    # Normalize text
    df['Developer_Name'] = df['Developer_Name'].str.strip().str.lower()
    df['Micro_Market'] = df['Micro_Market'].str.strip().str.lower()
    df['Transaction_Type'] = df['Transaction_Type'].str.strip().str.lower()

    return df