import requests

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

    print(link)
    linki.append(link)

#napisz funkcję zliczająca  wszytskie domeny gdzie jest tylko .pl:

def policz_domeny_pl():
    
    return 0