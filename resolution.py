import csv
with open('patient_data.csv', newline='') as csvfile:
  text = csv.reader(csvfile)
  print(text)
