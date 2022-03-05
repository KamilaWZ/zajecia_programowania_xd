def policz_domeny_pl(linki):

    n_domen_pl = 0
    #kod..
    orangutan = 'http://zajecia-programowania-xd.pl/flagi'
    surowe_info = requests.get(orangutan)
    text = surowe_info.text 
    efekt = text.split('</p>')
    linki =[] 

    for linia in efekt:
        link = linia.replace('<p>', '')
        link = link.replace('-', '')
        link = link.strip()
        if ' ' in link or '<' in link: 
            continue
        linki.append(link)

        for n in linki: 
            if ".pl" in n:
                n_domen_pl += 1
        return n_domen_pl

wynik = policz_domeny_pl(link)
print(wynik)