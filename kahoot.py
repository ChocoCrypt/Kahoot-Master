from sys import argv
from kahoot_player_class import *


if __name__ == "__main__":
    if(len(argv) == 4):
        code = str(argv[1])
        name = str(argv[2])
        number_threads = str(argv[3])
        kahoot = Kahoot_Master(code , number_threads , name)
        kahoot.parallel_tentacle()
    else:
        print("Usage: \n python3 <kahoot code> <name> <number of threads>")
