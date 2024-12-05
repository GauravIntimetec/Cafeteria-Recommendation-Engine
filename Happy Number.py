# def str_devide_square(num):
#             str_digit = str(num)
#             sum_of_sqr = 0
#             for item in str_digit:
#                 sum_of_sqr += int(item)**2
#             return sum_of_sqr

# print(str_devide_square(19))

# def have_zero_one(num):
#     return '0' in str(num) and '1' in str(num)


# print(have_zero_one(19))
# print(have_zero_one(300))
# print(have_zero_one(100))

class Solution:
    def isHappy(self, n: int) -> bool:

        def str_devide_square(num):
            str_digit = str(num)
            sum_of_sqr = 0
            for item in str_digit:
                sum_of_sqr += int(item)**2
            return sum_of_sqr

        def have_zero_one(num):
            return '0' in str(num) and '1' in str(num)
            
        visits = set()
        if n > 0:
            result = str_devide_square(n)
            while result not in visits:
                visits.add(result)
                result = str_devide_square(result)
                if result == 1:
                    return True
            return False
        else:
            return False
        
sol = Solution()
print(sol.isHappy(2))   