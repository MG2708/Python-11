#frequency of words in a sentence
import json
sent=input("Enter the sentence(s) :")
d={}
word=sent.split()
for i in word:
    key=i
    if key not in d:
        count=word.count(key)
        d[key]=count
print("Given sentence(s) is : ",sent)
print(json.dumps(d,indent=0))
