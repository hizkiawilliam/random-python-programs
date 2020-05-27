count = float(0)
f = open('DNA.txt','r')
text = str(f.read())
print("DNA data : ",text)
f.close()
for i in text:
    if i=="C" or i=="G":
        count +=1
percent = float(count/len(text)*100)
print("The percentage of C+G in the DNA is : {0:.2f}%".format(percent))
