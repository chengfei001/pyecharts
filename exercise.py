# 计算银行存款利率
def sum(money, accrual, n):
    # money = money * accrual
    if n == 0:
        return money

    return accrual * sum(money, accrual, n - 1)


if __name__ == '__main__':
    print(sum(10, 1.05, 2))
