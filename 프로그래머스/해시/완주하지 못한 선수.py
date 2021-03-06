def solution(participant, completion):
    dict = {}
    for i in participant:
        dict[i] = dict.get(i, 0) + 1
    for i in completion:
        dict[i] -= 1
    answer = [k for k, v in dict.items() if v > 0]
    return answer[0]
