from abc import ABCMeta, abstractmethod
import matplotlib.pyplot as plt
import seaborn as sns

####################father################   
class Graphics(metaclass = ABCMeta):
    
    @abstractmethod
    def plotting(df,columns):
        return NotImplementedError

####################child################   
class BoxPlotsGraphics(Graphics): 

    def plotting(df, columns):
        fig, ax = plt.subplots(figsize=(10, 6))
        df.boxplot(column=columns, ax=ax)
        plt.title('Boxplot')
        plt.ylabel('Values')
        plt.xlabel('Columns')
        plt.xticks(rotation=45)
        plt.show()

####################child################   
class DistributionGraphics(Graphics): 
    def plotting(df, columns):
        num_cols = len(columns)
        num_rows = (num_cols // 2) + (num_cols % 2)
        fig, axes = plt.subplots(num_rows, 2, figsize=(15, num_rows * 5))
        axes = axes.flatten()

        for i, col in enumerate(columns):
            ax = axes[i]
            ax.hist(df[col], bins=30, alpha=0.7)
            ax.set_title(f'Distribution of {col}')
            ax.set_xlabel(col)
            ax.set_ylabel('Density')

        plt.tight_layout()
        plt.show()

####################child################   
class CorrelationMatrixGraphics(Graphics): 
    def plotting(df, columns):
        corr = df[columns].corr()
        plt.figure(figsize=(10, 8))
        heatmap = sns.heatmap(corr, annot=True, cmap='viridis', fmt=".2f")
        heatmap.set_title('Correlation Matrix', fontdict={'fontsize': 18})
        plt.show()
