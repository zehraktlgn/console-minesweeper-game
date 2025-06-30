#ZEHRA KUTLUGÜN
#22100011002
while True:
    boyut = int(input("Mayin tarlasinin bir kenar uzunlugunu giriniz"))
    a = (boyut * boyut) * (3 / 10)
    a=int(a)
    bitis = (boyut * boyut) * (7 / 10)
    bitis=int(bitis)
    puan = 0
    kontrol2 = 0
    import random
    z=0
    k=0
    f=0
    h=0
    sayac = 0
    s = 0
    mayinkonum = []
    kontrol = []
    sec = int(input("1-GİZLİ MOD "  
                    "2-ACIK MOD"))

    matris = [['? ' for i in range(boyut)] for i in range(boyut)]

    m = [[' ' for j in range(boyut)] for j in range(boyut)]

    while s <= a:
        x = random.randint(0, boyut - 1)
        y = random.randint(0, boyut - 1)
        s = s + 1
        mayinkonum = ([x, y])
        if [x, y] in mayinkonum:
            s = s - 1
            continue
        else:
            mayinkonum.append([x, y])
            m[x][y] = 'X'
        #print(mayinkonum)

    if sec==2:
        for i in range(boyut):
            print(m[i])
    if sec==1:
        for i in range(boyut):
            print(matris[i])
        while sec==1 or sec==2:
            satir = int(input("Kacinci satiri acacaksiniz?"))
            sutun = int(input("Kacinci sutunu acacaksiniz?"))
            satir = satir - 1
            sutun = sutun - 1
            b = ([satir, sutun])
            if b in kontrol:
                print("Ayni konumu girdiniz")
                continue
            if b not in kontrol:
                kontrol.append([satir, sutun])
            if m[satir][
                sutun] == ' ' and satir != 0 and satir != boyut - 1 and sutun != 0 and sutun != boyut - 1:  # ORTA
                sayac = 0
                puan = puan + 1
                if m[satir - 1][sutun] == 'X':
                    sayac = sayac + 1
                if m[satir + 1][sutun] == 'X':
                    sayac = sayac + 1
                if m[satir][sutun - 1] == 'X':
                    sayac = sayac + 1
                if m[satir][sutun + 1] == 'X':
                    sayac = sayac + 1
                if m[satir - 1][sutun - 1] == 'X':
                    sayac = sayac + 1
                if m[satir + 1][sutun - 1] == 'X':
                    sayac = sayac + 1
                if m[satir - 1][sutun + 1] == 'X':
                    sayac = sayac + 1
                if m[satir + 1][sutun + 1] == 'X':
                    sayac = sayac + 1
            elif satir == 0 and sutun == 0 and m[satir][sutun] == ' ':  # sol ust kose
                sayac = 0
                puan = puan + 1
                if m[satir + 1][sutun] == 'X':
                    sayac = sayac + 1
                if m[satir][sutun + 1] == 'X':
                    sayac = sayac + 1
                if m[satir + 1][sutun + 1] == 'X':
                    sayac = sayac + 1
            elif satir == 0 and sutun == boyut - 1 and m[satir][sutun] == ' ':  # sag ust kose
                sayac = 0
                puan = puan + 1
                if m[satir + 1][sutun] == 'X':
                    sayac = sayac + 1
                if m[satir][sutun - 1] == 'X':
                    sayac = sayac + 1
                if m[satir + 1][sutun - 1] == 'X':
                    sayac = sayac + 1
            elif satir == boyut - 1 and sutun == 0 and m[satir][sutun] == ' ':  # sol alt kose
                sayac = 0
                puan = puan + 1
                if m[satir - 1][sutun] == 'X':
                    sayac = sayac + 1
                if m[satir][sutun + 1] == 'X':
                    sayac = sayac + 1
                if m[satir - 1][sutun + 1] == 'X':
                    sayac = sayac + 1
            elif satir == boyut - 1 and sutun == boyut - 1 and m[satir][sutun] == ' ':  # sag alt kose
                sayac = 0
                puan = puan + 1
                if m[satir - 1][sutun] == 'X':
                    sayac = sayac + 1
                if m[satir][sutun - 1] == 'X':
                    sayac = sayac + 1
                if m[satir - 1][sutun - 1] == 'X':
                    sayac = sayac + 1
            elif satir != 0 and satir != boyut - 1 and sutun == 0 and m[satir][sutun] == ' ':  # sol kenar
                sayac = 0
                puan = puan + 1
                if m[satir - 1][sutun] == 'X':
                    sayac = sayac + 1
                if m[satir + 1][sutun] == 'X':
                    sayac = sayac + 1
                if m[satir][sutun + 1] == 'X':
                    sayac = sayac + 1
                if m[satir - 1][sutun + 1] == 'X':
                    sayac = sayac + 1
                if m[satir + 1][sutun + 1] == 'X':
                    sayac = sayac + 1
            elif satir != 0 and satir != boyut - 1 and sutun == boyut - 1 and m[satir][sutun] == ' ':  # sag kenar
                sayac = 0
                puan = puan + 1
                if m[satir - 1][sutun] == 'X':
                    sayac = sayac + 1
                if m[satir + 1][sutun] == 'X':
                    sayac = sayac + 1
                if m[satir][sutun - 1] == 'X':
                    sayac = sayac + 1
                if m[satir - 1][sutun - 1] == 'X':
                    sayac = sayac + 1
                if m[satir + 1][sutun - 1] == 'X':
                    sayac = sayac + 1
            elif sutun != 0 and sutun != boyut - 1 and satir == 0 and m[satir][sutun] == ' ':  # ust kenar
                sayac = 0
                puan = puan + 1
                if m[satir][sutun - 1] == 'X':
                    sayac = sayac + 1
                if m[satir][sutun + 1] == 'X':
                    sayac = sayac + 1
                if m[satir + 1][sutun] == 'X':
                    sayac = sayac + 1
                if m[satir + 1][sutun - 1] == 'X':
                    sayac = sayac + 1
                if m[satir + 1][sutun + 1] == 'X':
                    sayac = sayac + 1
            elif sutun != 0 and sutun != boyut - 1 and satir == boyut - 1 and m[satir][sutun] == ' ':  # alt kenar
                sayac = 0
                puan = puan + 1
                if m[satir][sutun - 1] == 'X':
                    sayac = sayac + 1
                if m[satir][sutun + 1] == 'X':
                    sayac = sayac + 1
                if m[satir - 1][sutun] == 'X':
                    sayac = sayac + 1
                if m[satir - 1][sutun - 1] == 'X':
                    sayac = sayac + 1
                if m[satir - 1][sutun + 1] == 'X':
                    sayac = sayac + 1

            elif m[satir][sutun] == 'X':
                print("KAYBETTİNİZ")
                f=1
                for i in range(boyut):
                    print(m[i])
                break
            print(sayac)
            matris[satir][sutun] = sayac
            for i in range(boyut):
                print(matris[i])
            print("puanininz:{}".format(puan))
            if puan == bitis:
                print("KAZANDİNİZ")
                secim = int(input("1-YENİDEN OYNA\n"
                                "2-CIKIS"))
                if secim==2:
                    f=1
                    break
                if secim == 1:
                    kontrol2 = 1
                    break
            if kontrol2==1:
                z=1
                continue
        if z==1:
            k=1
            continue
    if k==1:
        continue
    if f == 1:
        break


