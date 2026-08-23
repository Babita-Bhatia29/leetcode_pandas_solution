import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:

    sorted_data=employee["salary"].sort_values(ascending=True)
    data=employee.groupby("departmentId")["salary"].transform("max")
    result=employee[employee["salary"]==data]
    
    result=result.merge(
        department,
        left_on="departmentId" ,
        right_on="id"
    )
    result=result[["name_x","name_y","salary"]]
    result.columns=["Department","Employee","Salary"]

    return result
