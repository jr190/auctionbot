import pandas as pd

class item:
	def __init__(self,name,list):
		self.name = name
		self.list = list

file = "itemList.xlsx"
Items = pd.read_excel(file,sheet_name=0, header=0) #2 dimensional list
listOfItems = [] #our csv stored (list of our item objects)

for column in Items.columns:  #column is basically the header to every column (i.e. armor, gun, schematic, etc.
	columnList = Items[column].tolist()	
	listOfItems.append(item(column,columnList))	

newmessages = ['looking to buy blue meth, scout armor rebel, and penis gun',"orange meth","PC Elite tusken"]

compareLists(newmessages,listOfItems)

buyingNorm = ["wtb","buy","looking for","ltb"]
sellingNorm = ['lts', "sell","looking to","wts"]

def compareLists(listOfMessages,listOfItems):
	for message in listOfMessages:
	itemsBeingBought = []
	for item in listOfItems:
		for keyword in item.list:
			if str(keyword) in message.lower():
				itemsBeingBought.append((item.name,str(keyword)))
	print(itemsBeingBought)

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

#messages = ["looking for mando", "i am LTB a gun","want to sell a schem","lts resource crate","wtb mando helm and lts aug crit 25s"]

'''for message in messages:
	message = message.lower()
	if isBuying(message,buyingNorm) is True and isSelling(message,sellingNorm) is True:
		print(message,str(findKeys(message,buyingNorm+sellingNorm)))
	elif isBuying(message,buyingNorm) is True:
		print(message,str(findKeys(message,buyingNorm)))
	elif isSelling(message,sellingNorm) is True:
		print(message,str(findKeys(message,sellingNorm)))'''