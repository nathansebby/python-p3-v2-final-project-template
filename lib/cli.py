from lib.models import Team, Jersey

def main_menu():
    while True:
        print("\nMain Menu")
        print("1. Manage Teams")
        print("2. Manage Jerseys")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            manage_teams()
        elif choice == '2':
            manage_jerseys()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

def manage_teams():
    while True:
        print("\nTeam Menu")
        print("1. Create Team")
        print("2. View All Teams")
        print("3. Find Team by ID")
        print("4. Delete Team")
        print("5. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            create_team()
        elif choice == '2':
            view_all_teams()
        elif choice == '3':
            find_team_by_id()
        elif choice == '4':
            delete_team()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")
            pass

def manage_jerseys():
    while True:
        print("\nJersey Menu")
        print("1. Create Jersey")
        print("2. View All Jerseys")
        print("3. Find Jersey by ID")
        print("4. Delete Jersey")
        print("5. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            create_jersey()
        elif choice == '2':
            view_all_jerseys()
        elif choice == '3':
            find_jersey_by_id()
        elif choice == '4':
            delete_jersey()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

def create_team():
    name = input("Enter team name: ")
    city = input("Enter team city: ")
    mascot = input("Enter team mascot: ")
    team = Team(name=name, city=city, mascot=mascot)
    team.save()
    print("Team created successfully!")

def view_all_teams():
    teams = Team.get_all()
    for team in teams:
        print(team)

def find_team_by_id():
    team_id = input("Enter team ID: ")
    team = Team.find_by_id(team_id)
    if team:
        print(team)
    else:
        print("Team not found.")

def delete_team():
    team_id = input("Enter team ID: ")
    Team.delete(team_id)
    print("Team deleted successfully!")

def create_jersey():
    player_name = input("Enter player name: ")
    number = input("Enter jersey number: ")
    size = input("Enter jersey size: ")
    color = input("Enter jersey color: ")
    team_id = input("Enter team ID: ")
    jersey = Jersey(player_name=player_name, number=number, size=size, color=color, team_id=team_id)
    jersey.save()
    print("Jersey created successfully!")

def view_all_jerseys():
    jerseys = Jersey.get_all()
    for jersey in jerseys:
        print(jersey)

def find_jersey_by_id():
    jersey_id = input("Enter jersey ID: ")
    jersey = Jersey.find_by_id(jersey_id)
    if jersey:
        print(jersey)
    else:
        print("Jersey not found.")

def delete_jersey():
    jersey_id = input("Enter jersey ID: ")
    Jersey.delete(jersey_id)
    print("Jersey deleted successfully!")
