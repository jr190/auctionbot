"""
Ok so. I think we will need write up a bunch of objects for our items (based on criterion they inherit) and save them with the quantity, 
author, position (buy/sell), and repetition of message (a way to quantify desirability). 
We will also need a way to parse our messages in a way to find out what objects need to captured and what side of the trade they are on
I think if we used a dictionary where the keys are lists of words that are keywords and the items are the objects used for those keywords
Once we can organise and structure our data the rest will be easy

nightsister clothes
5 pieces
augments/enhancements
beast eggs
enzymes
resources
bls/plcs
schematics (backpacks, weapons, deeds, psg)
space loot
junk loot

"""
#WTS Full Set of Mandalorian Armor(10 pieces) 7600/5600   sockets
#Primus RIS 6.6/6.6/5.4 socketed except chest is Crit Chance, Pistol Crit, Pistol Damage (extra dmg, shirt included too) 4M
#Rebel Special Forces Chest plate [5000e/7000k/6000r] deconstructed, socketed 8M

"""
Capped Primus -
   - Mandalorian Armor (This is the way)
   - Composite & Padded suits w/mod 
   - R.I.S suits w/mod
   - Bounty Hunter Armor w/mod
Capped Unlayered Armor 
   - Padded, Composite,  & 3 Marauder types
"""


#WTS,LTS,WTB,LTB

#   - DC15 Carbine Schem 10m
#Elite Tusken Rifle Schematic - 16M

class Augment:
    def __init__(self,augment,weaponType,value):
        self.augment = augment #health,action,crit
        self.weaponType = weaponType #ranged,melee
        self.value = value

class Armor:
    def __init__(self,armorType,kineticProtection,energyProtection,armorDescription,builtInMod,isSchematic):
        self.armorType = armorType
        self.kineticProtection = kineticProtection
        self.energyProtection = energyProtection
        self.armorDescription = armorDescription
        self.builtInMod = builtInMod
        self.isSchematic = isSchematic

class Weapon(Augment):
    def __init__(self,baseWeaponType,weaponCategory,weaponDPS,weaponElement,builtInMod,isSchematic,weaponDescription):
        self.baseWeaponType = baseWeaponType
        self.weaponCategory = weaponCategory
        self.weaponDPS = weaponDPS
        self.weaponElement = weaponElement
        self.builtInMod = builtInMod
        self.isSchematic = isSchematic
        self.weaponDescription = weaponDescription

class Beast:
    def __init__(self,beastType,points,beastDescription,isDNA):
        self.beastType = beastType
        self.points = points
        self.beastDescription = beastDescription
        self.isDNA = isDNA

class Jewelry:
    def __init__(self,setType,jewelryType,isSet):
        self.setType = setType
        self.jewelryType = jewelryType
        self.isSet = isSet