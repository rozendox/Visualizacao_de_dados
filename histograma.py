# Importação das bibliotecas
import pandas as pd
import seaborn as srn
#pip install seaborn (executar no Anaconda Prompt)
import matplotlib.pyplot as plt

# Carregamento da base de dados
base = pd.read_csv('trees.csv')
base.head()

# Histograma com 10 divisões (bins) e com gráfico de densidade
srn.distplot(base.Volume, bins = 10, axlabel = 'Volume').set_title('Árvores')

# Carregamento de outra base de dados
base2 = pd.read_csv('chicken.csv')
base2.head()

# Criação de novo dataframe agrupando o atributo 'feed'
agrupado = base2.groupby(['feed'])['weight'].sum()
agrupado

# Novo dataframe somente para testar os filtros do pandas
teste = base2.loc[base2['feed'] == 'horsebean']
teste

# Histrograma considerando somente o valor 'horsebean'
srn.distplot(base2.loc[base2['feed'] == 'horsebean'].weight, hist = False).set_title('horsebean')

# Histrograma considerando somente o valor 'casein'
srn.distplot(base2.loc[base2['feed'] == 'casein'].weight).set_title('casein')

# Histrograma considerando somente o valor 'linseed'
srn.distplot(base2.loc[base2['feed'] == 'linseed'].weight).set_title('linseed')

# Histrograma considerando somente o valor 'meatmeal'
srn.distplot(base2.loc[base2['feed'] == 'meatmeal'].weight).set_title('meatmeal')

# Histrograma considerando somente o valor 'soybean'
srn.distplot(base2.loc[base2['feed'] == 'soybean'].weight).set_title('soybean')

# Histrograma considerando somente o valor 'sunflower'
srn.distplot(base2.loc[base2['feed'] == 'sunflower'].weight).set_title('sunflower')

#impresssão em gráfico 2 x 3
plt.figure()
plt.subplot(3,2,1)
srn.distplot(base2.loc[base2['feed'] == 'horsebean'].weight, hist = False).set_title('horsebean')
plt.subplot(3,2,2)
srn.distplot(base2.loc[base2['feed'] == 'casein'].weight).set_title('casein')
plt.subplot(3,2,3)
srn.distplot(base2.loc[base2['feed'] == 'linseed'].weight).set_title('linseed')
plt.subplot(3,2,4)
srn.distplot(base2.loc[base2['feed'] == 'meatmeal'].weight).set_title('meatmeal')
plt.subplot(3,2,5)
srn.distplot(base2.loc[base2['feed'] == 'soybean'].weight).set_title('soybean')
plt.subplot(3,2,6)
srn.distplot(base2.loc[base2['feed'] == 'sunflower'].weight).set_title('sunflower')
#ajusta o layout para não haver sobreposição
plt.tight_layout()
