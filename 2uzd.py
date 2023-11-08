"""
Iegūt ziņas, izmantojot RSS plūsmu no google 
Kas ir RSS?  -formāts jeb sistēma kas automātiksi izplata jaunumus, rakstus, informāciju.
IEt kopāar XML valodu - priekš tīmekļim kas atvieglo atjauno ??
"""
import feedparser

#1) Norādīt RSS plūmas URL(vietrādis), kas satur google.lv ziņas

rss_url='https://news.google.com/rss?hl=lv&gl=LV&ceid=LV:lv'
#2)Lejuplādēju un analizēju RSS plūšmu
feed=feedparser.parse(rss_url)
#3) parādīšana
for entry in feed.entries:
    print("Virsraksts", entry.title)
    print("Saite", entry.link)
    print("/n")