'''
Calculates and keeps the Emotionvalue
'''
import math
import random
from threading import Timer


class EmotionContainer:

    mass = 0.0
    sxlast,  sylast,  sxt,  syt,  sdom,  sdomlast = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0
    vxlast,  vylast,  vxt,  vyt,  vdom,  vdomlast = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0
    axlast,  aylast,  axt,  ayt,  adom,  adomlast = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0
    dt = 0.0
    z = 0.0
    xSignChange,  ySignChange = 0, 0
    xSign,  ySign = 0, 0
    xTens,  yTens,  slope,  xReg,  yReg = 0, 0, 0, 0, 0
    Fx,  Fy,  boredom = 0.0, 0.0, 0.0

    def __init__(self):
        self.mass = 1000
        self.sxlast,  self.sylast,  self.sxt,  self.syt = 0.0, 0.0, 0.0, 0.0,
        self.sdom,  self.sdomlast = 100.0, 100.0
        self.vxlast,  self.vylast,  self.vxt,  self.vyt,  self.vdom,  self.vdomlast = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0
        self.axlast,  self.aylast,  self.axt,  self.ayt,  self.adom,  self.adomlast = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0
        self.dt = 0.1
        self.z = 0.0
        self.xSignChange = 0.0
        self.ySignChange = 0.0
        self.xSign = self.ySign = 0.0
        self.xTens = 50.0
        self.yTens = 10.0
        self.xReg = 1.0
        self.yReg = 1.0
        self.slope = 500.0
        self.boredom = 10.0

    def calculate(self):
        self.Fx = -self.xTens * self.sxlast
        self.Fy = -self.yTens * self.sylast
        self.axt = self.Fx / self.mass
        self.vxt = self.axt * self.dt + self.vxlast
        self.sxt = self.vxt * self.dt + self.sxlast

        if (self.sxt > 0 and self.sxlast < 0) or (self.sxt < 0 and self.sxlast > 0):
            self.sxt, self.sxlast = 0, 0
            self.vxlast = 0
            self.axlast = 0
        else:
            self.vxlast = self.vxt
            self.axlast = self.axt
            self.sxlast = self.sxt

        self.ayt = self.Fy / self.mass
        self.vyt = self.ayt * self.dt + self.vylast
        self.syt = self.vyt * self.dt + self.sylast
        self.syt += self.sxt * (self.slope / 100) / self.mass

        if (self.syt > 0 and self.sylast < 0) or (self.syt < 0 and self.sylast > 0):
            self.syt = self.sylast = 0.
            self.vylast = 0.
            self.aylast = 0.

        else:
            self.vylast = self.vyt
            self.aylast = self.ayt
            self.sylast = self.syt

        if self.sxt > 100:
            self.sxt = 100

        if self.syt > 100:
            self.syt = 100

        if self.sxt < -100:
            self.sxt = -100

        if self.syt < -100:
            self.syt = -100.

        if self.sxt < self.xReg and self.syt < self.yReg and self.sxt > -self.xReg and self.syt > -self.yReg:
            if self.z > -100:
                self.z -= self.boredom / 1000

        else:
            self.z = 0.

        #log.debug('x %s) (y %s) (z %s)', self.sxt, self.syt, self.z)

    def get_dt(self):
        return self.dt

    def emoimpulse(self, i):
        self.axt,  self.axlast,  self.vxt,  self.vxlast,  self.ayt,  self.aylast,  self.vyt,  self.vylast = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0
        self.sxlast += i

        if self.sxlast > 100:
            self.sxlast = 100

        if self.sxlast < -100:
            self.sxlast = -100

        self.sxt += i

        if self.sxt > 100:
            self.sxt = 100

        if self.sxt < -100:
            self.sxt = -100

    def get_emotion_list(self):
        emotionList = [self.sxt, self.syt, self.z, self.sdom]
        #log.debug('emotionlist: %s', emotionList)
        return emotionList

    def set_dominance(self, value):
        self.sdom = value


