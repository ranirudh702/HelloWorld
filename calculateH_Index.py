def calculate_H_index(list_of_papers_with_num_citations):
    """
    Calculates the h-index, given a list of citation counts.
    """
    list_of_papers_with_num_citations.sort(reverse= True)
    h=0
    for index, citation in enumerate(list_of_papers_with_num_citations):
        if citation >= index + 1:
            h = h+1
        else:
            break
    return h
citations = [1,1,1,2,3,4,4,5,6]
print(calculate_H_index(citations))

