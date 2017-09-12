import pandas as pd

#matriculados_2009 = pd.read_csv('csv/matriculados/matriculados_2009.csv')
matriculados_2010 = pd.read_csv('../raw_csv/matriculados/matriculados_2010.csv')
matriculados_2011 = pd.read_csv('../raw_csv/matriculados/matriculados_2011.csv')
matriculados_2012 = pd.read_csv('../raw_csv/matriculados/matriculados_2012.csv')
matriculados_2013 = pd.read_csv('../raw_csv/matriculados/matriculados_2013.csv')

cursos = set()

#for i in matriculados_2009['Nome Curso']:
#	cursos.add(i)
for i in matriculados_2010['Nome Curso']:
	cursos.add(i)
for i in matriculados_2011['Nome Curso']:
	cursos.add(i)
for i in matriculados_2012['Nome Curso']:
	cursos.add(i)
for i in matriculados_2013['Nome Curso']:
	cursos.add(i)

dict = {}

for i in cursos:
	dict[i] = [0,0,0,0]

#for index, row in matriculados_2009.iterrows():
#	dict[row['Nome Curso']][0] += row['Número de Matrículas'];
for index, row in matriculados_2010.iterrows():
	dict[row['Nome Curso']][0] += row['Número de Matrículas'];
for index, row in matriculados_2011.iterrows():
	dict[row['Nome Curso']][1] += row['Número de Matrículas'];
for index, row in matriculados_2012.iterrows():
	dict[row['Nome Curso']][2] += row['Número de Matrículas'];
for index, row in matriculados_2013.iterrows():
	dict[row['Nome Curso']][3] += row['Número de Matrículas'];

cursos_csv = {'CURSOS' : [], '2010': [], '2011': [], '2012': [], '2013': []}

for i in cursos:
	cursos_csv['CURSOS'].append(i)
	cursos_csv['2010'].append(dict[i][0])
	cursos_csv['2011'].append(dict[i][1])
	cursos_csv['2012'].append(dict[i][2])
	cursos_csv['2013'].append(dict[i][3])

#pd.DataFrame(cursos_csv).to_csv('../prepared_csv/matriculados_inv.csv', sep='\t', encoding='utf-8', index=False, header=True, columns=["CURSOS", "2010", "2011", "2012", "2013"])
pd.DataFrame(dict).to_csv('../prepared_csv/matriculados.csv', encoding='utf-8', index=False)