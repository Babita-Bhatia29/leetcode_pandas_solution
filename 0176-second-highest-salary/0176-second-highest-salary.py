import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    unique_salary = employee["salary"].drop_duplicates().sort_values(ascending=False)

    
    if len(unique_salary)>=2:
        second_heighest_salary = unique_salary.iloc[1]
    else:
        second_heighest_salary = None

    
    return pd.DataFrame({"SecondHighestSalary":[second_heighest_salary]})
    