import yaml
import os

CONFIG_PATH = os.path.join(os.path.dirname(__file__), '..', 'config', 'tableau_config.yaml')


def load_config():
    """Load the existing configuration if it exists, otherwise return an empty dictionary."""
    if os.path.exists(CONFIG_PATH):
        with open(CONFIG_PATH, 'r') as file:
            return yaml.safe_load(file)
    return {}


def save_config(config):
    """Save the updated configuration to the tableau_config.yaml file."""
    with open(CONFIG_PATH, 'w') as file:
        yaml.dump(config, file)


def prompt_for_server_url(config):
    """Prompt the user to update the Tableau server URL."""
    server_url = input(f"Enter new Server URL [{config.get('server_url', 'not set')}]: ") or config.get('server_url')
    config['server_url'] = server_url
    return config


def prompt_for_username(config):
    """Prompt the user to update the Tableau username."""
    username = input(f"Enter new Username [{config.get('username', 'not set')}]: ") or config.get('username')
    config['username'] = username
    return config


def prompt_for_site_id(config):
    """Prompt the user to update the Tableau site ID."""
    site_id = input(f"Enter new Site ID [{config.get('site_id', 'not set')}]: ") or config.get('site_id')
    config['site_id'] = site_id
    return config


def update_all(config):
    """Prompt the user to update all credentials."""
    config = prompt_for_server_url(config)
    config = prompt_for_username(config)
    config = prompt_for_site_id(config)
    return config


def display_menu(continuation=False):
    """Display the main menu for updating the configuration."""
    print("\nTableau Configuration Menu")
    print("1. Update Server URL")
    print("2. Update Username")
    print("3. Update Site ID")
    print("4. Update All Values")
    if continuation:
        print("5. Continue")
    else:
        print("5. Exit")


def main(continuation=False):
    config = load_config()  # Load the existing config if available

    while True:
        display_menu(continuation)
        choice = input("Choose an option (1-5): ").strip()

        if choice == '1':
            config = prompt_for_server_url(config)
            save_config(config)
            print("Server URL updated successfully.")
        elif choice == '2':
            config = prompt_for_username(config)
            save_config(config)
            print("Username updated successfully.")
        elif choice == '3':
            config = prompt_for_site_id(config)
            save_config(config)
            print("Site ID updated successfully.")
        elif choice == '4':
            config = update_all(config)
            save_config(config)
            print("All values updated successfully.")
        elif choice == '5':
            if continuation:
                print("Exiting Tableau configuration menu.")
            else:
                print("Exiting configuration.")
            break
        else:
            print("Invalid choice, please try again.")

    print(f"\nFinal configuration saved to {CONFIG_PATH}")
    print(f"Server URL: {config.get('server_url', 'not set')}")
    print(f"Username: {config.get('username', 'not set')}")
    print(f"Site ID: {config.get('site_id', 'not set')}")


if __name__ == "__main__":
    main()