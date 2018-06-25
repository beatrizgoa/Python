from matplotlib import pyplot as plt
from numpy import arange
import seaborn as sns

def plot_correlation(data, xticks = None, yticks = None):
    # correlacion among variables
    plt.matshow(data[['tag_id',  'post_id',  'product_id',  'user_id',  'date_tag',  'color', 'click_count', 'product_brand',  'country',  'date_joined' ]].corr())
    plt.legend()
    if xticks != None and yticks != None:
        plt.xticks(arange(10), xticks)
        plt.yticks(arange(10), yticks)
    plt.show()

    return 0


def plotSns(data, y_vars = None, x_vars = None, diag_kind = None, markers = '+'):

    sns.pairplot(data, y_vars=y_vars, x_vars=x_vars, diag_kind=diag_kind, markers=markers)
    plt.show()



def groupBySubplots(group_brand, group_country, group_color, group_date):
    plt.figure()

    plt.subplot(221)
    plt.plot(group_brand)
    plt.xlabel('product brand')

    plt.subplot(222)
    group_country.plot(kind='bar')
    plt.xlabel('country')

    plt.subplot(223)
    group_color.plot(kind='bar')
    plt.xlabel('color')

    plt.subplot(224)
    plt.plot(group_date)
    plt.xlabel('date tag')
    plt.show()

    return 0
