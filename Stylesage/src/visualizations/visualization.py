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



def twoGroupedSubplot(data1, data2, data1_label = None, data2_label = None):

    plt.figure()
    plt.subplot(211)
    users_date_joined =data1.plot(kind='bar')
    plt.ylabel(data1_label)
    plt.subplot(212)
    train_date_tag = data2.plot(kind='bar')
    plt.ylabel(data2_label)
    plt.show()




def twoSimpleSubplot(data1, data2, data1_xticks = None, data2_xticks = None, data1_label = None, data2_label = None):
    plt.figure(1)
    plt.subplot(211)
    plt.plot(data1)
    plt.xticks(data1_xticks[0], data1_xticks[1])
    plt.xlabel(data1_label)


    plt.subplot(212)
    plt.plot(data2[0],data2[1])
    plt.xticks(data2_xticks)
    plt.xlabel(data2_label)

    plt.show()

    return 0
