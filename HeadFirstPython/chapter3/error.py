import pickle
man=[]
other=[]
try:
    with open('man_data.txt','wb') as man_file,open('other_data.txt','wb') as other_file:
        pickle.dump(man,man_file)
        pickle.dump(other,other_file)
except IOError as err:
    print('file error'+str(err))
except pickle.pickleError as perr:
    print('pickling error:'+str(perr))