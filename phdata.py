from pyspark.sql import SparkSession

# Create a SparkSession
spark = SparkSession.builder.appName("Employee Analysis").getOrCreate()

# Load the data into a DataFrame
df = spark.read.format("csv") \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .load("path/to/your/data.csv")  # Replace with your actual data path

# Calculate the number of years since hire date
from pyspark.sql.functions import datediff, col, lit, when

df = df.withColumn("years_since_hire", datediff(col("current_date"), col("hire_date")) / 365)

# Filter employees with more than 2 years of service
filtered_df = df.filter(col("years_since_hire") > 2)

# Add a column indicating whether the employee is still part of the company
filtered_df = filtered_df.withColumn("is_still_part_of_company", 
                                      when(col("termination_date").isNull(), lit("Yes"))
                                      .otherwise(lit("No")))

# Show the filtered data
filtered_df.show()