import flightTourismDataLoader
import ryanVis
class menuObj():

    def __init__(self):
       self.choice=None


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




    def checkData(self,dataToSearch):
        quit(0)
        # so dataToSearch is the data you are looking for within the csv or internal JSON data files
        # search this for the required data
        # with open('cachedFlightData.csv') as f:
        #     csvReader = csv.reader(f)


    def visualiseData(self):
        quit(0)
        # placeholder function for all visualisations later on.

if __name__=="__main__":
    MenuObj=menuObj()
    MenuObj.displayMenu()