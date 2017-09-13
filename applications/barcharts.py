# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from collections import Counter as C

matriculados = pd.read_csv('../prepared_csv/matriculados.csv')
concluintes = pd.read_csv('../prepared_csv/concluintes.csv')

central_tendency_matriculados = {}
central_tendency_concluintes = {}
courses_matriculados = matriculados.columns.tolist()
courses_concluintes = concluintes.columns.tolist()

scatter_matriculados_2010 = []
scatter_matriculados_2011 = []
scatter_matriculados_2012 = []
scatter_matriculados_2013 = []

scatter_concluintes_2010 = []
scatter_concluintes_2011 = []
scatter_concluintes_2012 = []
scatter_concluintes_2013 = []

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
	key = i
	if key in matriculados: 
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

def autolabel(rects):
    """
    Attach a text label above each bar displaying its height
    """
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                '%d' % int(height),
                ha='center', va='bottom')

#plot barcharts

N = 4
ind = np.arange(N)  # the x locations for the groups
width = 0.23       # the width of the bars
fig, ax = plt.subplots()
rects1 = ax.bar(ind, central_tendency_means_matriculados, width, color='r')
rects2 = ax.bar(ind + width, central_tendency_medians_matriculados, width, color='y')
rects3 = ax.bar(ind + 2*width, central_tendency_std_matriculados, width, color='g')
rects4 = ax.bar(ind + 3*width, central_tendency_modes_matriculados, width, color='b')

plt.figure(1)
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

fig, ax = plt.subplots()
rects1 = ax.bar(ind, central_tendency_means_concluintes, width, color='r')
rects2 = ax.bar(ind + width, central_tendency_medians_concluintes, width, color='y')
rects3 = ax.bar(ind + 2*width, central_tendency_std_concluintes, width, color='g')
rects4 = ax.bar(ind + 3*width, central_tendency_modes_concluintes, width, color='b')

plt.figure(2)
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