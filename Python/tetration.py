def tetrate(n, a):
    # Tetration is just like this : ⁿa
    # So we have n, a for factor.
    # WARNING : Never put big numbers. It may stop the system.
    m = a
    temp = 0
    for i in range(0, n):
        temp = m ** a
        m = temp
    return m