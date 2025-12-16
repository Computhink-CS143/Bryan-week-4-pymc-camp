# AT THE END OF LESSON, COPY YOUR CODE FROM MINECRAFT HERE.
# THIS IS SO THAT YOU HAVE A RECORD OF YOUR CODE FROM MINECRAFT CODE BUILDER
################# Function Section #############################
def addition(num1,num2):
    player.say(num1+num2)


def multiply(num,num8):
    player.say(num*num8)




addition(23,34)





def teleport():
    agent.teleport_to_player()
player.on_chat("come", teleport)



#tr:turn right
def tr():
    agent.turn(TurnDirection.RIGHT)
player.on_chat("tr", tr)

#tl:turn left
def tl():
    agent.turn(TurnDirection.LEFT)
player.on_chat("tl",tl)def addition(num1,num2):
    player.say(num1+num2)


def multiply(num,num8):
    player.say(num*num8)




addition(23,34)





def teleport():
    agent.teleport_to_player()
player.on_chat("come", teleport)



#tr:turn right
def tr():
    agent.turn(TurnDirection.RIGHT)
player.on_chat("tr", tr)

#tl:turn left
def tl():
    agent.turn(TurnDirection.LEFT)
player.on_chat("tl",tl)

################## On Chat Commands Section #####################
