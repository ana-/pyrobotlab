def startLeftArm():
  #Left Arm
  i01.startLeftArm(leftPort)
  i01.leftArm.shoulder.map(0,180,0,180)
  #i01.leftArm.shoulder.setMinMax(25,180)
  i01.leftArm.omoplate.map(10,70,10,70)
  #i01.leftArm.omoplate.setMinMax(10,75)
  i01.leftArm.rotate.map(46,180,46,180)
  #i01.leftArm.rotate.setMinMax(46,180)
  i01.leftArm.bicep.map(5,60,5,80)
  #i01.leftArm.bicep.setMinMax(10,80)
  i01.leftArm.shoulder.setRest(30)
  i01.leftArm.omoplate.setRest(10)
  i01.leftArm.rotate.setRest(90)
  i01.leftArm.bicep.setRest(10)
  i01.leftArm.shoulder.setVelocity(14)
  i01.leftArm.omoplate.setVelocity(15)
  i01.leftArm.rotate.setVelocity(18)
  i01.leftArm.bicep.setVelocity(26)
  i01.leftArm.shoulder.setMaxVelocity(14)
  i01.leftArm.omoplate.setMaxVelocity(15)
  i01.leftArm.rotate.setMaxVelocity(18)
  i01.leftArm.bicep.setMaxVelocity(26)
  i01.leftArm.rest()
