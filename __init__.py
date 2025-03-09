from .database import Database  # Import database normally
from .config import DATABASE_NAME, LOAN_DAYS  # Import config settings

# Try importing Library only if there’s no circular import
try:
    from .library import Library
except ImportError:
    pass  # Avoid breaking the package if there's a circular dependency


# Delay CLI import until runtime
def get_cli():
    from .cli import main

    return main
