import MichaelVis
import CallumsVisualisation
import flightTourismDataLoader
import harryVis, ryanVis, AislingVis
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
            quit(0)

    def pickVis(self):
        try:
            pickVisC = int(input("----------------------------\n"
                            "   Select Visualisation\n"
                            "----------------------------\n"
                            "[1] Ryan's Visualisation\n"
                            "[2] Harry's Visualisation\n"
                            "[3] Aisling's Visualisation\n"
                            "[4] Michael's Visualisation\n"
                            "[5] Callum's Visualisation\n"
                            ">> "))
            if pickVisC == 1:
                ryanVis.ryanNumOfFlightsVis()
                ryanVis.ryanScatterMapEU()
            elif pickVisC == 2:
                harryVisObj = harryVis.harrysVis()

                self.cacheSelect=input("please enter [true|false] do you want to use cached data? >>")

                if self.cacheSelect in ["true","false"]:
                    self.cacheSelect=self.cacheSelect.lower() in ["true"]
                    harryVisObj.initaliseGraphAnalysis(self.cacheSelect, self.api_key,flightTourismDataLoader.load_tourism_data(), True)
                self.overlaySelect=input("Please enter place to map [world|uk] >>")
                if self.overlaySelect.lower() in ["uk","world"]:
                    harryVisObj.mapLiveFlights(self.api_key,self.cacheSelect,self.overlaySelect,True)

                if self.overlaySelect.lower() not in ["uk","world"]:
                    print("Invalid Data!, Try Again.")
                    self.pickVis()
            elif pickVisC ==3:
                AislingVis.RunVis()
            elif pickVisC ==4:
                MichaelVis.DailyOvernightVis()
            elif pickVisC ==5:
                CallumsVisualisation.touristsvis()
            elif pickVisC not in [1,2,3,4,5]:
                print("Invalid data")
                self.pickVis()
                quit(0)
        except:
            print("Invalid data")
            self.pickVis()
            quit(0)
if __name__=="__main__":
    MenuObj=menuObj()
    MenuObj.displayMenu()