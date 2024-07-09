players_seats = [
    ["Michael Jordan", "LeBron James", "Shaquille O'neill", "Magic Johnson", "Stephen Curry", "Kevin Durant"],
    ["Roger Federer", "Rafael Nadal", "Novak Djokovic", "Pete Sampras", "Andre Agassi"],
    ["Serena Williams", "Steffi Graf", "Martina Navratilova", "Venus Williams", "Chris Evert", "Monica Seles"],
    ["Tom Brady", "Patrick Mahomes", "Aaron Donald", "Peyton Manning", "Rob Gronkowski", "Alan Page"],
]

# printing players seatings

for i, row in enumerate(players_seats):
    for j, players in enumerate(row):
        print(f" {players} is seating in row {i+1}, seat {j+1}")