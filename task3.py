chest = {
'42': 'It is the Answer to Life the Universe and Everything.',
'666': 'If you would be a real seeker after truth, it is necessary that at least once in your life you doubt, as far as possible, all things.',
'8': 'It is wrong always, everywhere and for everyone, to believe anything upon insufficient evidence.',
'13': 'The Truth is in the Heart.',
'0': 'Freedom is secured not by the fulfilling of ones desires, but by the removal of desire.',
'9': 'The unexamined life is not worth living.',
'76': 'Life is a series of natural and spontaneous changes.',
'70': 'God is dead! He remains dead! And we have killed him.'
}

#(1) Sort the dictionary by its keys

res={}

keys = [int(i) for i in chest.keys()]
keys.sort()


for key in keys:
    res.update({str(key):chest[str(key)]})




#(2) Get the values of first, second, last and second last keys.

keys = [key for key in chest.keys()]

first_key=keys[0]
second_key=keys[1]
last_key=keys[-1]
secondlast_key=keys[-2]

result={}
result.update({str(first_key):chest[str(first_key)]})
result.update({str(second_key):chest[str(second_key)]})
result.update({str(secondlast_key):chest[str(secondlast_key)]})
result.update({str(last_key):chest[str(last_key)]})

# print(result)


#(3) Concatenate the values of obtained keys in a string

new_string=""
for key,value in result.items():
    new_string+=value




#(4) Get first and last characters of each word


res=""
for i in new_string.split(" "):
    res+=i[0]+i[-1]



print(res)

#(5)

new_dict={}
for i in res:
    if i in new_dict:
        new_dict[i]+=1

    else:
        new_dict[i]=1



op1 = {k: v for k, v in sorted(new_dict.items(), key=lambda item: item[1], reverse=True)}
first_n = dict(zip(list(op1.keys())[:5], list(op1.values())[:5]))

print(first_n)
print(list(first_n.values()))




##6

key_list = [52, 51, 61, 71, 56]
op6 = [i + j for i, j in zip(list(first_n.values()), key_list)]



#8

[print(chr(i), end="  ") for i in op6]