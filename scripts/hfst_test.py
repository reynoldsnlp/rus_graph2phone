from pathlib import Path
import sys
import udar
import hfst
import csv
import re

def get_fst(start_rule, end_rule, *args):
    src = Path('reflexive.twolc')
    tmp = Path('g2p_test_from_py.tmp.hfst')
    hfst.compile_twolc_file(src.name, tmp.name,
                                resolve_left_conflicts=True)
    print('Preparing rule transducers for composition...', file=sys.stderr)
    rule_fsts_stream = hfst.HfstInputStream(tmp.name)

    rule_numbers = set()
    rule_numbers.add(0)
    for i in range(start_rule, end_rule + 1):
        rule_numbers.add(i)
    if (len(args) > 0):
        for i in range(args[0], args[1]+1):
            rule_numbers.add(i)

    rule_fsts = []
    for index, rule in enumerate(rule_fsts_stream):
        if index in rule_numbers:
            rule_fsts.append(rule)

    print('Creating universal language FST...', file=sys.stderr)
    output = hfst.regex('?* ;')
    print('Compose-intersecting rules with universal FST...',
          file=sys.stderr)
    output.compose_intersect(rule_fsts)
    print('Optimizing for fast lookup...', file=sys.stderr)
    #output.lookup_optimize()
    return output


def test(text, truth, start_rule, end_rule, *args):
    fst = get_fst(start_rule, end_rule, *args);
    analyzer = udar.Udar('analyzer')
    print('Processing test words...', file=sys.stderr)
    for index, inword in enumerate(text):  # for inword, output in words:
        token = analyzer.lookup(inword)
        if 'Gen' in token:
            inword = inword + "G"
        if 'Pl3' in token:
            inword = inword + "P"
        if 'Loc' in token:
            inword = inword + "L"
        if 'Dat' in token:
            inword = inword + "D"
        if 'Ins' in token:
            inword = inword + "I"
        if inword.endswith("я") or inword.endswith("Я"):
            inword = inword + "Y"
        if inword.endswith("ясь") or inword.endswith("ЯСЬ"):
            inword = inword +"S"
        outputs = fst.lookup(inword)
        output = [w for w, wt in outputs][0]
        if (output != truth[index]):
            print("\n" + inword + " => " + output + " != " + truth[index])
        else:
            print('.', end='', flush=True, file=sys.stderr)


def test_words():
    datafile = open('test.csv', 'r')
    datareader = csv.reader(datafile, delimiter=',')
    text = []
    truth = []
    for row in datareader:
        text.append(row[0])
        truth.append(row[1])
    start_rule = 0
    end_rule = 18
    test(text, truth, start_rule, end_rule)

def test_softness():
    text =  ["ле́т", "зима́",  "я́рус", "све́т",  "питьё",  "бле́дный",  "включа́ть",  "где́",  "гря́зный",  "сле́дующий"]
    truth = ["лэ́т", "з'има́", "а́рус", "св'э́т", "п'ит'о́", "бл'э́дный", "вкл'уча́т'", "гд'э́", "гр'а́зный", "сл'э́дуущий"]
    start_rule = 0
    end_rule = 0
    test(text, truth, start_rule, end_rule)

def test_ee_kratkoye():
    text =  ["сле́дующий",   "чле́н",  "чьи́",  "извиня́юсь",    "я́рус",  "чуде́сный",  "мо́ю",  "я́щик",   "питьё",   "съе́л"]
    truth = ["сл'э́дуйущий", "чл'э́н", "ч'йи́", "изв'ин'а́йус'", "йа́рус", "чуд'э́сный", "мо́йу", "йа́щ'ик", "п'ит'йо", "сйэ́л"]
    start_rule = 1
    end_rule = 4
    test(text, truth, start_rule, end_rule)

def test_yeri():
    text =  ["живо́т", "щи́",  "сыгра́ть", "мы́шь","ци́кл", "лы́жи", "де́ньги",   "дружи́ть", "чи́щу",  "бо́льший"]
    truth = ["жыво́т", "щ'и́", "сыгра́т'", "мы́ш", "цы́кл", "лы́жы", "д'э́н'г'и", "дружы́т'", "ч'и́щу", "бо́л'шый"]
    start_rule = 5
    end_rule = 5
    test(text, truth, start_rule, end_rule)

def test_akanje():
    text =  ["берегово́й",   "молокосо́с", "острова́", "ка́федра",  "го́лову", "обжо́ра", "ско́вороды", "го́родом", "магази́н",  "грома́дность"]
    truth = ["б'ер'егʌво́й", "мълъкʌсо́с", "ʌстрʌва́", "ка́ф'едръ", "го́лъву", "ʌбжо́ръ", "ско́въръды", "го́ръдъм", "мъгʌз'и́н", "грʌма́днъс'т'"]
    start_rule = 6
    end_rule = 7
    test(text, truth, start_rule, end_rule)

