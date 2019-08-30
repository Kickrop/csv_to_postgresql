import pandas as pd
papers = pd.read_csv('unique15.csv')
#for row in papers['accession_number']:
#    print('UT=', row)
papers['new_an'] = 'UT=' + papers['accession_number'].astype(str)
group=''
#group1=''
# pam = []
# for i in range(len(papers['new_an'])):
#     if i%500==0:
#         #group.append(i)
#         pam.append(i)
# pam.append(len(papers['new_an']))
# print(pam)
groups = [0, 500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000,
           6500, 7000, 7500, 8000, 8500, 9000, 9500, 10000, 10500, 11000, 11500, 11806]


papers_list = papers['new_an'].tolist()


for gr in groups:
    if gr+500 < len(papers_list):
        for i in range(gr, gr+500):
            # if i < gr:
            #     group= group + papers_list[i] + ' or '
            # if i == gr:
            #     group = group + papers_list[i] + ';'
            try:
                group = group + papers_list[i] + ' or '
            except:
                print('mistakes were made')
    else:
        for j in range(gr, len(papers_list)):
                group = group + papers_list[j] + ' or '
            # if i > gr and i < gr+500:
            #     group = group + papers_list[i] + ' or '
            # if i == gr+500:
            #     group = group + papers_list[i] + ';'
with open('output_test.txt', 'w') as f:
    f.write(group)
f.close()
#print(group[1])
#group.to_csv('pam.csv')
