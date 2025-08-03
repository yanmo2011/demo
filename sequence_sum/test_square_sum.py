import unittest
import sys
import os

# 添加当前目录到Python路径，以便导入模块
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from square_sum import (
    square_sum, 
    square_sum_iterative, 
    square_sum_recursive, 
    square_sum_memoization,
    verify_formula,
    print_sequence_examples
)


class TestSquareSum(unittest.TestCase):
    """数列求和函数的单元测试类"""
    
    def test_square_sum_basic_cases(self):
        """测试基础情况"""
        # 手动计算前几个数列和
        # n=1: 1² = 1
        # n=2: 1² + 2² = 1 + 4 = 5
        # n=3: 1² + 2² + 3² = 1 + 4 + 9 = 14
        # n=4: 1² + 2² + 3² + 4² = 1 + 4 + 9 + 16 = 30
        # n=5: 1² + 2² + 3² + 4² + 5² = 1 + 4 + 9 + 16 + 25 = 55
        
        self.assertEqual(square_sum(0), 0)
        self.assertEqual(square_sum(1), 1)
        self.assertEqual(square_sum(2), 5)
        self.assertEqual(square_sum(3), 14)
        self.assertEqual(square_sum(4), 30)
        self.assertEqual(square_sum(5), 55)
        self.assertEqual(square_sum(6), 91)
        self.assertEqual(square_sum(7), 140)
        self.assertEqual(square_sum(8), 204)
        self.assertEqual(square_sum(9), 285)
        self.assertEqual(square_sum(10), 385)
    
    def test_square_sum_larger_numbers(self):
        """测试较大的数字"""
        # 使用公式验证：S(n) = n(n+1)(2n+1)/6
        self.assertEqual(square_sum(20), 2870)  # 20*21*41/6 = 2870
        self.assertEqual(square_sum(50), 42925)  # 50*51*101/6 = 42925
        self.assertEqual(square_sum(100), 338350)  # 100*101*201/6 = 338350
    
    def test_square_sum_negative_input(self):
        """测试负数输入"""
        with self.assertRaises(ValueError):
            square_sum(-1)
        with self.assertRaises(ValueError):
            square_sum(-10)
    
    def test_square_sum_invalid_input(self):
        """测试无效输入"""
        with self.assertRaises(TypeError):
            square_sum(3.14)
        with self.assertRaises(TypeError):
            square_sum("5")
        with self.assertRaises(TypeError):
            square_sum([1, 2, 3])
        with self.assertRaises(TypeError):
            square_sum(None)
    
    def test_square_sum_iterative_basic_cases(self):
        """测试迭代方法的基础情况"""
        self.assertEqual(square_sum_iterative(0), 0)
        self.assertEqual(square_sum_iterative(1), 1)
        self.assertEqual(square_sum_iterative(2), 5)
        self.assertEqual(square_sum_iterative(3), 14)
        self.assertEqual(square_sum_iterative(4), 30)
        self.assertEqual(square_sum_iterative(5), 55)
        self.assertEqual(square_sum_iterative(6), 91)
        self.assertEqual(square_sum_iterative(7), 140)
        self.assertEqual(square_sum_iterative(8), 204)
        self.assertEqual(square_sum_iterative(9), 285)
        self.assertEqual(square_sum_iterative(10), 385)
    
    def test_square_sum_iterative_larger_numbers(self):
        """测试迭代方法的较大数字"""
        self.assertEqual(square_sum_iterative(20), 2870)
        self.assertEqual(square_sum_iterative(50), 42925)
        self.assertEqual(square_sum_iterative(100), 338350)
    
    def test_square_sum_iterative_negative_input(self):
        """测试迭代方法的负数输入"""
        with self.assertRaises(ValueError):
            square_sum_iterative(-1)
        with self.assertRaises(ValueError):
            square_sum_iterative(-10)
    
    def test_square_sum_iterative_invalid_input(self):
        """测试迭代方法的无效输入"""
        with self.assertRaises(TypeError):
            square_sum_iterative(3.14)
        with self.assertRaises(TypeError):
            square_sum_iterative("5")
    
    def test_square_sum_recursive_basic_cases(self):
        """测试递归方法的基础情况"""
        self.assertEqual(square_sum_recursive(0), 0)
        self.assertEqual(square_sum_recursive(1), 1)
        self.assertEqual(square_sum_recursive(2), 5)
        self.assertEqual(square_sum_recursive(3), 14)
        self.assertEqual(square_sum_recursive(4), 30)
        self.assertEqual(square_sum_recursive(5), 55)
        self.assertEqual(square_sum_recursive(6), 91)
        self.assertEqual(square_sum_recursive(7), 140)
        self.assertEqual(square_sum_recursive(8), 204)
        self.assertEqual(square_sum_recursive(9), 285)
        self.assertEqual(square_sum_recursive(10), 385)
    
    def test_square_sum_recursive_negative_input(self):
        """测试递归方法的负数输入"""
        with self.assertRaises(ValueError):
            square_sum_recursive(-1)
        with self.assertRaises(ValueError):
            square_sum_recursive(-10)
    
    def test_square_sum_recursive_invalid_input(self):
        """测试递归方法的无效输入"""
        with self.assertRaises(TypeError):
            square_sum_recursive(3.14)
        with self.assertRaises(TypeError):
            square_sum_recursive("5")
    
    def test_square_sum_memoization_basic_cases(self):
        """测试记忆化方法的基础情况"""
        self.assertEqual(square_sum_memoization(0), 0)
        self.assertEqual(square_sum_memoization(1), 1)
        self.assertEqual(square_sum_memoization(2), 5)
        self.assertEqual(square_sum_memoization(3), 14)
        self.assertEqual(square_sum_memoization(4), 30)
        self.assertEqual(square_sum_memoization(5), 55)
        self.assertEqual(square_sum_memoization(6), 91)
        self.assertEqual(square_sum_memoization(7), 140)
        self.assertEqual(square_sum_memoization(8), 204)
        self.assertEqual(square_sum_memoization(9), 285)
        self.assertEqual(square_sum_memoization(10), 385)
    
    def test_square_sum_memoization_larger_numbers(self):
        """测试记忆化方法的较大数字"""
        self.assertEqual(square_sum_memoization(20), 2870)
        self.assertEqual(square_sum_memoization(50), 42925)
        self.assertEqual(square_sum_memoization(100), 338350)
    
    def test_square_sum_memoization_negative_input(self):
        """测试记忆化方法的负数输入"""
        with self.assertRaises(ValueError):
            square_sum_memoization(-1)
        with self.assertRaises(ValueError):
            square_sum_memoization(-10)
    
    def test_square_sum_memoization_invalid_input(self):
        """测试记忆化方法的无效输入"""
        with self.assertRaises(TypeError):
            square_sum_memoization(3.14)
        with self.assertRaises(TypeError):
            square_sum_memoization("5")
    
    def test_all_methods_consistency(self):
        """测试所有方法的一致性"""
        test_cases = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 25]
        
        for n in test_cases:
            result1 = square_sum(n)
            result2 = square_sum_iterative(n)
            result3 = square_sum_recursive(n)
            result4 = square_sum_memoization(n)
            
            self.assertEqual(result1, result2, f"公式方法和迭代方法在n={n}时结果不一致")
            self.assertEqual(result1, result3, f"公式方法和递归方法在n={n}时结果不一致")
            self.assertEqual(result1, result4, f"公式方法和记忆化方法在n={n}时结果不一致")
            self.assertEqual(result2, result3, f"迭代方法和递归方法在n={n}时结果不一致")
            self.assertEqual(result2, result4, f"迭代方法和记忆化方法在n={n}时结果不一致")
            self.assertEqual(result3, result4, f"递归方法和记忆化方法在n={n}时结果不一致")
    
    def test_formula_verification(self):
        """测试数学公式验证函数"""
        # 这个测试会调用verify_formula函数
        result = verify_formula()
        self.assertTrue(result, "数学公式验证失败")
    
    def test_sequence_examples(self):
        """测试数列示例打印函数"""
        # 这个测试会调用print_sequence_examples函数
        # 主要测试函数是否能正常运行，不检查输出
        try:
            print_sequence_examples()
            # 如果没有抛出异常，测试通过
            self.assertTrue(True)
        except Exception as e:
            self.fail(f"print_sequence_examples函数执行失败: {e}")


class TestSquareSumPerformance(unittest.TestCase):
    """性能测试类"""
    
    def test_performance_comparison(self):
        """比较不同方法的性能"""
        import time
        
        n = 100  # 选择一个适中的值来测试性能
        
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
        
        # 验证结果一致性
        self.assertEqual(result1, result2)
        self.assertEqual(result1, result3)
        
        # 输出性能比较（可选）
        print(f"\n性能测试结果 (n={n}):")
        print(f"公式方法耗时: {formula_time:.6f}秒")
        print(f"迭代方法耗时: {iterative_time:.6f}秒")
        print(f"记忆化方法耗时: {memoization_time:.6f}秒")
        
        # 注意：递归方法对于较大的n会很慢，所以这里不测试


if __name__ == '__main__':
    # 运行所有测试
    unittest.main(verbosity=2) 