def test_tense_ya_ye():
    text =  ["проче́сть",   "сове́тница",    "две́сти",    "боле́л",  "боле́ли",   "де́ле",   "све́тит",   "ча́сть",   "вычисля́ть",    "я́щик"]
    truth = ["проч'э̂с'т'", "сов'э̂т'н'ица", "дв'э̂с'т'и", "бол'э́л", "бол'э̂л'и", "д'э̂л'е", "св'э̂т'ит", "ч'а̂с'т'", "выч'ис'л'а̂т'", "йа̂щ'ик"]
    start_rule = 8
    end_rule = 8
    test(text, truth, start_rule, end_rule, 16, 18)
    # Depends on Softness Assimilation

def test_ikanje():
    text =  ["язы́к",  "ерунда́",  "еди́нственно",    "чепуха́",  "телефо́н",   "берегово́й",   "весна́",  "серебро́",   "о́череди",    "пятьдеся́т"]
    truth = ["йизы́к", "йьрунда́", "йид'и́нств'ьнно", "ч'ьпуха́", "т'ьл'ифо́н", "б'ьр'ьгово́й", "в'исна́", "с'ьр'ибро́", "о́ч'ьр'ьд'и", "п'ьт'д'ис'а́т"]
    start_rule = 9
    end_rule = 10
    test(text, truth, start_rule, end_rule, 1, 4)
    # Depends on EeKratkoye

def test_ykanje():
    text =  ["уценена́",  "жесто́кий",  "шелуха́", "шесто́й", "ше́рсть", "це́лый", "же́ртва", "шевели́ться",   "целико́м",  "кольцево́й"]
    truth = ["уцън'ена́", "жысто́к'ий", "шълуха́", "шысто́й", "шэ́рст'", "цэ́лый", "жэ́ртва", "шъв'ел'и́тс'я", "цъл'ико́м", "кол'цыво́й"]
    start_rule = 11
    end_rule = 12
    test(text, truth, start_rule, end_rule)

def test_final_devoicing():
    text =  ["пло́д", "гла́з", "зу́б", "но́ж", "дру́г", "сто́рож", "отре́жь",  "ся́дь",  "до́м", "ста́р"]
    truth = ["пло́т", "гла́с", "зу́п", "но́ш", "дру́к", "сто́рош", "от'р'э́ш", "с'а́т'", "до́м", "ста́р"]
    start_rule = 13
    end_rule = 13
    test(text, truth, start_rule, end_rule)

def test_cluster_unvoiced_assimilation():
    text =  ["тру́бка", "ло́дка", "вку́с", "коро́бка", "ска́зка", "второ́й"]
    truth = ["тру́пкъ", "ло́ткъ", "фку́с", "кʌро́пкъ", "ска́скъ", "фтʌро́й"]
    start_rule = 14
    end_rule = 14
    test(text, truth, start_rule, end_rule)

def test_cluster_voice_assimilation():
    text =  ["про́сьба", "вокза́л", "сгоре́л",  "све́т",  "сво́лочь", "сде́лал"]
    truth = ["про́з'бъ", "вʌгза́л", "згʌр'э́л", "св'э́т", "сво́лоч",  "зд'э́лал"]
    start_rule = 15
    end_rule = 15
    test(text, truth, start_rule, end_rule)

def test_softness_assimilation():
    text =  ["ча́сть",   "вперёд",    "две́рь",  "вме́сте",     "ски́дка",  "клева́ть",  "твёрдая",  "присе́сть",    "проче́сть",   "сове́тница"]
    truth = ["ч'а́с'т'", "в'п'ер'о́д", "дв'э́р'", "в'м'э́с'т'е", "ск'и́тка", "кл'ева́т'", "тв'о́рдая", "пр'ис'э́с'т'", "проч'э́с'т'", "сов'э́т'н'ица"]
    start_rule = 16
    end_rule = 18
    test(text, truth, start_rule, end_rule)


def test_all_rules():
    test_softness()
    test_ee_kratkoye()
    test_yeri()
    test_akanje()
    test_tense_ya_ye()
    test_ikanje()
    test_ykanje()
    test_final_devoicing()
    test_cluster_unvoiced_assimilation()
    test_cluster_voice_assimilation()
    test_softness_assimilation()

if __name__ == '__main__':
    switcher = {
        "words": test_words,
        "all_rules": test_all_rules,
        "softness": test_softness,
        "ee_kratkoye": test_ee_kratkoye,
        "yeri": test_yeri,
        "akanje": test_akanje,
        "tense_ya_ye": test_tense_ya_ye,
        "ikanje": test_ikanje,
        "ykanje": test_ykanje,
        "final_devoicing": test_final_devoicing,
        "cluster_unvoiced_assimilation": test_cluster_unvoiced_assimilation,
        "cluster_voice_assimilation": test_cluster_voice_assimilation,
        "softness_assimilation": test_softness_assimilation
    }

    arg = "words"
    if len(sys.argv) > 1:
        arg = sys.argv[1]

    func = switcher.get(arg)
    func()
