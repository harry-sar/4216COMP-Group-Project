import flightTourismDataLoader
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
            countryChoice=input("Enter Valid Country")
            print(flightTourismDataLoader.outputSpecificCountryData(countryChoice,
                                flightTourismDataLoader.load_tourism_data()))




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