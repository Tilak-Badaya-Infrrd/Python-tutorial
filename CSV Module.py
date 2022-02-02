import csv

with open('names.csv','r') as csv_file:
    csv_reader = csv.reader(csv_file)
    
    for line in csv_reader:
        print(line)
        
    for line in csv_reader:
        print(line[2])
        
    with open('new_names_csv' , 'w') as new_file:
        csv_writer = csv.writer(new_file, delimiter='-')
        
    for line in csv_reader:
        csv_writer.writerow(line)
        
    csv_reader = csv.DictReader(csv_file)
    
    for line in csv_reader:
        print(line)
