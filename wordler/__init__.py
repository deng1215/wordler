
import os 

FIXED = 2
FLOATING = 1
FORBIDDEN = 0

DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "data")
LOGO_PATH = os.path.join(os.path.dirname(__file__), "..", "logo_futura.png")


from .solver import Wordler
