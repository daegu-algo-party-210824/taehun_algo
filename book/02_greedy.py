from memory_profiler import profile

"""
page : pg311 ~
"""

def adven_guild():
    string = '23122'
    s = [int(i) for i in string]
    try:
        for i in range(len(s)):
            for ii in range(len(s)):
                group = s[i+1] + s[ii+i]
                if s[i] == group:
                    print(s[i])
    except:
        pass





def multi_plus():
    s = '5671'
    s = [int(i) for i in s]
    answer = 1
    for n in s:
        if n != 0:
            answer = answer * n
        if n == 1:
            answer = answer + 1
    print(answer)

def str_reverse():
    string = '0001100'
    string_list = [ int(i) for i in string]

    index_num = []
    count = 0
    for i in range(len(string_list)):
        if string_list[i] == 1:
            string_list[i] = 0

    print(string_list)



multi_plus()
