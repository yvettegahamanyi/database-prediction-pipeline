import csv
import psycopg2

# Connect to your PostgreSQL database
conn = psycopg2.connect(
    dbname="heart_disease_dataset",
    user="heart_disease_dataset_user",
    password="XBOcYl4d0fLr42Kp9i4u1COwK0CDkZBt",
    host="dpg-d41t0qvgi27c739nv670-a.ohio-postgres.render.com",
    port="5432"
)
cur = conn.cursor()

# Open your CSV file
with open('/Users/gahamanyi/Documents/alu/Neural network/formative_1_ml_pipeline/heart_disease_health_indicators_BRFSS2015.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        # Convert all numeric fields properly
        params = (
            float(row['Sex']),
            float(row['Age']),
            float(row['Education']),
            float(row['Income']),
            float(row['BMI']),
            float(row['Smoker']),
            float(row['PhysActivity']),
            float(row['Fruits']),
            float(row['Veggies']),
            float(row['HvyAlcoholConsump']),
            float(row['HeartDiseaseorAttack']),
            float(row['HighBP']),
            float(row['HighChol']),
            float(row['CholCheck']),
            float(row['Stroke']),
            float(row['Diabetes']),
            float(row['AnyHealthcare']),
            float(row['NoDocbcCost']),
            float(row['GenHlth']),
            float(row['MentHlth']),
            float(row['PhysHlth']),
            float(row['DiffWalk'])
        )

        # Call your stored procedure for each record
        cur.execute("""
            CALL add_patient_record(
                %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
                %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s
            )
        """, params)

# Commit all inserts at once
conn.commit()
print("✅ All records inserted successfully using stored procedure.")

cur.close()
conn.close()
