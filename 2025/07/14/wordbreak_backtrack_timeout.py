def sol(s, wordDict):
    idx = 0
    backlen = 0

    word_set = set(wordDict)

    def backtrack(str_, idx, backlen):
        print(f"{str_=}")
        print(f"{idx=}")
        print(f"{backlen=}")
        # base condition
        if str_ in word_set:
            print(f"flag!!!")
            return True
        for item in wordDict:
            if str_.startswith(item):
                print(f"{item=}")
                n = len(item)
                if backtrack(str_[n:], idx + n, n):
                    return True
        else:
            return False

    return backtrack(s, idx, backlen)

if __name__ == '__main__':
    # s = "catsandog"
    # wordDict = ["cats","dog","sand","and","cat"]
    # s = "leetcode"
    # wordDict = ["leet","code"]
    s = "cars"
    wordDict = ["car","ca","rs"]
    res = sol(s, wordDict)
    print(res)
