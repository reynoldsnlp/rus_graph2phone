

def test(text, truth, startRule, endRule):
    pass

#### All rules are dependent upon Softness (and not really EeKratkoye)
def testAllRules():
    pass


def testSoftness():
    text =  ["ле́т", "зима́",  "я́рус", "све́т",  "питьё",  "бле́дный",  "включа́ть",  "где́",  "гря́зный",  "сле́дующий"]
    truth = ["лэ́т", "з'има́", "а́рус", "св'э́т", "п'ит'о́", "бл'э́дный", "вкл'уча́т'", "гд'э́", "гр'а́зный", "сл'э́дуущий"]
    startRule = 0
    endRule = 0

def testEeKratkoye():
    text =  ["сле́дующий",   "чле́н",  "чьи́",  "извиня́юсь",    "я́рус",  "чуде́сный",  "мо́ю",  "я́щик",   "питьё",   "съе́л"]
    truth = ["сл'э́дуйущий", "чл'э́н", "ч'йи́", "изв'ин'а́йус'", "йа́рус", "чуд'э́сный", "мо́йу", "йа́щ'ик", "п'ит'йо", "сйэ́л"]
    startRule = 1
    endRule = 4

def testYeri():
    живо́т,жыво́т
    щи́,щ'и́
    сыгра́ть,сыгра́т'
    мы́шь,мы́ш
    ци́кл,цы́кл
    лы́жи,лы́жы
    де́ньги,д'э̂н'г'и
    дружи́ть,дружы́т'
    чи́щу,ч'и́щу
    бо́льший,бо́л'шый
    text = ["живо́т",  "щи́","сыгра́ть","мы́шь","ци́кл","лы́жи","де́ньги","дружи́ть","чи́щу","бо́льший"]
    truth = ["жыво́т", "щ'и́", "сыгра́т'", "мы́ш", "цы́кл", "лы́жы", "д'э́н'г'и", "дружы́т'", "ч'и́щу", "бо́л'шый"]
    startRule = 5
    endRule = 5

def testAkanje():
    text = ["","","","","","","","","",""]
    truth = ["","","","","","","","","",""]
    startRule = 6
    endRule = 7

def testTenseYaYe():
    text = ["","","","","","","","","",""]
    truth = ["","","","","","","","","",""]
    startRule = 8
    endRule = 8

def testIkanje():
    text = ["","","","","","","","","",""]
    truth = ["","","","","","","","","",""]
    startRule = 9
    endRule = 10

def testYkanje():
    text = ["","","","","","","","","",""]
    truth = ["","","","","","","","","",""]
    startRule = 11
    endRule = 12

def testFinalDevoicing():
    text = ["","","","","","","","","",""]
    truth = ["","","","","","","","","",""]
    startRule = 13
    endRule = 13

def testClusterUnvoicedAssimilation():
    text = ["","","","","","","","","",""]
    truth = ["","","","","","","","","",""]
    startRule = 14
    endRule = 14

def testClusterVoiceAssimilation():
    text = ["","","","","","","","","",""]
    truth = ["","","","","","","","","",""]
    startRule = 15
    endRule = 15

def testSoftnessAssimilation():
    text = ["","","","","","","","","",""]
    truth = ["","","","","","","","","",""]
    startRule = 16
    endRule = 18
