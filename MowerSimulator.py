'''
Emmet Evans - IS 303 - A01
This program will be a simple calculator to determine how many hours need to be spent in order to reach a desired level in lawnmower simulator

Inputs:
Current lawnmower level (int)
Target lawnmower level (int)
XP per session (int) (fixed input)
Model of lawnmower currently owned in-game (int)

Processes:
Target level - Current level = Levels needed
Levels needed / 100 = XP needed
XP per session * lawnmower type multiplier = XPplus
XP needed / XPplus = number of session needed

Outputs:
Print the lawnmower type, sessions needed, and target level in one message
'''

#Inputs
Clevel = int(input("\nWhat is your current level? "))
Tlevel = int(input("What level would you like to reach? "))
XPsession = 25
MowerModel = int(input("Which of the 4 mower models do you have? "))

#Processing
Nlevel = Tlevel - Clevel
XPneed = Nlevel * 100
XPplus = XPsession * MowerModel
FinalSession = XPneed / XPplus

#Output
print(f"If you have a model {MowerModel} lawnmower and want to reach level {Tlevel}, you will need to do {FinalSession:.1f} more gaming sessions.\n")