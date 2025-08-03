import unittest
import sys
import os

# 添加当前目录到Python路径，以便导入模块
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from fibonacci import fibonacci, fibonacci_recursive, fibonacci_memoization


class TestFibonacci(unittest.TestCase):
    """斐波那契数列函数的单元测试类"""
    
    def test_fibonacci_basic_cases(self):
        """测试基础情况"""
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(2), 1)
        self.assertEqual(fibonacci(3), 2)
        self.assertEqual(fibonacci(4), 3)
        self.assertEqual(fibonacci(5), 5)
        self.assertEqual(fibonacci(6), 8)
        self.assertEqual(fibonacci(7), 13)
        self.assertEqual(fibonacci(8), 21)
        self.assertEqual(fibonacci(9), 34)
        self.assertEqual(fibonacci(10), 55)
    
    def test_fibonacci_larger_numbers(self):
        """测试较大的数字"""
        self.assertEqual(fibonacci(20), 6765)
        self.assertEqual(fibonacci(25), 75025)
        self.assertEqual(fibonacci(30), 832040)
    
    def test_fibonacci_negative_input(self):
        """测试负数输入"""
        with self.assertRaises(ValueError):
            fibonacci(-1)
        with self.assertRaises(ValueError):
            fibonacci(-10)
    
    def test_fibonacci_invalid_input(self):
        """测试无效输入"""
        with self.assertRaises(TypeError):
            fibonacci(3.14)
        with self.assertRaises(TypeError):
            fibonacci("5")
        with self.assertRaises(TypeError):
            fibonacci([1, 2, 3])
        with self.assertRaises(TypeError):
            fibonacci(None)
    
    def test_fibonacci_recursive_basic_cases(self):
        """测试递归方法的基础情况"""
        self.assertEqual(fibonacci_recursive(0), 0)
        self.assertEqual(fibonacci_recursive(1), 1)
        self.assertEqual(fibonacci_recursive(2), 1)
        self.assertEqual(fibonacci_recursive(3), 2)
        self.assertEqual(fibonacci_recursive(4), 3)
        self.assertEqual(fibonacci_recursive(5), 5)
        self.assertEqual(fibonacci_recursive(6), 8)
        self.assertEqual(fibonacci_recursive(7), 13)
        self.assertEqual(fibonacci_recursive(8), 21)
        self.assertEqual(fibonacci_recursive(9), 34)
        self.assertEqual(fibonacci_recursive(10), 55)
    
    def test_fibonacci_recursive_negative_input(self):
        """测试递归方法的负数输入"""
        with self.assertRaises(ValueError):
            fibonacci_recursive(-1)
        with self.assertRaises(ValueError):
            fibonacci_recursive(-10)
    
    def test_fibonacci_recursive_invalid_input(self):
        """测试递归方法的无效输入"""
        with self.assertRaises(TypeError):
            fibonacci_recursive(3.14)
        with self.assertRaises(TypeError):
            fibonacci_recursive("5")
    
    def test_fibonacci_memoization_basic_cases(self):
        """测试记忆化方法的基础情况"""
        self.assertEqual(fibonacci_memoization(0), 0)
        self.assertEqual(fibonacci_memoization(1), 1)
        self.assertEqual(fibonacci_memoization(2), 1)
        self.assertEqual(fibonacci_memoization(3), 2)
        self.assertEqual(fibonacci_memoization(4), 3)
        self.assertEqual(fibonacci_memoization(5), 5)
        self.assertEqual(fibonacci_memoization(6), 8)
        self.assertEqual(fibonacci_memoization(7), 13)
        self.assertEqual(fibonacci_memoization(8), 21)
        self.assertEqual(fibonacci_memoization(9), 34)
        self.assertEqual(fibonacci_memoization(10), 55)
    
    def test_fibonacci_memoization_larger_numbers(self):
        """测试记忆化方法的较大数字"""
        self.assertEqual(fibonacci_memoization(20), 6765)
        self.assertEqual(fibonacci_memoization(25), 75025)
        self.assertEqual(fibonacci_memoization(30), 832040)
    
    def test_fibonacci_memoization_negative_input(self):
        """测试记忆化方法的负数输入"""
        with self.assertRaises(ValueError):
            fibonacci_memoization(-1)
        with self.assertRaises(ValueError):
            fibonacci_memoization(-10)
    
    def test_fibonacci_memoization_invalid_input(self):
        """测试记忆化方法的无效输入"""
        with self.assertRaises(TypeError):
            fibonacci_memoization(3.14)
        with self.assertRaises(TypeError):
            fibonacci_memoization("5")
    
    def test_all_methods_consistency(self):
        """测试所有方法的一致性"""
        test_cases = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20]
        
        for n in test_cases:
            result1 = fibonacci(n)
            result2 = fibonacci_recursive(n)
            result3 = fibonacci_memoization(n)
            
            self.assertEqual(result1, result2, f"迭代方法和递归方法在n={n}时结果不一致")
            self.assertEqual(result1, result3, f"迭代方法和记忆化方法在n={n}时结果不一致")
            self.assertEqual(result2, result3, f"递归方法和记忆化方法在n={n}时结果不一致")
    
    def test_fibonacci_sequence_correctness(self):
        """测试斐波那契数列的正确性"""
        # 验证前20个斐波那契数
        expected_sequence = [
            0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181
        ]
        
        for i, expected in enumerate(expected_sequence):
            result = fibonacci(i)
            self.assertEqual(result, expected, f"第{i}个斐波那契数应该是{expected}，但得到了{result}")


class TestFibonacciPerformance(unittest.TestCase):
    """性能测试类"""
    
    def test_performance_comparison(self):
        """比较不同方法的性能"""
        import time
        
        n = 35  # 选择一个适中的值来测试性能
        
        # 测试迭代方法
        start_time = time.time()
        result1 = fibonacci(n)
        iterative_time = time.time() - start_time
        
        # 测试记忆化方法
        start_time = time.time()
        result2 = fibonacci_memoization(n)
        memoization_time = time.time() - start_time
        
        # 验证结果一致性
        self.assertEqual(result1, result2)
        
        # 输出性能比较（可选）
        print(f"\n性能测试结果 (n={n}):")
        print(f"迭代方法耗时: {iterative_time:.6f}秒")
        print(f"记忆化方法耗时: {memoization_time:.6f}秒")
        
        # 注意：递归方法对于较大的n会很慢，所以这里不测试


if __name__ == '__main__':
    # 运行所有测试
    unittest.main(verbosity=2) 