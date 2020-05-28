from googletrans import Translator


def splitInChunks(text):
    splitted=text.split(".")
    length = [len(x) for x in splitted ]
    m = max(length)
    for ch in splitted:
        print("----------------")
        print(ch)
    print(m)
def transalteChunk(chunk):
    return chunk

def tranlateText(text):
    translator = Translator()
    # result = translator.translate(content, src='en', dest='it')