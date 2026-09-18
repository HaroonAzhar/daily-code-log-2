# 151. Reverse Words in a String
def reverseWords(self, s: str) -> str:
    words = s.split(" ")
    res = ""

    for i in range(len(words) - 1, -1, -1):
        word = words[i]

        if word == "":
            continue

        if res != "":
            res += " "

        res += word

    return res