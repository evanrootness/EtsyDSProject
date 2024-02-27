import numpy as np

def df_to_list_and_dict(dataframe_column):
    """Convert one column of a dataframe into a list of unique words and a dictionary counting how many times those words each show up.

    Args:
        dataframe_column (Pandas dataframe column): input dataframe column of strings
    """
    
    list_of_all_words = []
    
    for name in dataframe_column:
        temp_list_string = name.split()
        for string in temp_list_string:
            temp_string = string
            if ',' in temp_string:
                temp_string = string.replace(',', '')
            list_of_all_words.append(temp_string)
            
    unique_word_list = list(set(list_of_all_words))
    
    print('Total number of words among all listing names:', len(list_of_all_words))
    print('Count of unique words among all listing names:', len(unique_word_list))
    
    # initialize dictionary to contain unique words and the amount of times they show up    
    word_counter = {}

    for word in list_of_all_words:
        if word not in word_counter:
            word_counter[word] = 0
        word_counter[word] += 1
        
    return unique_word_list, word_counter


def order_words(word_dict, unique_list):
    """Convert a scrambled list of words into an Numpy array with two columns, one with the words and one with the corresponding number. From most common to least common. 

    Args:
        word_dict (Dictionary): Dictionary containing all words and the corresponding number of times they were in a listing name.
        unique_list (List): The unordered list of unique words.

    Returns:
        _type_: Numpy array with two columns. There are as many rows as there are unique words.
    """
    
    ordered_list = []
    ordered_list_nums = []
    
    # for each unique word
    for word in unique_list:
        
        # value of how many time that word shows up
        temp_num_occur = word_dict[word]
        
        temp_index_list = []
        # loop through new list of ordered words and find where to put new unqiue word
        for i in range(len(ordered_list)):
            if temp_num_occur < ordered_list_nums[i]:
                temp_index_list.append(i)
        
        # if the temp_index_list is empty, must place the current word at the beginning
        if len(temp_index_list) > 0:
            index = temp_index_list[-1] + 1
        else:
            index = 0
        ordered_list.insert(index, word)
        ordered_list_nums.insert(index, word_dict[word])
        
    return np.array([ordered_list, ordered_list_nums])