"""
Stack
'() {} []' 를 포함하고 있는 문자열 s가 주어졌을 때, 괄호가 유효한지 아닌지 판별하시오. 
제약조건 1 <=s.length <=10⁴


n²으로는 풀면 안됨. 10⁸을 넘어가니깐 

"""


"""
접근방법 
1. 여는게 있으먄 닫는게 있어야 함.(짝수) 
2. 여는게 먼저

여는 괄호 +1 닫는거 -1 
0이 나오면 짝이 맞는거다. 

-1이 있으면 닫는게 먼저 온거. 
가장 최근에 들어온 괄호가 닫히기전에 다른 괄호가 닫히면 안 됨(LIFO)
"""

def isValid(s):
    stack = [] 

    for p in s: 
        if p =="(":
            stack.append(")")
        elif p == "{":
            stack.append("}")
        elif p == "[":
            stack.appned("]")
        elif not stack or stack.pop() != p:
            return False
    return not stack
        