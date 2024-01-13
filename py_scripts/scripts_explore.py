
def addCategoricalLists(init_data, list_of_categories):
    """Produce categorical data for a specified list of keywords

    Args:
        init_data (pd dataframe): Dataframe to get listing names from and append categorical data onto.
        list_of_categories (list): List of keywords to create nominal binary data for.

    Returns:
        pd dataframe: Original dataframe with the categorical data appended in new columns.
    """
    
    for category in list_of_categories:
        temp_category_list = []
        for i in range(len(init_data)):
            if (category in init_data['name'][i]):
                temp_category_list.append(1)
            else:
                temp_category_list.append(0)
        init_data[str(category)] = temp_category_list
    return init_data
