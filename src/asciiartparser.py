#coding=utf-8




class AsciiArtParser():
    def __init__(self):
        self.fullText = None
        self.boxes = []

    def doParse(self):
        with open('input/input.txt', 'rb') as rf:
            fullText = []
            for line in rf:
                fullText.append(bytearray(line))
        
        self.fullText = fullText
        for y in range(len(fullText)):
            for x in range(len(fullText[y])):
                char = fullText[y][x]
                if char == ord('+') :
                    self.boxes.append(self._getBoxInfo((x,y)))
        

        print(self.boxes)
        
    def _getBoxInfo(self, spos):
        """
            @param spos (x, y)

        """
        left, top = spos
        ft = self.fullText

        # exist characters at the right and bottom
        if left+1 >= len(ft[top]) or ft[top][left+1] != ord('-'):
            return None
        if top+1 >= len(ft) \
            or left >= len(ft[top+1]) \
            or ft[top+1][left] != ord('|'):
            return None

        for x in range(left+1, len(ft[top])):
            if ft[top][x] == ord('+'):
                right = x
                break
        for y in range(top+1, len(ft)):
            if ft[y][left] == ord('+'):
                bottom = y
                break
        return (left, top, right, bottom)



def main():
    ap = AsciiArtParser()
    ap.doParse()


if __name__ == "__main__":
    main()


