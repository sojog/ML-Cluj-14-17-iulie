import csv

csv_text = """,culori,valori
0,alb,11.0
1,negru,22.0
2,rosu,33.0
3,verde,44.0
4,mov,55.0
5,blue,66.0
6,galben,77.0"""


csv_result_reader = csv.DictReader(csv_text, delimiter=",")
for line in csv_result_reader:
    print(line)