import numpy as np



#-----------------------------------------------------------------------------------

corpus = open('корпус/corpus.txt', 'r')
corpus = corpus.read()



corpus = corpus.split()


bigram = []
trigram = []
four_gram = []
for i in range(len(corpus) - 3):
    bigram += [(corpus[i], corpus[i+1])]
    trigram += [(corpus[i], corpus[i+1], corpus[i+2])]
    four_gram += [(corpus[i], corpus[i+1], corpus[i+2], corpus[i+3])]


#----------------------------------------------------------------------------------- 

class Model(object):

    
    def fourgram_next(self, four_gram):
        

        four_next = []
        

        four = input_[-3:]
        four = str(four[0] + ' ' + four[1] + ' ' + four[2])

        for g in four_gram:
            if g[0] + ' ' + g[1] + ' ' + g[2] == four:
                four_next += [g[3]]
        return four_next


    def trigram_next(self, trigram):

        tri_next = []

        tri = input_[-2:]
        tri = str(tri[0] + ' ' + tri[1])
        for k in trigram:
            if k[0] + ' ' + k[1] == tri:
                tri_next += [k[2]]
        return tri_next

        


    def bigram_next(self, bigram):
        
        bi_next = []

        bi = input_[-1:]
        bi = str(bi[0])
        for i in bigram:
            if i[0] == bi:
                bi_next += [i[1]]
        return bi_next
       

    def final_word(self, bi_next, tri_next, four_next):

        final_bi = []
        final_tri = []
        final_four = []
        
        if bi_next != []:
            final_bi = np.random.choice(bi_next, 1)
        
        if tri_next != []:
            final_tri = np.random.choice(tri_next, 1)

        if four_next != []:
            final_four = np.random.choice(four_next, 1)
    
        if len(final_four) == 1:
            input_.append(final_four[0])
            
        elif len(final_tri) == 1:
            input_.append(final_tri[0])
            
        elif len(final_bi) == 1:
            input_.append(final_bi[0])




#-----------------------------------------------------------------------------------        

input_ = input('Введите начальное выражение: ', )
how_many_words = int(input('Сколько слов вы хотите сгенерировать? ', ))



input_ = input_.split()
if corpus.count(input_[-1]) == 0:
    print('Извините, данного слова нет в базе данных.')
else:
    n = 0
    Model = Model()
    while n < how_many_words:
        if len(list(input_)) > 2:
            Model.final_word(Model.bigram_next(bigram), Model.trigram_next(trigram), Model.fourgram_next(four_gram))
        elif len(list(input_)) == 2:
            Model.final_word(Model.bigram_next(bigram), Model.trigram_next(trigram), [])
        else:
            Model.final_word(Model.bigram_next(bigram), [], [])
        n += 1
    print('Ваш сгенерировавшийся текст:')
    print(' '.join(input_))




































