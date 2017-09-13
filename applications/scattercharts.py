# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import lines as mlines
from matplotlib import transforms as mtransforms
from collections import Counter as C

matriculados = pd.read_csv('../prepared_csv/matriculados.csv')
concluintes = pd.read_csv('../prepared_csv/concluintes.csv')

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

	if i in courses_concluintes:
		scatter_matriculados_2010.append(matriculados[i][0])
		scatter_matriculados_2011.append(matriculados[i][1])
		scatter_matriculados_2012.append(matriculados[i][2])
		scatter_matriculados_2013.append(matriculados[i][3])

for i in courses_concluintes:
	if i in courses_matriculados:
		scatter_concluintes_2010.append(concluintes[i][0])
		scatter_concluintes_2011.append(concluintes[i][1])
		scatter_concluintes_2012.append(concluintes[i][2])
		scatter_concluintes_2013.append(concluintes[i][3])

#plot scatter charts

fig, ax= plt.subplots()

plt.figure(1)
plt.ylabel("Concluintes")
plt.xlabel("Matriculados")
a2010 = plt.scatter(scatter_matriculados_2010, scatter_concluintes_2010, marker="o", color="r", alpha=0.5) 
a2011 = plt.scatter(scatter_matriculados_2011, scatter_concluintes_2011, marker="o", color="b", alpha=0.5) 
a2012 = plt.scatter(scatter_matriculados_2012, scatter_concluintes_2012, marker="o", color="g", alpha=0.5) 
a2013 = plt.scatter(scatter_matriculados_2013, scatter_concluintes_2013, marker="o", color="y", alpha=0.5) 

plt.legend((a2010, a2011, a2012, a2013),
           ('2010', '2011', '2012', '2013'),
           scatterpoints=1,
           loc='lower right',
           ncol=1,
           fontsize=8)

line = mlines.Line2D([0, 1], [0, 1], color='red', linestyle='dashed')
transform = ax.transAxes
line.set_transform(transform)
ax.add_line(line)

plt.show()