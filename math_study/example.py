#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
斐波那契数列计算示例

这个文件展示了如何使用不同的方法计算斐波那契数列。
"""

from fibonacci import fibonacci, fibonacci_recursive, fibonacci_memoization


def main():
    """主函数，展示斐波那契数列的计算"""
    print("斐波那契数列计算示例")
    print("=" * 50)
    
    # 计算前15个斐波那契数
    print("前15个斐波那契数:")
    for i in range(15):
        result = fibonacci(i)
        print(f"F({i}) = {result}")
    
    print("\n" + "=" * 50)
    
    # 比较不同方法的性能
    print("性能比较 (计算第35个斐波那契数):")
    
    import time
    
    # 测试迭代方法
    start_time = time.time()
    result1 = fibonacci(35)
    iterative_time = time.time() - start_time
    
    # 测试记忆化方法
    start_time = time.time()
    result2 = fibonacci_memoization(35)
    memoization_time = time.time() - start_time
    
    # 测试递归方法（仅用于小值）
    start_time = time.time()
    result3 = fibonacci_recursive(20)  # 使用较小的值避免栈溢出
    recursive_time = time.time() - start_time
    
    print(f"迭代方法: F(35) = {result1}, 耗时: {iterative_time:.6f}秒")
    print(f"记忆化方法: F(35) = {result2}, 耗时: {memoization_time:.6f}秒")
    print(f"递归方法: F(20) = {result3}, 耗时: {recursive_time:.6f}秒")
    
    print("\n" + "=" * 50)
    
    # 错误处理示例
    print("错误处理示例:")
    
    try:
        fibonacci(-1)
    except ValueError as e:
        print(f"负数输入错误: {e}")
    
    try:
        fibonacci(3.14)
    except TypeError as e:
        print(f"非整数输入错误: {e}")
    
    try:
        fibonacci("abc")
    except TypeError as e:
        print(f"字符串输入错误: {e}")


if __name__ == "__main__":
    main() 