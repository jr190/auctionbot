
def isBuying(rawmsg,keywords):
    for key in keywords:
        if key in rawmsg:
            return (key,True)

def isSelling(rawmsg,keywords):
    for key in keywords:
        if key in rawmsg:
            return (key,True)


def asdas(message):
    buyingKeywords = ["wtb", "buy", "looking for", "ltb"]
    sellingKeywords = ["wts", "sell", "looking to", "lts"]

    rawMessage = message.content.lower()
    buyKey,buyBool = isBuying(rawMessage,buyingKeywords)
    sellKey,sellBool = isSelling(rawMessage,sellingKeywords)

    if buyBool is True:
        print(buyKey)
        
    if sellBool is True:
        print(sellKey)


legends = "LTS WG Skull (1/3 pieces required for Lava Crystal) 1m PST with dropoff location"

asdas(legends)