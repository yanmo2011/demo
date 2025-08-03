def fibonacci(n):
    """
    计算斐波那契数列的第n个元素的值
    
    斐波那契数列定义：F(0) = 0, F(1) = 1, F(n) = F(n-1) + F(n-2) (n >= 2)
    
    Args:
        n (int): 要计算的斐波那契数列的索引，必须是非负整数
        
    Returns:
        int: 斐波那契数列第n个元素的值
        
    Raises:
        ValueError: 当n为负数时抛出异常
        TypeError: 当n不是整数时抛出异常
    """
    # 参数验证
    if not isinstance(n, int):
        raise TypeError("参数n必须是整数")
    
    if n < 0:
        raise ValueError("参数n必须是非负整数")
    
    # 基础情况
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    # 使用迭代方法计算，避免递归的栈溢出问题
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
        # a = 1, b = 1, _ = 2
        # a = 1, b = 2, _ = 3
        # a = 2, b = 3, _ = 4
        # a = 3, b = 5, _ = 5
        # a = 5, b = 8, _ = 6
        # a = 8, b = 13, _ = 7
        # a = 13, b = 21, _ = 8
        # a = 21, b = 34, _ = 9
        # a = 34, b = 55, _ = 10
        # a = 55, b = 89, _ = 11
        # a = 89, b = 144, _ = 12
        # a = 144, b = 233, _ = 13
        # a = 233, b = 377, _ = 14

    # 解释左闭右开 [2, n + 1)
    # [2, 9) : 2, 3, 4, 5, 6, 7, 8
    # [2, 9] : 2, 3, 4, 5, 6, 7, 8, 9
    return b




def fibonacci_recursive(n):
    """
    使用递归方法计算斐波那契数列的第n个元素的值
    
    注意：此方法仅适用于较小的n值，大值会导致栈溢出
    
    Args:
        n (int): 要计算的斐波那契数列的索引，必须是非负整数
        
    Returns:
        int: 斐波那契数列第n个元素的值
    """
    # 参数验证
    if not isinstance(n, int):
        raise TypeError("参数n必须是整数")
    
    if n < 0:
        raise ValueError("参数n必须是非负整数")
    
    # 基础情况
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    # 递归计算
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def fibonacci_memoization(n, memo=None):
    """
    使用记忆化方法计算斐波那契数列的第n个元素的值
    
    这种方法结合了递归的简洁性和迭代的效率
    
    Args:
        n (int): 要计算的斐波那契数列的索引，必须是非负整数
        memo (dict): 用于存储已计算结果的字典
        
    Returns:
        int: 斐波那契数列第n个元素的值
    """
    # 参数验证
    if not isinstance(n, int):
        raise TypeError("参数n必须是整数")
    
    if n < 0:
        raise ValueError("参数n必须是非负整数")
    
    # 初始化记忆字典
    if memo is None:
        memo = {}
    
    # 检查是否已经计算过
    if n in memo:
        return memo[n]
    
    # 基础情况
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    # 递归计算并存储结果
    memo[n] = fibonacci_memoization(n - 1, memo) + fibonacci_memoization(n - 2, memo)
    return memo[n] 