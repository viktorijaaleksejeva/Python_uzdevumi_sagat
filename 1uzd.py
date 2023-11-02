"""Uzrakstiet programmu definējot klasi,lai veselu skaitli pārveidotu par romiešu ciparu.
1) Kas ir klase?
Klase sastāv no konstruktora/destruktora un metodēm
metodes - klases iekšējās funkcijas
2)kadas datu strukturas es zinu ? - 0
  List, array (masīvs)
  dict (dictionary- vardnica) ...{} otrs - dict()
3) Kas ir vārdnīca?
-datu struktūra - tabula ar 2 kolonnām - svarīga ir atslēga un tās vērtība

"""
class AAA:
    def __init__(self):
        self.roma_sk={
            1: 'I',
            4: 'IV',
            5: 'V',
            9: 'IX',
            10: 'X',
            40: 'XL',
            50: 'L',
            90: 'XC',
            100: 'C',
            400: 'CD',
            500: 'D',
            900: 'CM',
            1000: 'M'
        }
    def to_roman(self, num):
        result = ""
        for value, numeral in sorted(self.roma_sk.items(), key=lambda x: x[0], reverse=True):
            while num >= value:
                result += numeral
                num -= value
        return result

#piemērs
skaitlis=2023
# definējam objektu
kk=AAA()
#jaunajam objektam jāizsauc klases metode (iekšējā funkcija)
romieshu=kk.to_roman(skaitlis)
#noformēt izdruku
print(f"{skaitlis} ar romiešu cipariem ir {romieshu}.")