# -----------------------------------------------------------------------------------------
# Import
from src.providerData.ReaderFromFile import ReaderFromFile
# -----------------------------------------------------------------------------------------
# Constant

# -----------------------------------------------------------------------------------------
# Code

def main():
    test = ReaderFromFile (2, "./data/", "test.txt")
    test.get_points()
    print(test.listPoints)

main()
