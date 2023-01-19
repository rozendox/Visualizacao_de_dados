# Importação das bibliotecas
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

# Carregamento da base de dados
base = pd.read_csv('orchard.csv')
base

# Criação do gráfico 3D, indicando o atributo projection = '3d' e passando três atributos (decrease, rowpos e colpos)
figura = plt.figure()
eixo = figura.add_subplot(1, 1, 1, projection = '3d')
eixo.scatter(base.decrease, base.rowpos, base.colpos)
eixo.set_xlabel('decrease')
eixo.set_ylabel('rowpos')
eixo.set_zlabel('colpos')
