"""Tathagata Mitra
2:17 PM
Write a SQL query to find all numbers that appear at least three times consecutively.

ID  |   Num
1   |   1
2   |   1
3   |   1
4   |   2
5   |   1
6   |   2
7   |   2

For example, given the above Logs table, 1 is the only number that appears consecutively for at least three times.

Result
1
# """
# select num from 
# (select count(num), 
# row_num() over(oartition by num ) as count_of_num ) x
# where count(num) > 3

# select num from(
#     select num,count(num) over (partition by num ) as count_of from log
# )
# as counted_nums 
# where count(num) > 3 
# group by num,count_of


# ID  |   Num
# 1   |   1
# 2   |   1
# 3   |   1
# 4   |   2
# 5   |   1
# 6   |   2
# 7   |   2

# num | count(num)
# 1       4


select num from(
    select num, 
    lead(num,1) over (order by id )as next_num_1,
    lead(num,2) over (order by id )as next_num_2
    from logs
) as consecutive_log
where num = next_num_1 and num = next_num_2