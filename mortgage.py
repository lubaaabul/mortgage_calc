def monthly_payment(principal, annual_rate, years):
    """
    Ежемесячный платёж по аннуитетной схеме.
    principal - сумма кредита
    annual_rate - годовая ставка в процентах
    years - срок в годах
    """
    if principal <= 0 or annual_rate <= 0 or years <= 0:
        raise ValueError("Все параметры должны быть положительными")

    monthly_rate = annual_rate / 100 / 12
    n = years * 12
    payment = principal * (monthly_rate * (1 + monthly_rate) ** n) / ((1 + monthly_rate) ** n - 1)
    return round(payment, 2)


def total_payment(principal, annual_rate, years):
    """Общая сумма всех выплат."""
    return round(monthly_payment(principal, annual_rate, years) * years * 12, 2)


def overpayment(principal, annual_rate, years):
    """Переплата по процентам."""
    return round(total_payment(principal, annual_rate, years) - principal, 2)