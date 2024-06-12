from lib.cli import main_menu
from lib.models import Team, Jersey

if __name__ == "__main__":
    # Create tables if they don't exist
    Team.create_table()
    Jersey.create_table()
    
    # Start the CLI
    main_menu()
