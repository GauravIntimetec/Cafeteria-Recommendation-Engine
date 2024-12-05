import duckdb

a = duckdb.read_csv("C:\L n C\Cafeteria-Recommendation-Engine\Sample.csv")
print(a)

# print(a.columns("Start Date"))

# top_three = duckdb.sql("SELECT Variables, sum(Spend) as Spend FROM 'C:\L n C\Cafeteria-Recommendation-Engine\Sample.csv' group by Variables order by Spend limit 3")
# print(top_three)
star = duckdb.sql("SELECT Variables,Market, sum(Spend) as Spend FROM 'C:\L n C\Cafeteria-Recommendation-Engine\Sample.csv' where variables in (SELECT Variables as Spend FROM 'C:\L n C\Cafeteria-Recommendation-Engine\Sample.csv' group by Variables order by Spend limit 3) group by Variables, Market  order by Spend limit 6")

# star = duckdb.sql("SELECT market, Variables FROM 'C:\L n C\Cafeteria-Recommendation-Engine\Sample.csv' group by market, Variables")
print(star)


top_three = duckdb.sql("SELECT Variables, sum(Spend) as Spend FROM 'C:\L n C\Cafeteria-Recommendation-Engine\Sample.csv' group by Variables order by Spend limit 3")
print(top_three)
           

