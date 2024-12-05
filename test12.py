# json = {"item_id" : 1, "clicks" : 92, "impressions" : 991}

# file = "text1.csv"
# path2 = "dbo.table1"



# df1 = spark.read.format("csv").options(path, "text1.csv").header=True   
# #id, first_name, salary  
# # 1,gaurav, 200  
# # 2,singh, 100  
# # 1,gaurav, 500 


# df2 = spark.read.jdbc(url = "", table= "")                              
# #last_name, month, location, dept 
# #gaurav, 1, "jaipur India", cse
# #mohit, 2, "kota Rajasthan India", me
# #gaurav, 2, "jaipur", cse


"""
select id, name 
    from df1 join df2 
    on df1.first_name = {df2}.last_name
    group by df1.first_name, month
    having sum(df2.salary) > 10000"""

"""select 
location, length(split(location, " "))
from df2 """


# l1 = [1,2,3,4,1,2,3,4, 4]
# dic = {}
# for i in l1:
#     dic[i] = dic.get(i, 0) + 1

# print(dic)

def fib(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a,b = b,b+a     

fib = fib(6)
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))

spark.broadcast("table1")


