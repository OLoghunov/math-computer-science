import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from kalman_filter.main import main
if __name__ == "__main__":
    """
    A wrapper script for running the Kalman filter. 
    You can configure the filter in the kamlan_filter.main file.
    """
    main()