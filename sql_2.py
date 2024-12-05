"""
CoinDCX has a VIP Program, based on the past 30 days transaction volume, we want to find out the list of VIP Users:
Assume that the fee for every transaction is 1% of the total amount.
UserTransactions
UserID  |  Amount_INR  |  TransactionDate
—----------------------------------------------------------
1           |   5000     |   05-06-2023
2           |   6000     |   15-06-2023
1           |  1000      |   22-11-2023
2           |   5000     |   24-11-2023
2           |  2500      |   25-11-2023
VIPLevels
startAmount  |  EndAmount    |  Level           |  Discount_Perc
—-------------------------------------------------------------------------------
0                   |       1000          |   Non VIP     |  0
1001             |       5000          |   VIP 1          |  0.25
5001             |      10000         |   VIP 2          |  0.5
10001           |       99999        |   VIP 3          |  0.75
Provide the list of VIP Users along with their Transaction Amount over past 30 days with fees and savings
UserID     | Amount_INR   |  VIP_Level | Fees_perc   | Savings
—-----------------------------------------------------------------------------------
   2           |      7500           | 2                | 0.5               |  375"""


with cte as (select user_id, amount_inr from UserTransactions 
group by user_id 
where TransactionDate between 25-11-2023 and date(25-11-2023, -30) )

select user_id , amount_inr, level, Discount_Perc from cte
join VIPLevels on EndAmount<=amount_inr And startAmount>=amount_inr 

l = [1, 2, 1, 4, 3, 3, 2, 4]
out = [1, 3, 2, 4] 