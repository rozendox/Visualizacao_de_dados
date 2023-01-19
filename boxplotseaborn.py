# Importação das bibliotecas
import pandas as pd
import seaborn as srn

# Carregamento da base de dados
base = pd.read_csv('trees.csv')
base.head()

# Visualização de um boxplot
srn.boxplot(base.Volume).set_title('Árvores')

# Visualização de vários boxplots na mesma imagem
srn.boxplot(data = base)
