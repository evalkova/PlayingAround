class Solution(object):
    def two_sum(self, nums, target):

        def __init__(self):
            print("init")  # never prints
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        Given an array of integers, return indices of the two numbers such that they add up to a specific target.
        You may assume that each input would have exactly one solution, and you may not use the same element twice.
        """
        for i in range(len(nums)):
            for n in range(len(nums)):
                if nums[i] + nums[n] == target:
                    if i != n:
                        print (i, n)
                        return


    def roman_to_int(self, s):
        """
        :type s: str
        :rtype: int
        """
        # dict of lists - first value is the int value, second value is the number that needs to be substracted if it is
        # before that number
        roman_in_dict = {'I': [1, None], 'V': [5, 'I'], 'X': [10, 'I'], 'L': [50, 'X'], 'C': [100, 'X'], 'D': [500, 'C'],
                        'M': [1000, 'C']}
        result = 0
        try:
            for position, character in enumerate(s):
                try:
                    if position != 0 and s[position-1] == roman_in_dict[character][1]:
                        result += (roman_in_dict[character][0]-roman_in_dict[s[position-1]][0])-roman_in_dict[s[position-1]][0]
                    else:
                        result += roman_in_dict[character][0]
                except KeyError:
                    print(s[0] + ' is not a valid Roman character!')
                    return
        except TypeError:
            print('Please enter a string character!')
        print(result)


    def fizz_buzz(self):
        for num in range(1,50):
            if num % 3 is 0 and num % 5 is 0: #or num % 15 is 0
                print('FizzBuzz')
            elif num % 3 is 0:
                print('Fizz')
            elif num % 5 is 0:
                print('Buzz')
            else:
                print(num)

    def reverse_int(self, x): #32 bit constrains

        if x >0:
            result = int(str(x)[::-1])
            if abs(result) < 2**31 and result != 2**31 - 1:
                print(result)
                print(result)
            else:
                print(0)
        else:
            result = int("-"+str(abs(x))[::-1])
            if abs(result) < 2**31 and result != 2**31 - 1:
                print(result)
            else:
                print(0)


    def plus_one(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        incrementor = True
        position = len(digits) - 1

        while incrementor:
            ldigit = digits[position]
            if position == -1:
                digits.insert(0, 1)
                incrementor = False
                '''
                if all digits have been incremented and incrementor is still true
                prepend a new digit of 1
                '''
            elif ldigit >= 9:
                replace = 0
                digits[position] = replace
                position -= 1
                '''
                the digit is 9 so it must be reset to 0 and the next digit to the left incremented by 1
                '''
            else:
                replace = ldigit + 1
                digits[position] = replace
                incrementor = False
                '''
                just increment the last digit with no shifting
                '''
        print(digits)


    def generate_pascal_triangle(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]] - each number is the sum of the two numbers directly above it
        #[[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
        """

        pascal = []
        total = 0
        for i in range(1, numRows + 1):
            if i == 1:
                inner = [1]
            if i == 2:
                inner = [1, 1]
            elif i > 2:
                inner = [1]

                for j in range(len(pascal[-1]) - 1):
                    total = pascal[-1][j] + pascal[-1][j + 1]
                    inner.append(total)
                inner.append(1)
            pascal.append(inner)

        print(pascal)


    def fibonacci(self, num):
        list = []
        for i in range(1, num+1):
            if i == 1 or i == 2:
                list.append(1)
            elif i > 2:
                list.append(list[i-3]+list[i-2])
        print(list)



if __name__ == '__main__':
    solution = Solution()
    # n = [1, 1, 2]
    # t = 2
    # solution.twoSum(nums=n, target=t)
    # solution.roman_to_int(s=7)
    # solution.fizz_buzz()
    # solution.reverse_int(-2423)
    # solution.plus_one([8,9,9])
    # solution.generate_pascal_triangle(5)
    solution.fibonacci(6)