import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

matriculados = pd.read_csv('../prepared_csv/matriculados.csv')
concluintes = pd.read_csv('../prepared_csv/concluintes.csv')

central_tendency_matriculados = {}
central_tendency_concluintes = {}
courses_matriculados = matriculados.columns.tolist()

#Populating central_tendency_matriculados
for i in courses_matriculados:
	central_tendency_matriculados[i] = []
	central_tendency_matriculados[i].append(np.mean(matriculados[i]))
	central_tendency_matriculados[i].append(np.median(matriculados[i]))
	central_tendency_matriculados[i].append("%.2f" % np.std(matriculados[i]))

	key = i

	if key in concluintes:
		central_tendency_concluintes[i] = []
		central_tendency_concluintes[i].append(np.mean(concluintes[i]))
		central_tendency_concluintes[i].append(np.median(concluintes[i]))
		central_tendency_concluintes[i].append("%.2f" % np.std(concluintes[i]))

matriculados_2010 = []
matriculados_2011 = []
matriculados_2012 = []
matriculados_2013 = []

for i in courses_matriculados:
	matriculados_2010.append(matriculados[i][0])
	matriculados_2011.append(matriculados[i][1])
	matriculados_2012.append(matriculados[i][2])
	matriculados_2013.append(matriculados[i][3])

concluintes_2010 = []
concluintes_2011 = []
concluintes_2012 = []
concluintes_2013 = []

for i in courses_matriculados:
	if i in concluintes:
		concluintes_2010.append(concluintes[i][0])
		concluintes_2011.append(concluintes[i][1])
		concluintes_2012.append(concluintes[i][2])
		concluintes_2013.append(concluintes[i][3])
"""
#plot boxplots
plt.boxplot([matriculados_2010, matriculados_2011, matriculados_2012, matriculados_2013])
plt.title("Número de matriculados entre 2010 e 2013")
plt.ylabel("Nº de matrículas")
plt.xticks([1,2,3,4],['2010', '2011', '2012', '2013'], rotation='horizontal')
plt.show()
"""

matriculados_overall = []
concluintes_overall = []

matriculados_overall.append(sum(matriculados_2010))
matriculados_overall.append(sum(matriculados_2011))
matriculados_overall.append(sum(matriculados_2012))
matriculados_overall.append(sum(matriculados_2013))

concluintes_overall.append(sum(concluintes_2010))
concluintes_overall.append(sum(concluintes_2011))
concluintes_overall.append(sum(concluintes_2012))
concluintes_overall.append(sum(concluintes_2013))

#plot line charts
fig, ax = plt.subplots()
plt.plot(range(1,5), matriculados_overall, 'b--o', label='Alunos matriculados')
plt.plot(range(1,5), concluintes_overall , 'g--o', label='Alunos concluintes')
plt.title('Número de matriculados e concluintes')
plt.ylabel('Matriculados e concluintes')
plt.xlabel('Anos')
legend = ax.legend(loc='center', shadow=True, fontsize='x-large')
plt.xticks([1,2,3,4],['2010', '2011', '2012', '2013'], rotation='horizontal')
plt.show()