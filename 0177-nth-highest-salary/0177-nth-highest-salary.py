import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    unique_salary=employee["salary"].drop_duplicates()
    sorted_salary=unique_salary.sort_values(ascending=False)
     
    if  N <= 0 or N>len(sorted_salary):
        return pd.DataFrame({f"getNthHighestSalary({N})":[None]})
    else:
        nth_highest = sorted_salary.iloc[N-1]

    return pd.DataFrame({f"getNthHighestSalary({N})":[nth_highest]})