import pickle
load_file = open('save.dat','rb')
load_data = pickle.load(load_file)
print(load_data)
load_file.close()
