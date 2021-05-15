import csv
import os
import shutil
from tempfile import NamedTemporaryFile

def view():
    try:
        liste_offres = []
        with open('jobs.csv', 'r') as file:
            reader = csv.reader(file, delimiter=';')
            for item in reader:
                if len(item) > 1:
                    liste_offres.append(item)
        return liste_offres
    except :
        return "There are no offers available at the moment"

def insert(id_job, society, adress, e_mail, profile, mission):
    with open('jobs.csv', 'a') as file:
        job_writer = csv.writer(file, delimiter = ';', quotechar = '|')
        if os.stat('jobs.csv').st_size == 0:
            job_writer.writerow(['ID_job', 'society', 'adress', 'e_mail', 'profile', 'mission'])
        job_writer.writerow([id_job, society, adress, e_mail, profile, mission])

def delete(id_job):
    try:
        lines = list()
        with open('jobs.csv', 'r') as readFile:
            reader = csv.reader(readFile, delimiter=';')
            for row in reader:
                lines.append(row)
                for field in row:
                    if field == id_job:
                        lines.remove(row)
        print(lines)
        with open('jobs.csv', 'w') as writeFile:
            writer = csv.writer(writeFile, delimiter=';')
            writer.writerows(lines)
        return 1                 
    except : 
        return "Such offer doesn't exist"

def update(id_job, society, adress, e_mail, profile, mission):
    try:
        fields = ['ID_job', 'society', 'adress', 'e_mail', 'profile', 'mission']
        tempfile = NamedTemporaryFile(mode='w', delete=False)
        with open('jobs.csv', 'r') as file, tempfile:
            reader = csv.DictReader(file, fieldnames=fields, delimiter=';')
            writer = csv.DictWriter(tempfile, fieldnames=fields, delimiter=';')
            for row in reader:
                for field in row:
                    if field == id_job:
                        row['society'], row['adress'], row['e_mail'], row['profile'], row['mission'] = society, adress, e_mail, profile, mission
                row = {'ID_job' : row['ID_job'], 'society' : row['society'], 'adress' : row['adress'], 'e_mail' : row['e_mail'], 'profile' : row['profile'], 'mission' : row['mission']}
                writer.writerow(row)
        shutil.move(tempfile, 'jobs.csv')
        return 1                    
    except : 
        return "Such offer doesn't exist"



# print(insert('0123', 'hello', 'yahayh', '@lala', 'zbeybi', 'adsqdds'))
# print(update('0123', 'sdqsdds', 'rzrfsf', "qsfsfqs", 'qsffqsfqsf', 'sqfqsd'))
# print(view())
