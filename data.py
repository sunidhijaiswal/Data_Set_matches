import csv

teams = []
total_played = []
winner = []
x={}

# Read csv file matches.csv

with open('matches.csv', 'r') as file:
    reader = csv.reader(file)

    for row in reader:
        teams.append(row[4])
        total_played.append(row[4])
        total_played.append(row[5])
        winner.append(row[10])

file.close()
#filter common names teams
teams = set(teams)
#convert into dict
for i in teams:
    x[i] = {"Total_played": total_played.count(i), "won": winner.count(i), "lost": total_played.count(i) - winner.count(i)}

print(d)
