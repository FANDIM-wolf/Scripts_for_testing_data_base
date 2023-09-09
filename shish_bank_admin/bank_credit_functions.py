def annuity_payment_schedule(loan_amount, annual_interest_rate, loan_term_months):
    """
    Calculates the annuity payment schedule for a loan.

    Parameters:
    loan_amount (float): The amount of the loan.
    annual_interest_rate (float): The annual interest rate in percent for the loan.
    loan_term_months (int): The total number of months for the loan term.

    Returns:
    list: A list of tuples containing the payment number, interest payment, principal payment, and remaining balance for each month.
    """

    monthly_interest_rate = annual_interest_rate / 12 / 100  # Calculate the monthly interest rate.

    # Calculate the annuity coefficient
    annuity_coefficient = (monthly_interest_rate * (1 + monthly_interest_rate) ** loan_term_months) / \
                          ((1 + monthly_interest_rate) ** loan_term_months - 1)

    # Calculate the monthly annuity payment
    monthly_payment = loan_amount * annuity_coefficient

    payment_schedule = []

    for month in range(1, loan_term_months + 1):
        interest_payment = loan_amount * monthly_interest_rate
        principal_payment = monthly_payment - interest_payment
        loan_amount -= principal_payment
        payment_schedule.append((month, interest_payment, principal_payment, loan_amount))

    return payment_schedule


def differential_payment_algorithm(loan_amount, annual_interest_rate, loan_term_years):
    """Calculate the monthly payments for a loan using the differential payment algorithm.

    Args:
        loan_amount (float): The total amount of the loan.
        annual_interest_rate (float): The annual interest rate as a decimal (e.g. 0.05 for 5%).
        loan_term_years (int): The number of years for the loan.

    Returns:
        list: A list of tuples containing the payment number, interest payment, principal payment, and remaining balance for each month.
    """
    # Calculate the monthly interest rate
    monthly_interest_rate = annual_interest_rate / 12

    # Calculate the total number of payments
    total_payments = loan_term_years * 12

    # Calculate the principal payment per month
    principal_payment = loan_amount / total_payments

    payments = []

    # Loop over all the months in the loan term
    for month in range(1, total_payments + 1):
        # Calculate the interest payment for the month
        interest_payment = loan_amount * monthly_interest_rate

        # Calculate the principal payment for the month
        principal_payment = loan_amount / total_payments

        # Update the remaining balance for the loan
        loan_amount -= principal_payment

        # Append the payment information for the month
        payments.append((month, interest_payment, principal_payment, loan_amount))

    return payments

def calculate_loan_repayment(loan_amount, annual_interest_rate, loan_term, amount_paid):
    """
    Calculates the early repayment for an annuity loan.

    Args:
        loan_amount (float): The loan amount.
        annual_interest_rate (float): The annual interest rate.
        loan_term (int): The loan term in months.
        amount_paid (float): The amount the customer pays in advance.

    Returns:
        dict: A dictionary with information about each month's payments and remaining balance details.
    """

    # Calculate the monthly interest rate
    monthly_interest_rate = annual_interest_rate / 12 / 100
    
    # Determine the monthly annuity coefficient
    annuity_coefficient = (monthly_interest_rate * (1 + monthly_interest_rate) ** loan_term) / \
                          ((1 + monthly_interest_rate) ** loan_term - 1)
    
    # Determine the remaining balance at the end of the period
    balance_previous = loan_amount
    
    # Create a list to store payment information
    payment_schedule = []
    
    # Calculate payments for each month
    for month in range(1, loan_term + 1):
        # Calculate the interest payment for the month
        accrued_interest = balance_previous * monthly_interest_rate
        
        # Calculate the principal payment for the month
        principal_payment = min(amount_paid - accrued_interest, balance_previous)
        
        # Calculate the total payment for the month
        monthly_payment = principal_payment + accrued_interest
        
        # Calculate the remaining balance at the end of the period
        balance = balance_previous - principal_payment
        
        # Add the payment information to the payment list
        payment_schedule.append({
            'Month': month,
            'Interest Payment': accrued_interest,
            'Principal Payment': principal_payment,
            'Total Payment': monthly_payment,
            'Remaining Balance': balance
        })
        
        # Update the remaining balance
        balance_previous = balance
    
    return payment_schedule


def calculate_differential_loan_repayment(loan_amount, annual_interest_rate, loan_term):
    """
    Calculates the early repayment for a differential loan.

    Args:
        loan_amount (float): The loan amount.
        annual_interest_rate (float): The annual interest rate.
        loan_term (int): The loan term in months.

    Returns:
        dict: A dictionary with information about each month's payments and remaining balance details.
    """

    # Calculate the monthly interest rate
    monthly_interest_rate = annual_interest_rate / 12 / 100

    # Calculate the fixed principal payment for each month
    fixed_principal_payment = loan_amount / loan_term

    # Initialize the remaining balance at the beginning of the loan term
    balance_previous = loan_amount

    # Create a list to store payment information
    payment_schedule = []

    # Calculate payments for each month
    for month in range(1, loan_term + 1):
        # Calculate the interest payment for the month
        interest_payment = balance_previous * monthly_interest_rate

        # Calculate the total payment for the month
        monthly_payment = fixed_principal_payment + interest_payment

        # Calculate the remaining balance at the end of the period
        balance = balance_previous - fixed_principal_payment

        # Add the payment information to the payment list
        payment_schedule.append({
            'Month': month,
            'Interest Payment': interest_payment,
            'Principal Payment': fixed_principal_payment,
            'Total Payment': monthly_payment,
            'Remaining Balance': balance
        })

        # Update the remaining balance
        balance_previous = balance

    return payment_schedule