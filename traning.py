import random as r

def son_top(x=10):
    print("Keling o'ylagan sonni topish o'ynaymiz! ")
    sonlar = r.sample(range(1, x), 1)
    numb = int(sonlar[0])
    son = int(input(f"1 dan {x} gacha son o'yladim. Topa olasizmi: "))
    y = 0
    while True:
        y += 1
        if numb == son:
            print(f"Topdingiz! {sonlar[0]} sonini o'ylagandim. {y} ta urinish bilan topdingiz. Tabrikliyman!!")
            break
        elif numb > son:
            print("Men o'ylagan son kattaroq.")
        elif numb < son:
            print("Men o'ylagan son kichikroq.")
        son = int(input("Yana harakat qiling: "))


    return y

# son_top(10)

# ----------------------------------------------------------


def son_oyla(x=10):
    print(f"1 dan {x} gacha son o'ylang. Men topishga harakat qilaman.")
    input("Son o'ylagan bo'lsangiz istalgan tugmani bosing.")
    
    past = 1
    yuqori = x
    q = 0
    
    while True:
        q += 1
        bot = (past + yuqori) // 2  # O'rtacha qiymatni topish
        javob = input(f"Siz {bot} sonini o'yladingiz: to'g'ri (T), men o'ylagan son bundan kattaroq (+), yoki kichikroq (-)?? ").lower()
        
        if javob == 't':
            print(f"Soningizni {q} ta taxmin bilan topdim!")
            break
        elif javob == '+':
            past = bot + 1  # Pastki chegarani oshiramiz
        elif javob == '-':
            yuqori = bot - 1  # Yuqori chegarani pasaytiramiz
        else:
            print("Faqat 'T', '+' yoki '-' javoblarini kiriting!")

    return q
# son_oyla(10)



def play(x=10):
    yana = True
    while yana:
        taxminlar = son_top(x)
        taxminlar2 = son_oyla(x)
        if taxminlar > taxminlar2:
            print("Men yutdim")
        elif taxminlar < taxminlar2:
            print("Siz yutdingiz")
        else :
            print("Durrang")

        yana = input("Yana o'ynaymizmi? ha(1)/yo'q(0): ")

play()