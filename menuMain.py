import flightTourismDataLoader
import harryVis, ryanVis
class menuObj():

    def __init__(self):
       self.choice=None
       self.api_key="018ec34c-8a03-4cd6-aa66-026d1a0385cf"

    def displayMenu(self):
        ''' Main menu Console display '''
        print("----------------------------\n"
              "Flight & Tourism Data Menu\n"
              "----------------------------")
        print("[1] Output Singular Flight")
        print("[2] Output All Flights")
        print("[3] Output Country data for Specific Country")
        print("[4] Output Visualisations")
        self.userCheck=input()
        if self.userCheck not in ["1","2","3","4"]:
            print("Try Again, Invalid Data!")
            self.displayMenu()
        elif self.userCheck=="1":
            flightTourismDataLoader.load_specific_flight(flightTourismDataLoader.load_cached_flight_data())
        elif self.userCheck=="2":
            print(flightTourismDataLoader.load_all_flights(flightTourismDataLoader.load_cached_flight_data()))
        elif self.userCheck=="3":
            countryChoice=input("Enter Valid Country")
            print(flightTourismDataLoader.outputSpecificCountryData(countryChoice,
                                flightTourismDataLoader.load_tourism_data()))
        elif self.userCheck=="4":
            self.pickVis()

    def pickVis(self):
        try:
            pickVis = int(input("----------------------------\n"
                            "   Select Visualisation\n"
                            "----------------------------\n"
                            "[1] Ryan's Visualisation\n"
                            "[2] Harry's Visualisation\n"
                            "[3] Aisling's Visualisation\n"
                            "[4] Michael's Visualisation\n"
                            "[5] Callum's Visualisation\n"
                            ">> "))
            if pickVis == 1:
                ryanVis.ryanNumOfFlightsVis()
                ryanVis.ryanScatterMapEU()
            elif pickVis == 2:
                harryVisObj=harryVis.harrysVis()
                harryVisObj.initaliseGraphAnalysis(True,self.api_key,flightTourismDataLoader.load_tourism_data(),True)
                harryVisObj.mapLiveFlights(self.api_key,True,"uk",True)
            elif pickVis ==3:
                quit(0)
            elif pickVis ==4:
                quit(0)
            elif pickVis ==5:
                quit(0)
            elif pickVis not in [1,2,3,4,5]:
                print("Invalid data")
                self.pickVis()
        except:
            print("Invalid data")
            self.pickVis()
if __name__=="__main__":
    MenuObj=menuObj()
    MenuObj.displayMenu()