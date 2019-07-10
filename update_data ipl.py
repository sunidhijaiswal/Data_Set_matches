import csv
teams_play = []
total_played = []
winner = []
x = {}

def recur_data(p):
    for row in p:
        if p == reader:
            teams_play.append(row[4])
            total_played.append(row[4])
            total_played.append(row[5])
            winner.append(row[10])

        else:
            x[row] = {"Total_played": total_played.count(row), "won": winner.count(row),
                                        "lost": total_played.count(row) - winner.count(row)}



def show():
    teams_play.remove('team1')
    recur_data(teams_play)
    print(x)

with open('matches.csv', 'r') as file:
    reader = csv.reader(file)
    recur_data(reader)
    show()
file.close()

