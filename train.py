alf = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz;:»)("–…][-“”"1234567890&#«'




co = open('корпус/база данных\база данных 1.txt')
co_1 = open('корпус/база данных\HP4RUS.txt')
co_2 = open('корпус/база данных\HP2RUS.txt')
co_3 = open('корпус/база данных\HP3RUS.txt')
co_4 = open('корпус/база данных\HP1RUS.txt')
co_5 = open('корпус/база данных\базаданных2.txt')
co_6 = open('корпус/база данных\базаданных3.txt')
co_7 = open('корпус/база данных\три товарища.txt')
co_8 = open('корпус/база данных\чёрный обелиск.txt')
co_9 = open('корпус/база данных\портрет.txt')
co_10 = open('корпус/база данных\оруэл.txt')
co_11 = open('корпус/база данных\хроники.txt')
co_12 = open('корпус/база данных\БББББ.txt')
co_13 = open('корпус/база данных\emelian.txt')
co_14 = open('корпус/база данных\pugach.txt')
co_15 = open('корпус/база данных\война.txt')
co_16 = open('корпус/база данных\борьба.txt')

co = co.read()
co_1 = co_1.read()
co_2 = co_2.read()
co_3 = co_3.read()
co_4 = co_4.read()
co_5 = co_5.read()
co_6 = co_6.read()
co_7 = co_7.read()
co_8 = co_8.read()
co_9 = co_9.read()
co_10 = co_10.read()
co_11 = co_11.read()
co_12 = co_12.read()
co_13 = co_13.read()
co_14 = co_14.read()
co_15 = co_15.read()
co_16 = co_16.read()

co = co.lower()
co_1 = co_1.lower()
co_2 = co_2.lower()
co_3 = co_3.lower()
co_4 = co_4.lower()
co_5 = co_5.lower()
co_6 = co_6.lower()
co_7 = co_7.lower()
co_8 = co_8.lower()
co_9 = co_9.lower()
co_10 = co_10.lower()
co_11 = co_11.lower()
co_12 = co_12.lower()
co_13 = co_13.lower()
co_14 = co_14.lower()
co_15 = co_15.lower()
co_16 = co_16.lower()


corpus = co_15 + co + co_1 + co_2 + co_3 + co_4 + co_5 + co_6 + co_7 + co_8 + co_9 + co_10 + co_11 + co_12 + co_13 + co_14 + co_15





for i in alf:
    corpus = corpus.replace(i, '')


corpus = corpus.replace('  ', ' ')
corpus = corpus.replace('   ', ' ')


cp = open('корпус/corpus.txt', 'w')
cp.write(corpus)



corpus = corpus.split()
bigram = []
trigram = []
four_gram = []
for i in range(len(corpus) - 3):
    bigram += [(corpus[i], corpus[i+1])]
    trigram += [(corpus[i], corpus[i+1], corpus[i+2])]
    four_gram += [(corpus[i], corpus[i+1], corpus[i+2], corpus[i+3])]

bg = open('n-grams/bigrams.txt', 'w')
tg = open('n-grams/trigrams.txt', 'w')
fg = open('n-grams/four_grams.txt', 'w')

bg.write(str(bigram))
tg.write(str(trigram))
fg.write(str(four_gram))
