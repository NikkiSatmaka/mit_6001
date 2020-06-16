# s = 'azcbobobegghakl'
# s = 'abcbcd'
s = 'abcab cd'

answer = ""
tmp_answer = ""

for i in range(len(s)):

    if s[i] >= s[i - 1]:
        tmp_answer += s[i]
    else:
        if len(answer) < len(tmp_answer):
            answer = tmp_answer
        tmp_answer = s[i]

    if (i == len(s) - 1) & (len(answer) < len(tmp_answer)):
        answer = tmp_answer

print(f"Longest substring in alphabetical order is: {answer}")
