"""
Let's create a function that counts words in a sentence!
"""
def count_words(text):
    """
    this function counts words
    param sentence: string containing words
    """
    if not isinstance(text, str):
        raise TypeError("word counter accepts only strings")
    normal_word_splits = text.split(" ")
    new_words = []
    for asplit in normal_word_splits:
        if "\n" in asplit:
            new_words.append(asplit.split("\n"))
        elif "-" in asplit:
            new_words.append(asplit.split("-"))
        else:
            new_words.append(asplit)
    one_list = []
    for i in new_words:
        if isinstance(i, list):
            for j in i:
                one_list.append(j)
        else:
            one_list.append(i)
    return len(one_list)

if __name__ == '__main__':
    SENTENCE = "my\nname\nis\njoseph in this"
    #SENTENCE = "my name is joseph"
    print("")
    print(count_words(SENTENCE))
    print("")
