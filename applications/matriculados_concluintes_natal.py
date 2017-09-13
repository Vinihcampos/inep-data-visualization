import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from collections import Counter as C

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
	central_tendency_matriculados[i].append(C(matriculados[i]).most_common(1)[0][0])
	central_tendency_matriculados[i].append(min(matriculados[i]))
	central_tendency_matriculados[i].append(max(matriculados[i]))

	key = i

	if key in concluintes:
		central_tendency_concluintes[i] = []
		central_tendency_concluintes[i].append(np.mean(concluintes[i]))
		central_tendency_concluintes[i].append(np.median(concluintes[i]))
		central_tendency_concluintes[i].append("%.2f" % np.std(concluintes[i]))
		central_tendency_concluintes[i].append(C(concluintes[i]).most_common(1)[0][0])
		central_tendency_concluintes[i].append(min(concluintes[i]))
		central_tendency_concluintes[i].append(max(concluintes[i]))

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
"""
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
"""
central_tendency_means_matriculados = []
central_tendency_medians_matriculados = []
central_tendency_modes_matriculados = []
central_tendency_std_matriculados = []

central_tendency_means_concluintes = []
central_tendency_medians_concluintes = []
central_tendency_modes_concluintes = []
central_tendency_std_concluintes = []

#Central tendencies of enrolled
central_tendency_means_matriculados.append( "%.2f" % (sum(matriculados_2010) / len(matriculados_2010)) )
central_tendency_means_matriculados.append( "%.2f" % (sum(matriculados_2011) / len(matriculados_2011)) )
central_tendency_means_matriculados.append( "%.2f" % (sum(matriculados_2012) / len(matriculados_2012)) )
central_tendency_means_matriculados.append( "%.2f" % (sum(matriculados_2013) / len(matriculados_2013)) )

central_tendency_medians_matriculados.append( "%.2f" % np.median(matriculados_2010) )
central_tendency_medians_matriculados.append( "%.2f" % np.median(matriculados_2011) )
central_tendency_medians_matriculados.append( "%.2f" % np.median(matriculados_2012) )
central_tendency_medians_matriculados.append( "%.2f" % np.median(matriculados_2013) )

central_tendency_std_matriculados.append( "%.2f" % np.std(matriculados_2010) )
central_tendency_std_matriculados.append( "%.2f" % np.std(matriculados_2011) )
central_tendency_std_matriculados.append( "%.2f" % np.std(matriculados_2012) )
central_tendency_std_matriculados.append( "%.2f" % np.std(matriculados_2013) )

central_tendency_modes_matriculados.append( C(matriculados_2010).most_common(1)[0][1] )
central_tendency_modes_matriculados.append( C(matriculados_2011).most_common(1)[0][1] )
central_tendency_modes_matriculados.append( C(matriculados_2012).most_common(1)[0][1] )
central_tendency_modes_matriculados.append( C(matriculados_2013).most_common(1)[0][1] )

#Central tendencies of graduated
central_tendency_means_concluintes.append( "%.2f" % (sum(concluintes_2010) / len(concluintes_2010)) )
central_tendency_means_concluintes.append( "%.2f" % (sum(concluintes_2011) / len(concluintes_2011)) )
central_tendency_means_concluintes.append( "%.2f" % (sum(concluintes_2012) / len(concluintes_2012)) )
central_tendency_means_concluintes.append( "%.2f" % (sum(concluintes_2013) / len(concluintes_2013)) )

central_tendency_medians_concluintes.append( "%.2f" % np.median(concluintes_2010) )
central_tendency_medians_concluintes.append( "%.2f" % np.median(concluintes_2011) )
central_tendency_medians_concluintes.append( "%.2f" % np.median(concluintes_2012) )
central_tendency_medians_concluintes.append( "%.2f" % np.median(concluintes_2013) )

central_tendency_std_concluintes.append( "%.2f" % np.std(concluintes_2010) )
central_tendency_std_concluintes.append( "%.2f" % np.std(concluintes_2011) )
central_tendency_std_concluintes.append( "%.2f" % np.std(concluintes_2012) )
central_tendency_std_concluintes.append( "%.2f" % np.std(concluintes_2013) )

central_tendency_modes_concluintes.append( C(concluintes_2010).most_common(1)[0][1] )
central_tendency_modes_concluintes.append( C(concluintes_2011).most_common(1)[0][1] )
central_tendency_modes_concluintes.append( C(concluintes_2012).most_common(1)[0][1] )
central_tendency_modes_concluintes.append( C(concluintes_2013).most_common(1)[0][1] )

"""
print ("Central tendencies (enrolled): ")
print ("means: ", end='')
print(central_tendency_means_matriculados)
print ("medians: ", end='')
print(central_tendency_medians_matriculados)
print ("stds: ", end='')
print(central_tendency_std_matriculados)

print ("Central tendencies (graduated): ")
print ("means: ", end='')
print(central_tendency_means_concluintes)
print ("medians: ", end='')
print(central_tendency_medians_concluintes)
print ("stds: ", end='')
print(central_tendency_std_concluintes)
"""

