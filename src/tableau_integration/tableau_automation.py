import yaml
import os
import tableauserverclient as TSC
import getpass
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def load_tableau_config():
    """
    Loads Tableau credentials (server URL, username, site ID) from a YAML configuration file.

    Returns:
        dict: A dictionary containing the Tableau server URL, username, and site ID.
    """
    config_path = os.path.join(os.path.dirname(__file__), '../config/tableau_config.yaml')
    with open(config_path, 'r') as file:
        return yaml.safe_load(file)


# Load Tableau config (server_url, username, site_id)
tableau_config = load_tableau_config()

TABLEAU_SERVER_URL = tableau_config['server_url']
USERNAME = tableau_config['username']
SITE_ID = tableau_config.get('site_id', '')

# Prompt user for their password
PASSWORD = getpass.getpass(prompt='Enter your Tableau password: ')


def authenticate_tableau():
    """
    Authenticates to Tableau Server using the username, password, and site ID.

    Returns:
        tuple: A tuple containing the TableauAuth object and the Server object.
    """
    tableau_auth = TSC.TableauAuth(USERNAME, PASSWORD, SITE_ID)
    server = TSC.Server(TABLEAU_SERVER_URL, use_server_version=True)
    return tableau_auth, server


def list_workbooks():
    """
    Lists all available workbooks on Tableau Server.

    Logs the workbook name, ID, and project name for each workbook.
    """
    logger.info("Fetching all available workbooks...")
    tableau_auth, server = authenticate_tableau()

    with server.auth.sign_in(tableau_auth):
        all_workbooks, pagination_item = server.workbooks.get()

        for workbook in all_workbooks:
            logger.info(f"Workbook: {workbook.name}, ID: {workbook.id}, Project: {workbook.project_name}")


def refresh_extract(workbook_name):
    """
    Refreshes the extract for a specific workbook.

    Args:
        workbook_name (str): The name of the workbook to refresh.

    Logs the result of the extract refresh.
    """
    logger.info(f"Starting extract refresh for workbook: {workbook_name}")
    tableau_auth, server = authenticate_tableau()

    with server.auth.sign_in(tableau_auth):
        all_workbooks, pagination_item = server.workbooks.get()

        workbook = next((wb for wb in all_workbooks if wb.name == workbook_name), None)
        if not workbook:
            logger.error(f"Workbook {workbook_name} not found!")
            return

        logger.info(f"Found workbook: {workbook.name}, refreshing extract...")

        # Trigger the extract refresh
        server.workbooks.refresh(workbook)
        logger.info(f"Successfully triggered extract refresh for {workbook_name}")


def publish_workbook(workbook_path, project_name):
    """
    Publishes a workbook to Tableau Server.

    Args:
        workbook_path (str): The path to the workbook file (e.g., .twbx file).
        project_name (str): The name of the project on Tableau Server to publish the workbook to.

    Logs the result of the workbook publication.
    """
    logger.info(f"Publishing workbook from {workbook_path} to project {project_name}")
    tableau_auth, server = authenticate_tableau()

    with server.auth.sign_in(tableau_auth):
        all_projects, pagination_item = server.projects.get()
        project = next((proj for proj in all_projects if proj.name == project_name), None)
        if not project:
            logger.error(f"Project {project_name} not found!")
            return

        # Create the new workbook item
        new_workbook = TSC.WorkbookItem(project_id=project.id)

        # Publish the workbook
        with open(workbook_path, 'rb') as workbook_file:
            server.workbooks.publish(new_workbook, workbook_file, TSC.Server.PublishMode.Overwrite)

        logger.info(f"Workbook published successfully to project {project_name}")


def download_workbook(workbook_name, download_path):
    """
    Downloads a specific workbook from Tableau Server.

    Args:
        workbook_name (str): The name of the workbook to download.
        download_path (str): The local directory where the workbook will be saved.

    Logs the path where the workbook was downloaded.
    """
    logger.info(f"Downloading workbook: {workbook_name}")
    tableau_auth, server = authenticate_tableau()

    with server.auth.sign_in(tableau_auth):
        all_workbooks, pagination_item = server.workbooks.get()

        workbook = next((wb for wb in all_workbooks if wb.name == workbook_name), None)
        if not workbook:
            logger.error(f"Workbook {workbook_name} not found!")
            return

        file_path = os.path.join(download_path, f"{workbook_name}.twbx")
        server.workbooks.download(workbook.id, filepath=file_path)

        logger.info(f"Workbook {workbook_name} downloaded to {file_path}")


