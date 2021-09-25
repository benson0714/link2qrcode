import selenium
import csv
import random
    
with open('list_of_bot.csv','w') as file:
    fieldnames = ['姓名','帳號','密碼']
    rows = csv.DictWriter(file,fieldnames = fieldnames)
    rows.writeheader()
    count = 0
    print(count)
    with open('random_name.txt','r') as random_name_file:
        allName = random_name_file.read()
        names = list(map(str, allName.split()))
        while count<10:
            count+=1
            print(random.choice(names))
            rows.writerow({'姓名':153,'帳號':234,'密碼':345})  
            
