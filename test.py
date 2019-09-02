import pandas as pd
papers = pd.read_csv('unique15.csv', converters={'accession_number': lambda x: str(x)})
#добавляем UT= для каждого номера статьи
papers['new_an'] = 'UT=' + papers['accession_number'].astype(str)

#формируем группы по 500 статей (для удобства скачивания из WOS)
groups = []
for i in range(len(papers['new_an'])):
    if i%500==0:
        #group.append(i)
        groups.append(i)
groups.append(len(papers['new_an']))

#переводим строки в список
papers_list = papers['new_an'].tolist()
#groups = [0, 500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000,
#           6500, 7000, 7500, 8000, 8500, 9000, 9500, 10000, 10500, 11000, 11500, len(papers_list)]

#формируем списки номеров статей через or, по <500шт.
group=''
for gr in groups:
    if gr+500 < len(papers_list):
        for i in range(gr, gr+500):
            try:
                if i < gr+500-2:
                    group = group + papers_list[i] + ' or '
                if i == gr+500-1:
                    group = group + papers_list[i] + '\n\n'
            except:
                print('mistakes were made ', papers_list[i])
    else:
        for j in range(gr, len(papers_list)):
            if j < len(papers_list)-2:
                group = group + papers_list[j] + ' or '
            if j == len(papers_list)-1:
                group = group + papers_list[j]

#создаем текстовый файл, в который записываем сформированные группы со списками номеров статей                
with open('new_papers_queries.txt', 'w') as f:
    f.write(group)
f.close()
print('done')
#print(papers.head())

