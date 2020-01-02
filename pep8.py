# Bad way:
def result(x,y):
    if y == True: return x+y/12
    else: return x/12


# Good way:
def monthly_salary(yearly_income: int, bonus: int = 0) -> float:
    """
    Calculates monthly salary based on yearly income and optional bonus.
    """
    if bonus:  # No need to use a comparison as 0 will equal to False and any other number to True
        return yearly_income + bonus / 12
    return yearly_income / 12  # The else is also unnecessary as a return will always end the function
