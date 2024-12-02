import seaborn as sns
import matplotlib.pyplot as plt

def plot_countplots(data, categorical_vars):
    """ Plot countplots for categorical variables """
    fig, ax = plt.subplots(6, 3, figsize=(12, 20))
    for i, var in enumerate(categorical_vars):
        sns.countplot(data[var], ax=ax[i // 3][i % 3])
    plt.show()

def plot_distribution(data, continuous_vars):
    """ Plot distribution plots for continuous variables """
    import seaborn as sns
    nd = pd.melt(data, value_vars=continuous_vars)
    n1 = sns.FacetGrid(nd, col='variable', col_wrap=2, sharex=False, sharey=False)
    n1 = n1.map(sns.histplot, 'value')
    plt.show()

def plot_correlation_matrix(data, continuous_vars):
    """ Plot correlation heatmap for continuous variables """
    corr = data[continuous_vars].corr()
    sns.heatmap(corr, annot=True, cmap='coolwarm')
    plt.show()
