def square_sum(n):
    """
    计算数列 1² + 2² + 3² + ... + n² 的和
    
    数列定义：S(n) = 1² + 2² + 3² + ... + n²
    
    数学公式：S(n) = n(n+1)(2n+1)/6
    
    Args:
        n (int): 数列的项数，必须是非负整数
        
    Returns:
        int: 数列的和
        
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
    
    # 使用数学公式计算：S(n) = n(n+1)(2n+1)/6
    return n * (n + 1) * (2 * n + 1) // 6


def square_sum_iterative(n):
    """
    使用迭代方法计算数列 1² + 2² + 3² + ... + n² 的和
    
    Args:
        n (int): 数列的项数，必须是非负整数
        
    Returns:
        int: 数列的和
    """
    # 参数验证
    if not isinstance(n, int):
        raise TypeError("参数n必须是整数")
    
    if n < 0:
        raise ValueError("参数n必须是非负整数")
    
    # 基础情况
    if n == 0:
        return 0
    
    # 使用循环迭代计算
    result = 0
    for i in range(1, n + 1):
        result += i * i
    
    return result


def square_sum_recursive(n):
    """
    使用递归方法计算数列 1² + 2² + 3² + ... + n² 的和
    
    递归公式：S(n) = n² + S(n-1)
    
    Args:
        n (int): 数列的项数，必须是非负整数
        
    Returns:
        int: 数列的和
    """
    # 参数验证
    if not isinstance(n, int):
        raise TypeError("参数n必须是整数")
    
    if n < 0:
        raise ValueError("参数n必须是非负整数")
    
    # 基础情况
    if n == 0:
        return 0
    
    # 递归计算：S(n) = n² + S(n-1)
    return n * n + square_sum_recursive(n - 1)


def square_sum_memoization(n, memo=None):
    """
    使用记忆化方法计算数列 1² + 2² + 3² + ... + n² 的和
    
    这种方法结合了递归的简洁性和缓存的高效性
    
    Args:
        n (int): 数列的项数，必须是非负整数
        memo (dict): 用于存储已计算结果的字典
        
    Returns:
        int: 数列的和
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
    
    # 递归计算并存储结果
    memo[n] = n * n + square_sum_memoization(n - 1, memo)
    return memo[n]


def verify_formula():
    """
    验证数学公式的正确性
    
    通过比较公式计算和迭代计算的结果来验证公式
    """
    print("验证数学公式的正确性:")
    print("=" * 50)
    
    test_cases = [1, 2, 3, 4, 5, 10, 20, 50, 100]
    
    for n in test_cases:
        formula_result = square_sum(n)
        iterative_result = square_sum_iterative(n)
        
        print(f"n = {n:3d}: 公式结果 = {formula_result:8d}, 迭代结果 = {iterative_result:8d}")
        
        if formula_result != iterative_result:
            print(f"❌ 错误：n = {n} 时结果不一致")
            return False
    
    print("✅ 所有测试用例都通过，公式验证正确")
    return True


def print_sequence_examples():
    """
    打印数列示例
    """
    print("\n数列示例:")
    print("=" * 50)
    
    examples = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    for n in examples:
        sequence = " + ".join([f"{i}²" for i in range(1, n + 1)])
        result = square_sum(n)
        print(f"n = {n:2d}: {sequence} = {result}") 