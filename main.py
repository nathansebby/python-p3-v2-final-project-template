from lib.cli import main_menu
from lib.models import Team, Jersey

if __name__ == "__main__":
   
    Team.create_table()
    Jersey.create_table()
    
    print("\nWelcome to the Team!")
    main_menu()
