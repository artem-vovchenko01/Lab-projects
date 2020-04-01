def MyBaseSave(A, FileName):
    '''Збереження всієї бази даних в одному файлі '''
    import pickle
    f = open(FileName, 'wb')
    pickle.dump(A, f)
    f.close()
    del pickle

def MyBaseRestore(FileName):
    '''Відновлення всієї бази з файлу '''
    import pickle
    f = open(FileName, 'rb')
    A = pickle.load(f)
    f.close()
    del pickle
    return A
