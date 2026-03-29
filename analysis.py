import pandas as pd

def run_queries(engine):
    query1="SELECT COUNT(*) FROM housing_data;"
    result = pd.read_sql(query1, engine)
    print(result)

#Booked vs Not Booked
    query2="SELECT Booking_Flag, COUNT(*)  FROM housing_data GROUP BY Booking_Flag;"
    result = pd.read_sql(query2, engine)
    print(result)

#expensive properties
    query3="SELECT Developer_Name, AVG(Ticket_Price_Cr) AS Avg_Price FROM housing_data GROUP BY Developer_Name ORDER BY Avg_Price DESC;"
    result = pd.read_sql(query3, engine)
    print(result)

 #Total Revenue per Developer_Name'
    query4="""SELECT Developer_Name, SUM(Ticket_Price_Cr) AS Total_Revenue FROM housing_data
    GROUP BY Developer_Name
    ORDER BY Total_Revenue DESC;
    """
    result = pd.read_sql(query4, engine)
    print(result)

#% of successful bookings
    query5="SELECT  AVG(Booking_Flag) * 100 AS Conversion_Rate FROM housing_data;"
    result = pd.read_sql(query5, engine)
    print(result)

#Quarter-wise Sales

    query6="SELECT Quarter_Number, COUNT(*) AS Total_Sales FROM housing_data GROUP BY Quarter_Number ORDER BY Quarter_Number;"
    result = pd.read_sql(query6, engine)
    print(result)

