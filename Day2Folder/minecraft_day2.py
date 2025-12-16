# AT THE END OF LESSON, COPY YOUR CODE FROM MINECRAFT HERE.
# THIS IS SO THAT YOU HAVE A RECORD OF YOUR CODE FROM MINECRAFT CODE BUILDER
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



#move forward
def foward(count):
    agent.move(FORWARD, count)
player.on_chat("fw", foward)
#move up
def o(count):
    agent.move(UP, count)
player.on_chat("up", o)
#move down
def down(count):
    agent.move(DOWN, count)
player.on_chat("down", down)
#playground forwards
def on_chat():
    agent.move(FORWARD, 4)
    agent.turn(TurnDirection.LEFT)
    agent.move(FORWARD, 4)
    agent.turn(TurnDirection.RIGHT)
    agent.move(FORWARD, 3)
    agent.move(UP, 1)
    agent.move(FORWARD, 1)
    agent.move(UP, 1)
    agent.move(FORWARD, 1)
    agent.move(UP, 1)
    agent.move(FORWARD, 3)
    agent.move(DOWN, 1)
    agent.move(FORWARD, 1)
    agent.move(DOWN, 1)
    agent.move(FORWARD, 1)
    agent.move(DOWN, 1)
player.on_chat('obby1', on_chat)

#playground backwards
def on_chat2():
    agent.move(UP, 1)
    agent.move(FORWARD, 1)
    agent.move(UP, 1)
    agent.move(FORWARD, 1)
    agent.move(UP, 1)
    agent.move(FORWARD, 3)
    agent.move(DOWN, 1)
    agent.move(FORWARD, 1)
    agent.move(DOWN, 1)
    agent.move(FORWARD, 1)
    agent.move(DOWN, 1)
    agent.move(FORWARD, 4)
    agent.turn(TurnDirection.LEFT)
    agent.move(FORWARD, 4)
    agent.turn(TurnDirection.RIGHT)
    agent.move(FORWARD, 4)
player.on_chat("ob2", on_chat2)




def on_chat3(count):
    agent.destroy(FORWARD)
    agent.move(FORWARD, 1)
    for i in range(count):
     agent.destroy(UP)
     agent.collect_all()
     agent.move(UP, 1)
agent.teleport_to_player()
player.on_chat("chop", on_chat3)
