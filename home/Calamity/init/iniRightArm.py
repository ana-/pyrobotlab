def startRightArm():
  #Right Arm
  i01.startRightArm(rightPort)
  i01.rightArm.shoulder.map(0,180,0,180)
  #i01.rightArm.shoulder.setMinMax(0,180)
  i01.rightArm.omoplate.map(10,70,10,70)
  #i01.rightArm.rotate.setMinMax(46,160)
  i01.rightArm.rotate.map(46,160,46,160)
  #i01.rightArm.omoplate.setMinMax(10,70)
  i01.rightArm.bicep.map(5,60,5,80)
  #i01.rightArm.bicep.setMinMax(5,80)
  i01.rightArm.shoulder.setRest(20)
  i01.rightArm.omoplate.setRest(10)
  i01.rightArm.rotate.setRest(90)
  i01.rightArm.bicep.setRest(10)
  i01.rightArm.shoulder.setVelocity(14)
  i01.rightArm.omoplate.setVelocity(15)
  i01.rightArm.rotate.setVelocity(18)
  i01.rightArm.bicep.setVelocity(26)
  i01.rightArm.shoulder.setMaxVelocity(14)
  i01.rightArm.omoplate.setMaxVelocity(15)
  i01.rightArm.rotate.setMaxVelocity(18)
  i01.rightArm.bicep.setMaxVelocity(26)
  i01.rightArm.rest()
