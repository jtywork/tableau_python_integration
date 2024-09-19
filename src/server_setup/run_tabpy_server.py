import os
from subprocess import Popen


def run_tabpy_server():
    """Run the TabPy server."""

    try:
        # Check if TabPy is installed
        import tabpy
    except ImportError:
        print("TabPy is not installed. Installing now...")
        os.system('pip install tabpy')

    # Set the path for TabPy
    tabpy_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'venv', 'lib', 'site-packages',
                              'tabpy', 'tabpy_server')

    print("Starting TabPy server...")

    # Launch the TabPy server as a subprocess
    Popen(['python', '-m', 'tabpy'], cwd=tabpy_path)

    print("TabPy server is running. You can connect Tableau to it now.")


if __name__ == "__main__":
    run_tabpy_server()