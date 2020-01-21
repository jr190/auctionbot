buyingNorm = ["wtb","buy","looking for","ltb"]
sellingNorm = ['lts', "sell","looking to","wts"]
def isBuying(rawMessage,buyingNorm):
    rawMessage = message.lower()
    for buy in buyingNorm:
        if buy in rawMessage:
            return True
def findKeys(rawMessage,keys):
    returnKeys = []
    for key in keys:
        if key in rawMessage:
            returnKeys.append(key)
    return returnKeys
def isSelling(rawMessage,sellingNorm):
    rawMessage = message.lower()
    for sell in sellingNorm:
        if sell in rawMessage:
            return True

    
messages = ["looking for mando", "i am LTB a gun","want to sell a schem","lts resource crate","wtb mando helm and lts aug crit 25s"]
        
for message in messages:
	message = message.lower()
	if isBuying(message,buyingNorm) is True and isSelling(message,sellingNorm) is True:
		print(message,str(findKeys(message,buyingNorm+sellingNorm)))
	elif isBuying(message,buyingNorm) is True:
		print(message,str(findKeys(message,buyingNorm)))
	elif isSelling(message,sellingNorm) is True:
		print(message,str(findKeys(message,sellingNorm)))