def delete_workbook(workbook_name):
    """
    Deletes a specific workbook from Tableau Server.

    Args:
        workbook_name (str): The name of the workbook to delete.

    Logs whether the workbook was successfully deleted or not.
    """
    logger.info(f"Attempting to delete workbook: {workbook_name}")
    tableau_auth, server = authenticate_tableau()

    with server.auth.sign_in(tableau_auth):
        all_workbooks, pagination_item = server.workbooks.get()

        workbook = next((wb for wb in all_workbooks if wb.name == workbook_name), None)
        if not workbook:
            logger.error(f"Workbook {workbook_name} not found!")
            return

        server.workbooks.delete(workbook.id)
        logger.info(f"Workbook {workbook_name} has been deleted")


def get_workbook_connections(workbook_name):
    """
    Retrieves data connection details for a specific workbook.

    Args:
        workbook_name (str): The name of the workbook to retrieve connections for.

    Logs each data connection's details (e.g., datasource name, type, server address).
    """
    logger.info(f"Retrieving data connections for workbook: {workbook_name}")
    tableau_auth, server = authenticate_tableau()

    with server.auth.sign_in(tableau_auth):
        all_workbooks, pagination_item = server.workbooks.get()

        workbook = next((wb for wb in all_workbooks if wb.name == workbook_name), None)
        if not workbook:
            logger.error(f"Workbook {workbook_name} not found!")
            return

        connections, pagination_item = server.workbooks.connections(workbook)

        for connection in connections:
            logger.info(
                f"Connection: {connection.datasource_name}, Type: {connection.datasource_type}, Server: {connection.server_address}")


def add_user_to_project(username, project_name):
    """
    Adds a user to a specific project on Tableau Server.

    Args:
        username (str): The username of the user to add.
        project_name (str): The name of the project to add the user to.

    Logs whether the user was successfully added to the project or not.
    """
    logger.info(f"Adding user {username} to project {project_name}")
    tableau_auth, server = authenticate_tableau()

    with server.auth.sign_in(tableau_auth):
        all_users, pagination_item = server.users.get()
        user = next((u for u in all_users if u.name == username), None)
        if not user:
            logger.error(f"User {username} not found!")
            return

        all_projects, pagination_item = server.projects.get()
        project = next((proj for proj in all_projects if proj.name == project_name), None)
        if not project:
            logger.error(f"Project {project_name} not found!")
            return

        # Add user to project (role: Viewer)
        server.projects.add_user(project, user, role='Viewer')
        logger.info(f"User {username} added to project {project_name} as Viewer")


def publish_datasource(datasource_path, project_name):
    """
    Publishes a data source to Tableau Server.

    Args:
        datasource_path (str): The path to the data source file.
        project_name (str): The name of the project to publish the data source to.

    Logs the result of the data source publication.
    """
    logger.info(f"Publishing data source from {datasource_path} to project {project_name}")
    tableau_auth, server = authenticate_tableau()

    with server.auth.sign_in(tableau_auth):
        all_projects, pagination_item = server.projects.get()
        project = next((proj for proj in all_projects if proj.name == project_name), None)
        if not project:
            logger.error(f"Project {project_name} not found!")
            return

        # Create the new data source item
        new_datasource = TSC.DatasourceItem(project_id=project.id)

        # Publish the data source
        with open(datasource_path, 'rb') as datasource_file:
            server.datasources.publish(new_datasource, datasource_file, TSC.Server.PublishMode.Overwrite)

        logger.info(f"Data source published successfully to project {project_name}")


def check_server_status():
    """
    Checks the status and version information of the Tableau Server.

    Logs the server version and build number.
    """
    logger.info("Checking Tableau Server status...")
    tableau_auth, server = authenticate_tableau()

    with server.auth.sign_in(tableau_auth):
        server_info = server.server_info.get()
        logger.info(f"Tableau Server version: {server_info.version}")
        logger.info(f"Product build: {server_info.build_number}")


# Example usage
if __name__ == '__main__':
    # Refresh extract for a workbook
    refresh_extract('Sales Dashboard')