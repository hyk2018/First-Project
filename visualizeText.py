"""
Visualize data using Matplotlib.
project
2017
Yankai He
"""
import numpy as np
import matplotlib.pyplot as plt
from collections import OrderedDict    # ordered dictionary for printing
import re
import doctest
from matplotlib.ticker import MaxNLocator
from collections import namedtuple

def replace(words):
    '''helper function that replaces some meaningless marks with 'the' that will be filtered out later
    >>> replace(['tom','dick','harry','-','c'])
    ['tom', 'dick', 'harry', 'the', 'the']
    '''
    for i in range(len(words)):
        if len(words[i])==1 or len(words[i])==0:
            words[i]='the'
    return words
            
def wordCount(fileName):
    ''' modified version of wordCount that
    counts the number of appearace of each top 20 unique words
    
    >>> wordCount('robin_hood.txt')
    (['robin', 'hood', 'thou', 'good', 'said', 'john', 'robyn', 'shall', 'little', 'see', 'men', 'thy', 'may', 'man', 'king', 'sayd', 'well', 'bold', 'old', 'come'], [1036, 779, 439, 357, 337, 307, 298, 254, 248, 248, 243, 227, 226, 224, 220, 216, 204, 188, 179, 163])
    '''
    f=open(fileName,'r',encoding = 'UTF-8') #the file that is going to be analyzed
    text=f.read()
    f.close()
    text=text.lower()
    words=re.split('\W+',text)

    g=open('stopwords.txt','r',encoding = 'UTF-8') #the file that contains stopwords
    text2=g.read()
    g.close()
    text2=text2.lower()
    words2=re.split('\W+',text2)

    replace(words)# replace all meaningless signs that is not part of stopwords

    d={}
    for w in words:
        if w not in words2:
            
            if w not in d:
                d[w] = 1
            else:
                d[w] += 1
    newd=OrderedDict(sorted(d.items(),key=lambda t:t[1],reverse=True)) #makes a rearranged dictionary

    #find out times of appearance for each unique word in the text
    count=0
    unique=0
    words=[]
    counts=[]
    for i,j in newd.items():
        count += 1
        words += [i]
        counts += [j]
        if count == 20:
            break
    return words,counts

def visualize():
    '''function that visualizes information including top 20 unique words
    and each of their frequencies in Robin Hood and Robin Crusoe
    '''
    #figure for Robin Hood
    words,counts1=wordCount('robin_hood.txt')
    n_groups = 20
    means_avg = counts1
    fig, ax = plt.subplots()
    index = np.arange(n_groups)
    bar_width = 0.2
    opacity = 0.4
    error_config = {'ecolor': '0.3'}
    rects1 = ax.bar(index, means_avg, bar_width,
                    alpha=opacity, color='b',
                     error_kw=error_config,
                    label='Number of Unique Words in RobinHood')

    ax.set_xlabel('Words')
    ax.set_ylabel('Counts')
    ax.set_title('Counts of Unique Words in RobinHood')
    ax.set_xticks(index + bar_width / 2)
    ax.set_xticklabels(words,rotation='vertical')
    ax.legend()
    fig.tight_layout()
    plt.show()

    #Figure for Robin Crusoe
    words,counts2=wordCount('crusoe.txt')
    n_groups = 20
    means_num = counts2
    fig, ax = plt.subplots()
    index = np.arange(n_groups)
    bar_width = 0.2
    opacity = 0.4
    error_config = {'ecolor': '0.3'}
    rects2 = ax.bar(index + bar_width, means_num, bar_width,
                    alpha=opacity, color='r',
                     error_kw=error_config,
                    label='Number Of Unique Words in Crusoe')

    ax.set_xlabel('Words')
    ax.set_ylabel('Counts')
    ax.set_title('Counts of Unique Words in Crusoe')
    ax.set_xticks(index + bar_width / 2)
    ax.set_xticklabels(words,rotation='vertical')
    ax.legend()
    fig.tight_layout()
    plt.show()



def main():
    '''convenient way of executing the program'''
    visualize()

doctest.testmod()
