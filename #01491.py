# You are given an array of unique integers salary where salary[i] is the salary of the ith employee.
# Return the average salary of employees excluding the minimum and maximum salary. Answers within 10-5 of the actual answer will be accepted.
class Solution:
    def average(self, salary: list[int]) -> float:
        salary_max, salary_min = float(0), float('inf')
        total_salary = 0
        for i in salary:
            if i > salary_max:
                salary_max = i
            if i < salary_min:
                salary_min = i
            total_salary += i
        total_salary -= salary_max + salary_min
        return total_salary / int(len(salary) - 2)

        # or

        # salary_max = max(salary)
        # salary_min = min(salary)
        # salary.remove(salary_max)
        # salary.remove(salary_min)
        # if len(salary) > 1:
        #     average = sum(salary)/ len(salary)
        #     output = round(average, 5)
        #     return output
        # else:
        #     output = round(salary[0], 5)
        #     return output
