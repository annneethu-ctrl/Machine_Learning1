import pandas as pd
def add_features(df):

    # Price per sqft
    df['Price_per_Sqft'] = (df['Ticket_Price_Cr'] * 10000000) / df['Unit_Size_Sqft']

    # Date features
    df['Purchase_Quarter'] = pd.to_datetime(df['Purchase_Quarter'], errors='coerce')
    df['Quarter_Number'] = df['Purchase_Quarter'].dt.quarter
    df['Year'] = df['Purchase_Quarter'].dt.year

    # Booking flag
    df['Booking_Flag'] = df['Transaction_Type'].apply(
        lambda x: 1 if x == "primary" else 0
    )
    #Outlier Detection
    Q1 = df['Ticket_Price_Cr'].quantile(0.25)
    Q3 = df['Ticket_Price_Cr'].quantile(0.75)

    IQR = Q3 - Q1

    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR

    outliers = df[(df['Ticket_Price_Cr'] < lower) | (df['Ticket_Price_Cr'] > upper)]
    print(outliers)

    return df