lis = [1,2,3,4,5,6]
lis1 = []
def reverse_list(lis):
    
    lis1.append(lis.pop())
    while lis:
        reverse_list(lis)
    return ("list1",lis1)

print(reverse_list(lis))

sampleDf = spark.read.format("csv").options("header", True).options("inferschema", True).load("Filestore/tables/sample.csv")
from pyspark.sql.functions import StructField, StructType, IntegerType, FLoatType
schema = StructType(
    [StructField("id", IntegerType, "True")]
)