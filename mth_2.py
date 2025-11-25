import pandas as pd

def drop_dup(data):
    #display(data[data.duplicated()])
    print('Кол-во дублей ДО удаления: ',data.duplicated().sum())
    print('Кол-во ДО удаления: ',len(data))
    data = data.drop_duplicates() 
    print('Кол-во ПОСЛЕ удаления: ',len(data))
    print('')
