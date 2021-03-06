# first solve

# from collections import Counter

# def solution(participant, completion):
#     participant_lst = Counter(participant)
#     completion_lst = Counter(completion)

#     if len(participant_lst) != len(completion_lst):
#         for key in participant_lst.keys():
#             if key not in completion_lst:
#                 return key
#     else:
#         for key, val in participant_lst.items():
#             if completion_lst[key] != val:
#                 return key

    # answer = ''
    # return answer



# best solve

# from collections import Counter

# def solution(participant, completion):
#     answer = Counter(participant) - Counter(completion)
#     return list(answer.keys())[0]



# hash solve

def solution(participant, completion):
    answer = ''
    temp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part
        temp += int(hash(part))
    for com in completion:
        temp -= hash(com)
    answer = dic[temp]

    return answer



print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))
print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))

# answer
# "leo"
# "vinko"
# "mislav"