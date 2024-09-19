!!!THIS IS NOT READY FOR USE YET!!!

!!! WARNING !!!

# tableau_python_integration
For exploring the use of python's functionalities within Tableau.

# Repo Plan & Structure: 
	•	src/: Contains all the Python source code, divided into different functional areas (e.g., tableau_integration, server_setup).
	•	config/: Contains configuration files for different environments and settings specific to Tableau.
	•	tests/: Includes unit tests for the various modules in the repo.
	•	docker/: Includes files for Dockerizing your app and creating a reproducible environment.
	•	scripts/: Contains shell scripts for automating tasks like server setup, deployment, or resource cleanup.
	•	docs/: Holds all project documentation for developers and users.

```
tableau_python_integration/
	│
	├── README.md                  # Overview of the repo, setup instructions, usage.
	├── requirements.txt           # Python dependencies.
	├── .gitignore                 # Ignore unnecessary files for version control.
	├── LICENSE                    # License for the project (optional).
	├── setup.py                   # Setup script for packaging if needed.
	│
	├── src/                       # Main source code folder.
	│   ├── __init__.py            # Makes it a package.
	│   ├── tableau_integration/   # Python scripts for Tableau interaction.
	│   │   ├── __init__.py
	│   │   ├── data_preprocessing.py   # For preprocessing data before passing to Tableau.
	│   │   ├── tableau_connector.py    # Scripts for connecting and pushing data to Tableau.
	│   │   └── tableau_automation.py   # Automating Tableau tasks with Python.
	│   │
	│   ├── server_setup/          # Scripts related to server setup & interaction.
	│   │   ├── __init__.py
	│   │   ├── create_virtual_server.py 	# Script for spinning up virtual servers.
	│   │   ├── config.py              		# Server configuration settings.
	│   │   ├── run_tabpy_server.py         # Stands up TabPy server.
	│   │   └── server_monitoring.py    	# Monitor server health, status checks.
	│   │
	│   └── utils/                 # Helper utility scripts (generic helpers).
	│       ├── __init__.py
	│       ├── logging_util.py        	# Utilities for logging.
	│       ├── config_loader.py       	# Config loading/parsing.
	│       ├── error_handling.py      	# Custom error handling utilities.
	│       └── configure_tableau.py	# Config tableau server access.
	│
	├── config/                    # Configuration files for various environments.
	│   ├── dev_config.yaml        # Development config.
	│   ├── prod_config.yaml       # Production config.
	│   ├── tableau_config.yaml    # Tableau-specific configurations.
	│   └── tabpy_config.conf
	│
	├── tests/                     # Test suite for the repo.
	│   ├── __init__.py
	│   ├── test_tableau_integration.py   # Unit tests for Tableau integration.
	│   ├── test_server_setup.py          # Unit tests for server setup.
	│   └── test_utils.py                 # Unit tests for utility scripts.
	│
	├── docker/                    # Docker files to containerize your environment.
	│   ├── Dockerfile             # Dockerfile to create the container image.
	│   └── docker-compose.yml     # Docker Compose setup for the project.
	│
	├── scripts/                   # Bash/other scripts for automation.
	│   ├── start_server.sh        # Shell script to start virtual server.
	│   ├── deploy.sh              # Shell script to deploy the application.
	│   └── cleanup.sh             # Cleanup script for resources.
	│
	└── docs/                      # Documentation for the project.
		├── api_docs.md            # API/Integration documentation for Tableau.
		├── server_docs.md         # Documentation for server setup and configuration.
		└── troubleshooting.md     # Common issues and troubleshooting.
```


## Running the TabPy Server
To run the TabPy server for Tableau integration, we provide a script that simplifies the process. You can choose to run the server with default settings or with a custom configuration.

### Basic Usage:
To run the TabPy server with the default configuration, use:
```bash
python src/server_setup/run_tabpy_server.py
```

### Advanced Usage:
If you want to specify a custom configuration file, use the --config option:
```bash
python src/server_setup/run_tabpy_server.py --config config/tabpy_config.conf
```

### Stopping the Server
Since the TabPy server is started as a background process, you can stop it manually by finding its process ID and killing it, or by closing the terminal session.