class EmotionConverter:
    emoIndex = 0
    emoDistance, outerRadius, innerRadius = 0.0, 0.0, 0.0
    tempList, stringConvertList, actualStringConvertElement = [], [], []
    v, temp = [0, 0, 0], [0, 0, 0]
    emoX, moodY, boredomZ, dominance, tempDistance = 0.0, 0.0, 0.0, 0.0, 0.0,
    s = ''

    def __init__(self):
        self.outerRadius = 0.8
        self.innerRadius = 0.4
        self.emoIndex = -1.
        self.s = "confused"
        self.actualStringConvertElement = ["relaxed", [0, 0, 1.0]]

        self.tempList = ["angry", [-0.8, 0.8, 1.0]]
        self.stringConvertList.append(self.tempList)

        self.tempList = ["fearful", [-0.8, 0.8, -1.0]]
        self.stringConvertList.append(self.tempList)

        self.tempList = ["annoyed", [-0.5, 0.0, 1.0]]
        self.stringConvertList.append(self.tempList)

        self.tempList = ["sad", [-0.5, 0.0, 1.0]]
        self.stringConvertList.append(self.tempList)

        self.tempList = ["joyful-d", [0.8, 0.8, 1.0]]
        self.stringConvertList.append(self.tempList)

        self.tempList = ["joyful-s", [0.8, 0.8, -1.0]]
        self.stringConvertList.append(self.tempList)

        self.tempList = ["relaxed-d", [0.0, 0.0, 1.0]]
        self.stringConvertList.append(self.tempList)

        self.tempList = ["sad-s", [-0.5, 0.0, -1.0]]
        self.stringConvertList.append(self.tempList)

        self.tempList = ["surprised", [0.1, 0.8, 1.0]]
        self.stringConvertList.append(self.tempList)

        self.tempList = ["startled", [0.1, 0.8, -1.0]]
        self.stringConvertList.append(self.tempList)

        self.tempList = ["bored", [0.0, -0.8, 1.0]]
        self.stringConvertList.append(self.tempList)

        self.tempList = ["depressed", [0.0, -0.8, -1.0]]
        self.stringConvertList.append(self.tempList)

        self.tempList = ["neutral", [0.0, 0.0, 0.0]]
        self.stringConvertList.append(self.tempList)

    '''
    receives a list with 4 elements and converts the values
    into a vector
    '''
    def convertToClassType(self, foreignData):
        v = [0, 0, 0]

        if len(foreignData) == 4:
            emoX = foreignData[0]
            moodY = foreignData[1]
            boredomZ = foreignData[2]
            dominance = foreignData[3]

            v[0] = ((emoX + moodY) / 200)
            v[1] = (abs(emoX / 100) - abs(boredomZ / 100))
            v[2] = dominance / 100
            #log.debug('convert to class type: %s', v)

        return v

    '''
    calculates the distances between the current vector and the emotion vectors.
    return the emotions with the smallest distance
    '''
    def getString(self, PADData):
        self.s ="neutral"
        self.actualStringConvertElement = ["neutral", [0, 0, 0]]
        self.emoDistance = 10.0

        #iterates through every declared emotion and subtracts it from the given vector
        for element in self.stringConvertList:
            self.temp[0] = PADData[0] - element[1][0]
            self.temp[1] = PADData[1] - element[1][1]
            self.temp[2] = PADData[2] - element[1][2]

            #calculates the length of the resulting vector
            self.tempDistance = math.sqrt(self.temp[0]**2+self.temp[1]**2+self.temp[2]**2)

            #if the new vector length is smaller than the last one, the new value is saved
            if self.tempDistance < self.emoDistance and self.tempDistance < self.outerRadius:
                self.actualStringConvertElement = element
                self.s = element[0]
                self.emoDistance = self.tempDistance

        return self.s

    #def EmotionLabel(self):

    '''
    return the current emotion list element
    '''
    def getActualStringConvertElement(self):
        return self.actualStringConvertElement


class EmotionalAgent:
    myEmotionContainer = EmotionContainer()
    myEmotionConverter = EmotionConverter()
    emoimp = 0

    def __init__(self):
        self.myEmotionContainer.calculate()
        self.calculate_emotions()
        #self.send_random_emoimpulse()
        #self.send_emoimpulse(75)

    def calculate_emotions(self):
        self.myEmotionContainer.calculate()
        t = Timer(0.4, self.calculate_emotions)
        t.start()

    def send_random_emoimpulse(self):
        self.emoimp = random.randint(26, 75) - 25
        self.myEmotionContainer.emoimpulse(self.emoimp)
        t = Timer(5.0, self.send_random_emoimpulse)
        t.start()

    def send_emoimpulse(self, impulse):
        self.myEmotionContainer.emoimpulse(impulse)

    def get_emotion_label(self):
        return self.myEmotionConverter.getString(
            self.myEmotionConverter.convertToClassType(
                self.myEmotionContainer.get_emotion_list()))
