from Functions.Testing import *
from lab2.FordFulkerson import *
from lab2.ConectivityFordFelcurson import *

if __name__ == "__main__":
    # testing Ford–Fulkerson by sample graphs
    print("Flow test")
    testing(FordFulkersonWraper, "Flow")
    print("_______________________________")
    # testing Ford-Fulkerson to connectivity check
    print("connectivity check")
    testing(Connectivity, "connectivity")
    print("_______________________________")
