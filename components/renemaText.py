class RenameText:
    def __init__(self, *args, **kwargs) -> None:
        self.text = None

    @property
    def renameHeader(self):
        return self.text
    
    @renameHeader.setter
    def renameHeader(self, text):
        text = text.replace('\n', '&&&&&')
        for _ in range(10):
            text = text.replace('  ', ' ')
        self.text = ''
        countEnd = 0
        for letter in text:
            if letter == '&':
                countEnd += 1
                if countEnd >= 3:
                    break
                continue
            else: 
                self.text += letter