"""
Wimbledon
Estimated: 2 hours
Actual: 1 hour 30 minutes
"""
import csv


def main():
    """a program that displays winners of wimbledon and there country"""
    winners = []
    winner_to_wins = {}
    filename = "wimbledon.csv"
    with open(filename, 'r', encoding="utf-8-sig") as in_file:
        get_winners(in_file, winners)
        countries = get_number_of_wins(winner_to_wins, winners)
        display_winners(countries, winner_to_wins)


def display_winners(countries, winner_to_wins):
    """Print the winners country."""
    print("Wimbledon Champions: ")
    for winner in winner_to_wins:
        print(winner, winner_to_wins[winner])
    print(f"These {len(countries)} have won Wimbledon:")
    print(", ".join(country for country in sorted(countries)))


def get_number_of_wins(winner_to_wins, winners):
    """Calculate the number of wins each winner has."""
    countries = set()
    for winner in winners:
        countries.add(winner[1])
        try:
            winner_to_wins[winner[2]] += 1
        except KeyError:
            winner_to_wins[winner[2]] = 1
    return countries


def get_winners(in_file, winners):
    """Get each winner from file"""
    in_file.readline()
    for line in in_file:
        parts = line.strip().split(",")
        winners.append(parts)


main()
