import sys; sys.stdin = open('text1.txt', 'r')


# solve1

# from itertools import permutations


# def create_operator():
#     # cnt = sum(operators_cnt)
#     operators = []
#     for i in range(4):
#         for j in range(operators_cnt[i]):
#             if i == 0:
#                 operators.append('+')
#             elif i == 1:
#                 operators.append('-')
#             elif i == 2:
#                 operators.append('*')
#             else:
#                 operators.append('//')
#     return operators


# def calc():
#     min_res = 1000000001
#     max_res = -1000000001
#     for i in range(len(select_operators)):
#         temp = 0
#         for j in range(len(select_operators[i])):
#             if select_operators[i][j] == '+':
#                 if j:
#                     temp += numbers[j + 1]
#                 else:
#                     temp = numbers[j] + numbers[j + 1]
#             elif select_operators[i][j] == '-':
#                 if j:
#                     temp -= numbers[j + 1]
#                 else:
#                     temp = numbers[j] - numbers[j + 1]
#             elif select_operators[i][j] == '*':
#                 if j:
#                     temp *= numbers[j + 1]
#                 else:
#                     temp = numbers[j] * numbers[j + 1]
#             else:
#                 if j:
#                     if temp < 0 or numbers[j + 1] < 0:
#                         temp = -(abs(temp) // abs(numbers[j + 1]))
#                     else:
#                         temp //= numbers[j + 1]
#                 else:
#                     if numbers[j] < 0 or numbers[j + 1] < 0:
#                         temp = abs(numbers[j]) // abs(numbers[j + 1])
#                     else:
#                         temp = numbers[j] // numbers[j + 1]
#         if temp < min_res:
#             min_res = temp
#         if temp > max_res:
#             max_res = temp
#     return min_res, max_res



# for tc in range(1, int(input()) + 1):
#     N = int(input())
#     numbers = list(map(int, input().split()))
#     # +, -, *, // 의 순서
#     operators_cnt = list(map(int, input().split()))
    
#     operators = create_operator()

#     select_operators = list(permutations(operators, N - 1))
#     select_operators = list(set(select_operators))
#     min_res, max_res = calc()
#     print(max_res)
#     print(min_res)


# best solve - backtracking

def backtrack( preVal, size, idx, plus, minus, multi, divide):
    global max, min
    
    if size == N - 1:
        if max < preVal:
            max = preVal
        if min > preVal:
            min = preVal

    else:
        if plus:
            backtrack(preVal + nums[idx], size + 1, idx + 1, plus - 1, minus, multi, divide)
        
        if minus:
            backtrack(preVal - nums[idx], size + 1, idx + 1, plus, minus - 1, multi, divide)

        if multi:
            backtrack(preVal * nums[idx], size + 1, idx + 1, plus, minus, multi - 1, divide)

        if divide:
            if preVal < 0:
                backtrack(-(abs(preVal) // nums[idx]), size + 1, idx + 1, plus, minus, multi, divide - 1)
            else:
                backtrack(preVal // nums[idx], size + 1, idx + 1, plus, minus, multi, divide - 1)



for tc in range(1, int(input()) + 1):
    N = int(input())
    nums = list(map(int, input().split()))
    oper = list(map(int, input().split()))

    max = -(10 ** 9 + 1)
    min = 10 ** 9 + 1
    backtrack(nums[0], 0, 1, *oper)
    print(max, min, sep="\n")