def autolabel(rects):
    """
    Attach a text label above each bar displaying its height
    """
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                '%d' % int(height),
                ha='center', va='bottom')

#Plot bar charts
def plot_enrolled(N, ind, width, fig, ax):
	rects1 = ax.bar(ind, central_tendency_means_matriculados, width, color='r')
	rects2 = ax.bar(ind + width, central_tendency_medians_matriculados, width, color='y')
	rects3 = ax.bar(ind + 2*width, central_tendency_std_matriculados, width, color='g')
	rects4 = ax.bar(ind + 3*width, central_tendency_modes_matriculados, width, color='b')
	
	# add some text for labels, title and axes ticks
	ax.set_ylabel('Means, Medians and Standard Deviations')
	ax.set_title('Central tendencies of enrolled students')
	ax.set_yticks(np.arange(0, 2200, 200))
	ax.set_xticks(ind + width * 1.5)
	ax.set_xticklabels(('2010', '2011', '2012', '2013'))
	
	ax.legend((rects1[0], rects2[0], rects3[0], rects4[0]), ('Means', 'Medians', 'Standard Deviations', 'Modes'))
	autolabel(rects1)
	autolabel(rects2)
	autolabel(rects3)
	autolabel(rects4)
	plt.show()

def plot_graduated(N, ind, width, fig, ax):
	rects1 = ax.bar(ind, central_tendency_means_concluintes, width, color='r')
	rects2 = ax.bar(ind + width, central_tendency_medians_concluintes, width, color='y')
	rects3 = ax.bar(ind + 2*width, central_tendency_std_concluintes, width, color='g')
	rects4 = ax.bar(ind + 3*width, central_tendency_modes_concluintes, width, color='b')
	
	# add some text for labels, title and axes ticks
	ax.set_ylabel('Means, Medians and Standard Deviations')
	ax.set_title('Central tendencies of graduated students')
	ax.set_yticks(np.arange(0, 400, 50))
	ax.set_xticks(ind + width * 1.5)
	ax.set_xticklabels(('2010', '2011', '2012', '2013'))
	
	ax.legend((rects1[0], rects2[0], rects3[0], rects4[0]), ('Means', 'Medians', 'Standard Deviations', 'Modes'))
	autolabel(rects1)
	autolabel(rects2)
	autolabel(rects3)	
	autolabel(rects4)
	plt.show()


N = 4
ind = np.arange(N)  # the x locations for the groups
width = 0.23       # the width of the bars
fig, ax = plt.subplots()

plot_enrolled(N, ind, width, fig, ax)
plot_graduated(N, ind, width, fig, ax)

"""
#Create CSV for central tendencies
cursos_csv = {'CURSO' : [], 'MÉDIA': [], 'MEDIANA': [], 'DESVIO PADRÃO': [], 'MODA': [], 'MIN': [], 'MAX': []}

for i in central_tendency_matriculados:
	cursos_csv['CURSO'].append(i)
	cursos_csv['MÉDIA'].append(central_tendency_matriculados[i][0])
	cursos_csv['MEDIANA'].append(central_tendency_matriculados[i][1])
	cursos_csv['DESVIO PADRÃO'].append(central_tendency_matriculados[i][2])
	cursos_csv['MODA'].append(central_tendency_matriculados[i][3])
	cursos_csv['MIN'].append(central_tendency_matriculados[i][4])
	cursos_csv['MAX'].append(central_tendency_matriculados[i][5])

pd.DataFrame(cursos_csv).to_csv('../prepared_csv/central_tendency_enrolled.csv', encoding='utf-8', index=False,
	columns=['CURSO', 'MÉDIA', 'MEDIANA', 'DESVIO PADRÃO', 'MODA', 'MIN', 'MAX'])

cursos_csv = {'CURSO' : [], 'MÉDIA': [], 'MEDIANA': [], 'DESVIO PADRÃO': [], 'MODA': [], 'MIN': [], 'MAX': []}

for i in central_tendency_concluintes:
	cursos_csv['CURSO'].append(i)
	cursos_csv['MÉDIA'].append(central_tendency_concluintes[i][0])
	cursos_csv['MEDIANA'].append(central_tendency_concluintes[i][1])
	cursos_csv['DESVIO PADRÃO'].append(central_tendency_concluintes[i][2])
	cursos_csv['MODA'].append(central_tendency_concluintes[i][3])
	cursos_csv['MIN'].append(central_tendency_concluintes[i][4])
	cursos_csv['MAX'].append(central_tendency_concluintes[i][5])

pd.DataFrame(cursos_csv).to_csv('../prepared_csv/central_tendency_graduated.csv', encoding='utf-8', index=False,
	columns=['CURSO', 'MÉDIA', 'MEDIANA', 'DESVIO PADRÃO', 'MODA', 'MIN', 'MAX'])
"""