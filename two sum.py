nums1 = [1, 3, 5]
nums2 = [2, 4, 6]

def merge_arrays(nums1, nums2):
    i,j = 0,0
    m,n = len(nums1), len(nums2)
    
    nums1.extend([0]*n)

    while i < m+n and j<n:
        if nums1[i] <=nums2[j]:
            i+=1
        else: 
            nums1.insert(i, nums2[j])
            nums1.pop()
            j+=1
    print(nums1, m, n)
    while j<m:
        nums1[m+j] = nums2[j]
        j+=1
    



merge_arrays(nums1, nums2)
print(nums1)



zeta : Table Name : customer_orders

Column Name	Type
order_id	integer
customer_id	integer
order_date	date
order_amount	integer

Write a SQL query to find the new and repeated customer for each order_date.
Return the result table in the increasing order of order_date.



  order_id	customer_id	order_date	order_amount
1	100	2022-01-01	2000
2	200	2022-01-01	2500
3	300	2022-01-01	2100
4	100	2022-01-02	2000
5	400	2022-01-02	2200
6	500	2022-01-02	2700
7	100	2022-01-03	3000
8	400	2022-01-03	1000
9	600	2022-01-03	3000

order_date new_cus rep_cus

with cte as(
  select customer_id,
  min(order_date) as first_order
  from customer_orders
group by customer_id
),

customer_type(
  select 
  order_date,
  customer_id,
  case 
    when c.first_order = o.order_date then 'new'
    else 'repeated'
  end as customer_type

from orders.o
join cte c
on o.customer_id = c.customer_id 
)

select 
order_date,
  sum(case when customer_type = 'new' then 1 else 0) as new_customer,
 sum(case when customer_type = 'repeated' then 1 else 0) as repeated_customer
  from customer_type
group by order_date
order by order_date
  
# try withb Binary 
  Given a 0-indexed integer array nums of length n and an integer target, 
  return the number of pairs (i, j) where 0 <= i < j < n and nums[i] + nums[j] < target.

  [-1,1,2,3,1] 2

def sum_less_then_2(list1, target):  [1, 2,3,4,5]  target = 7  
  num.sort()
  count = 0
  left = 0
  right = len(list1)- 1
  while left < right: 
    if nums1[left] + nums1[right] < target:
      count+= right - left
      left+=1
    else :
       right -= 1
return count
  




