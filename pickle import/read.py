import pickle
f=open("file.txt","rb")
data=pickle.looad(f)
f.close()
print(data)
