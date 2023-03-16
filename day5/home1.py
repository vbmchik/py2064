class stringsSort():
    
    def clearword(self, word):
        cleanword = ''.join([x for x in word if x.isalpha() or x == ' '])
        return cleanword
    
    def __init__(self, text) -> None:
        self.text = self.clearword(text)
        words = list(filter(lambda x: x != '', self.text.split(" ")))
        self.wordcount = {}
        for word in words:
            if not word in self.wordcount:
                self.wordcount[word] = 1
            else:
                self.wordcount[word] = self.wordcount[word] + 1

    def __str__(self):
        return f"text with len {len(self.wordcount)}"
