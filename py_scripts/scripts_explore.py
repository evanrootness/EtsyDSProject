import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import cm

def one_hot_encode(init_data, list_of_categories):
    """Produce categorical data for a specified list of keywords

    Args:
        init_data (pd dataframe): Dataframe to get listing names from and append categorical data onto.
        list_of_categories (list): List of keywords to create nominal binary data for.

    Returns:
        pd dataframe: Original dataframe with the categorical data appended in new columns.
    """
    data_copy = init_data.copy()
    for category in list_of_categories:
        temp_category_list = []
        for i in range(len(data_copy['name'])):
            if (category in data_copy['name'].iloc[i]):
                temp_category_list.append(1)
            else:
                temp_category_list.append(0)
        data_copy[str(category)] = temp_category_list
    return data_copy



def bar_plot_categories_mean(dataset, cat_list, figx=15, figy=3):
    color = iter(cm.rainbow(np.linspace(0, 1, len(cat_list) * 2)))
    plt.figure(figsize=(figx, figy))
    for caty in cat_list:
        c = next(color)
        plt.bar(x=[caty],#, 'No ' + caty], 
                height=[np.mean(dataset.query('{0} == 1'.format(caty))['min_price'])],#, np.mean(dataset.query('{0} == 0'.format(caty))['min_price'])],
                color = c)
        
    plt.axhline(np.mean(dataset['min_price']), color='k', label='Average over all data')
    plt.legend()
    plt.title('Mean minimum price on listing of different categories')
    

def bar_plot_categories_median(dataset, cat_list, figx=15, figy=3):
    color = iter(cm.rainbow(np.linspace(0, 1, len(cat_list) * 2)))
    plt.figure(figsize=(figx, figy))
    for caty in cat_list:
        c = next(color)
        plt.bar(x=[caty],#, 'No ' + caty], 
                height=[np.median(dataset.query('{0} == 1'.format(caty))['min_price'])],# np.median(dataset.query('{0} == 0'.format(caty))['min_price'])],
                color = c)
        
    plt.axhline(np.median(dataset['min_price']), color='k', label='Median over all data')
    plt.legend()
    plt.title('Median minimum price on listing of different categories')



def significance(data, ordered_list_of_words):
    word_list = []
    list_with = []
    list_without = []
    
    for word in ordered_list_of_words:
        word_list.append(word)

        # list_with.append(data.query('{0} == 1'.format(word))['min_price'].median())
        # list_without.append(data.query('{0} == 0'.format(word))['min_price'].median())
        list_with.append(data.where(data[word] == 1).dropna(subset=word)['min_price'].median())
        list_without.append(data.where(data[word] == 0).dropna(subset=word)['min_price'].median())
        
    # output a np.array of word and difference between 0 and 1 medians
    return np.array([word_list, list_with, list_without])

