def merge_the_tools(string, k):
    # your code goes here
    n = len(string)
    index = 0
    count = 0
    for i in range(n//k):
        substring = string[k*i:(k*i)+k]
        substring_output = ""
        for j in range(len(substring)-1, -1, -1):
            if substring[j] not in substring[:j]:
                substring_output += substring[j]
        print(substring_output[::-1])
            

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
