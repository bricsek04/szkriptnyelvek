#Haladó sztringformázás

def main():   
    players = [
        ['Max Verstappen', 'Red Bull', 2015, 412],
        ['Lando Norris', 'McLaren', 2019, 310],
        ['Lewis Hamilton', 'Mercedes', 2007, 358],
        ['Charles Leclerc', 'Ferrari', 2019, 285],
        ['George Russell', 'Mercedes', 2019, 275],
        ['Carlos Sainz', 'Ferrari', 2015, 260],
    ]

    print(f"| {'Player':<16} | {'TEAM':<9} | {'JOINED':>6} | {'PTS':>3} |")
    print(f"|{'-'*18}|{'-'*11}|{'-'*8}|{'-'*5}|")

    for name, team, joined, pts in players:
        print(f"| {name:<16} | {team:<9} | {joined:6d} | {pts:3d} |")

if __name__ == "__main__":
    main()