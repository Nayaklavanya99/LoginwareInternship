import re

def stringVal(N, strings):
    result = []
    for s in strings:
        # Check if the string matches the pattern
        if re.match(r'^[a-zA-Z].{1,}\d$', s):
            result.append(1)  # valid product code
        else:
            result.append(0)  # invalid product code
    return result

if __name__ == "__main__":
    N = int(input())
    strings = [input().strip() for _ in range(N)]
    results = stringVal(N, strings)
    for res in results:
        print(res)
