def startRightHand():
  ##############
  i01.startRightHand(rightPort)
  i01.rightHand.thumb.setMinMax(0,115)
  i01.rightHand.index.setMinMax(35,130)
  i01.rightHand.majeure.setMinMax(35,130)
  i01.rightHand.ringFinger.setMinMax(35,130)
  i01.rightHand.pinky.setMinMax(35,130)
  i01.rightHand.wrist.map(90,90,90,90)
  #i01.rightHand.thumb.map(0,180,0,115)
  #i01.rightHand.index.map(0,180,35,130)
  #i01.rightHand.majeure.map(0,180,35,130)
  #i01.rightHand.ringFinger.map(0,180,35,130)
  #i01.rightHand.pinky.map(0,180,35,130)
  i01.rightHand.thumb.setVelocity(250)
  i01.rightHand.index.setVelocity(250)
  i01.rightHand.majeure.setVelocity(250)
  i01.rightHand.ringFinger.setVelocity(250)
  i01.rightHand.pinky.setVelocity(250)
  i01.rightHand.wrist.setVelocity(250)
  i01.rightHand.thumb.setMaxVelocity(250)
  i01.rightHand.index.setMaxVelocity(250)
  i01.rightHand.majeure.setMaxVelocity(250)
  i01.rightHand.ringFinger.setMaxVelocity(250)
  i01.rightHand.pinky.setMaxVelocity(250)
  i01.rightHand.wrist.setMaxVelocity(250)
  i01.rightHand.thumb.setRest(10)
  i01.rightHand.index.setRest(40)
  i01.rightHand.majeure.setRest(40)
  i01.rightHand.ringFinger.setRest(40)
  i01.rightHand.pinky.setRest(40)
  i01.rightHand.wrist.setRest(90)
  i01.rightHand.rest()
