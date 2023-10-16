class player:

  def play(self):
    print("the player is playing cricket")


class batsman(player):

  def play(self):
    print("the player is playing batting")


class bowler(player):

  def play(self):
    print("the player is playing bowling")


batsman = batsman()
bowler = bowler()
batsman.play()
bowler.play()
