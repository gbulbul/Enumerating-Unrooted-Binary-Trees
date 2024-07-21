# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 18:45:01 2024

@author: gbulb
"""

class Enumerating_Unrooted_Binary_Trees:
    def obtain_Unrooted_Binary_Trees(list_):
        list_1=list_[1:]
        tuples_list=[]
        for i,idx1 in enumerate(list_1):
            for j,idx2 in enumerate(list_1):
                if idx1!=idx2 and [idx2,idx1] not in tuples_list:
                   tuples_list.append([idx1,idx2])
                   print(f'((({idx1},{idx2})){list_[0]};')

if __name__=="__main__":   
    list_=['dog','cat','mouse','elephant']
    Enumerating_Unrooted_Binary_Trees.obtain_Unrooted_Binary_Trees(list_)
    