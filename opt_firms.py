'''
Read in conjunction with Respons-ableSG documentation
16 May 2020

Programme to determine list of firms which will maximise GDP
with an average r that will not exceed 1.0

Working Dataset
Firm A    0.6 R   30 GDP
Firm B    0.9 R    8 GDP
Firm C    1.1 R   79 GDP
Firm D    1.6 R   54 GDP
Firm E    0.3 R   17 GDP
'''

data = [('A',0.6,30),('B',0.9, 8),('C',1.1,79),
  ('D',1.6,54),('E',0.3,17)]

r_ne = 1.0

track = {}

for i in range(len(data)):
   r_total = data[i][1]
   firm_list = [data[i][0]]
   gdp_total = data[i][2]
   for n in range(len(data)):
       if data[n] == data[i]:
           continue
       r_total = r_total + data[n][1]
       r_avg = r_total / len(firm_list)
       gdp_total = gdp_total + data[n][2]
       if r_avg > r_ne:
           r_total = r_total - data[n][1]
           r_avg = r_total / len(firm_list)
           gdp_total = gdp_total - data[n][2]
           continue
       firm_list.append(data[n][0])
   track[gdp_total] = firm_list

tmax = max(list(track))
for obj in track[tmax]:
   print(f'Firm(s) {obj}')
print(f'Combined max GDP of {tmax}')
