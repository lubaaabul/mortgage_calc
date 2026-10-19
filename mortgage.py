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


if __name__ == "__main__":
    print("=== Ипотечный калькулятор")
    try:
        principal = float(input("Введите сумму кредита (руб.): "))
        annual_rate = float(input("Введите годовую ставку (например, 12): "))
        years = int(input("Введите срок кредита (лет): "))

        m_pay = monthly_payment(principal, annual_rate, years)
        t_pay = total_payment(principal, annual_rate, years)
        over = overpayment(principal, annual_rate, years)

        print("-" * 40)
        print(f"Ежемесячный платеж: {m_pay:,.2f} руб.")
        print(f"Общая сумма выплат: {t_pay:,.2f} руб.")
        print(f"Переплата по процентам: {over:,.2f} руб.")
        print("-" * 40)

    except ValueError:
        print("Ошибка: пожалуйста, вводите только числа.")
