import pandas as pd
papers = pd.read_csv('unique15.csv')
#for row in papers['accession_number']:
#    print('UT=', row)
papers['new_an'] = 'UT=' + papers['accession_number'].astype(str)
group=''
group1=''
#for i in range(len(papers['new_an'])):
#    if i%500==0:
        #group.append(i)
#        print(i)
        #print(papers['new_an'][i])
papers_list = papers['new_an'].tolist()
for i in range(len(papers_list)):
    if i < 501:
        group = group + papers_list[i] + ' or '
    if i > 501 and i < 1001:
        if i < 1000:
            group1 = group1 + papers_list[i]  + ' or '
        if i == 1000:
            group1 = group1 + papers_list[i]
print(group1)