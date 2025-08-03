#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
数列求和计算示例

这个文件展示了如何计算数列 1² + 2² + 3² + ... + n² 的和。
"""

from square_sum import (
    square_sum, 
    square_sum_iterative, 
    square_sum_recursive, 
    square_sum_memoization,
    verify_formula,
    print_sequence_examples
)


def main():
    """主函数，展示数列求和的计算"""
    print("数列求和计算示例")
    print("=" * 60)
    print("计算数列：1² + 2² + 3² + ... + n²")
    print("=" * 60)
    
    # 验证数学公式
    print("\n1. 验证数学公式的正确性:")
    verify_formula()
    
    # 打印数列示例
    print("\n2. 数列示例:")
    print_sequence_examples()
    
    print("\n" + "=" * 60)
    
    # 比较不同方法的性能
    print("3. 性能比较:")
    
    import time
    
    test_cases = [10, 100, 500]
    
    for n in test_cases:
        print(f"\n计算 n = {n} 时的数列和:")
        
        # 测试公式方法
        start_time = time.time()
        result1 = square_sum(n)
        formula_time = time.time() - start_time
        
        # 测试迭代方法
        start_time = time.time()
        result2 = square_sum_iterative(n)
        iterative_time = time.time() - start_time
        
        # 测试记忆化方法
        start_time = time.time()
        result3 = square_sum_memoization(n)
        memoization_time = time.time() - start_time
        
        # 测试递归方法（仅用于小值）
        if n <= 20:  # 避免栈溢出
            start_time = time.time()
            result4 = square_sum_recursive(n)
            recursive_time = time.time() - start_time
            print(f"  递归方法: {result4:10d}, 耗时: {recursive_time:.6f}秒")
        
        print(f"  公式方法: {result1:10d}, 耗时: {formula_time:.6f}秒")
        print(f"  迭代方法: {result2:10d}, 耗时: {iterative_time:.6f}秒")
        print(f"  记忆化方法: {result3:10d}, 耗时: {memoization_time:.6f}秒")
    
    print("\n" + "=" * 60)
    
    # 错误处理示例
    print("4. 错误处理示例:")
    
    try:
        square_sum(-1)
    except ValueError as e:
        print(f"负数输入错误: {e}")
    
    try:
        square_sum(3.14)
    except TypeError as e:
        print(f"非整数输入错误: {e}")
    
    try:
        square_sum("abc")
    except TypeError as e:
        print(f"字符串输入错误: {e}")
    
    print("\n" + "=" * 60)
    
    # 数学公式说明
    print("5. 数学公式说明:")
    print("数列 1² + 2² + 3² + ... + n² 的和可以用以下公式计算:")
    print("S(n) = n(n+1)(2n+1)/6")
    print("\n这个公式的推导:")
    print("- 可以通过数学归纳法证明")
    print("- 也可以通过积分近似推导")
    print("- 是平方数列求和的标准公式")
    
    # 实际应用示例
    print("\n6. 实际应用示例:")
    print("假设我们要计算前10个自然数的平方和:")
    n = 10
    result = square_sum(n)
    sequence = " + ".join([f"{i}²" for i in range(1, n + 1)])
    print(f"计算: {sequence}")
    print(f"结果: {result}")
    print(f"验证: {n} × {n+1} × {2*n+1} ÷ 6 = {n*(n+1)*(2*n+1)//6}")


if __name__ == "__main__":
    main() 