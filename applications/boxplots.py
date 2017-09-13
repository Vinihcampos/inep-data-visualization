# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from collections import Counter as C

matriculados = pd.read_csv('../prepared_csv/matriculados.csv')
concluintes = pd.read_csv('../prepared_csv/concluintes.csv')

courses_matriculados = matriculados.columns.tolist()
courses_concluintes = concluintes.columns.tolist()

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

#plot boxplots
plt.figure(1)
plt.boxplot([matriculados_2010, matriculados_2011, matriculados_2012, matriculados_2013])
plt.title("Número de matriculados entre 2010 e 2013")
plt.ylabel("Nº de matrículas")
plt.xticks([1,2,3,4],['2010', '2011', '2012', '2013'], rotation='horizontal')

plt.figure(2)
plt.boxplot([concluintes_2010, concluintes_2011, concluintes_2012, concluintes_2013])
plt.title("Número de concluintes entre 2010 e 2013")
plt.ylabel("Nº de concluintes")
plt.xticks([1,2,3,4],['2010', '2011', '2012', '2013'], rotation='horizontal')

plt.show()