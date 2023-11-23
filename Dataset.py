Dataset = {1:['kiran','3BR21AI020','AIML','20',],
            2:['3BR21AI020','3BR21AI014','3BR21AI013','3BR21AI009','3BR21AI035'],
            3:['AIML','AIML','AIML','AIML','AIML'],
            4:['20','20','21','19','21'],
            5:['20','14','13','9','35']
        }

print("{:<10} {:<10} {:<10} {:<10} {:<10}".format('NAME','USN','BRANCH',"AGE","ROLLNO"))

for key,value in Dataset.items():
    NAME,USN,BRANCH,AGE,ROLLNO = value
    print("{:<10} {:<10} {:<10} {:<10} {:<10}".format(NAME,USN,BRANCH,AGE,ROLLNO))

