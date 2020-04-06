import pickle

#part1
dic={}

d={"ip":'value',"name":"name2","ttl":"10"}
dic["name1"]=d
print(dic["name1"])
with open('AS/my_dict.txt', 'wb') as f:
    pickle.dump(dic,f)

#part2
with open('AS/my_dict.txt', 'rb') as f:
    dic=pickle.load(f)
print(dic["name1"])