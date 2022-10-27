#Amanda Miloserny
string = "SPAM!HelloSPAM! worldSPAM!"
def replace_substring(string, word, replace):
    list = []
    index = 0
    while index < len(string):
        if string[index:index + len(word)]==word:
            index += len(word)
        else:
            list.append(string[index])
            index += 1
    print("".join(list))

replace_substring(string, "SPAM!", " ")
