import flightTourismDataLoader
class menuObj():

    def __init__(self):
       self.choice=None


    def displayMenu(self,UserSelect):
        ''' Main menu Console display '''
        print("----------------------------\n"
              "Flight & Tourism Data Menu\n"
              "----------------------------")
        print("1 - Current Flights") #HarryVis
        print("2 - Airport Usage Graph") #AislingVis
        print("3 - Popular Tourist Destinations") #CallumVis
        print("4 - Airspace Density Heatmap") #RyanVis
        print("5 - Flight Trends") #MichaelVis

        if UserSelect in ["1"]:
            self.checkData(currentFlights)

        if UserSelect in ["2"]:
            self.checkData(airportUsage)

        if UserSelect in ["3"]:
            self.checkData(touristDest)

        if UserSelect in ["4"]:
            self.checkData(airspaceDens)

        if UserSelect in ["5"]:
            self.checkData(flightTrends)


    def checkData(self,dataToSearch):
        quit(0)
        # so dataToSearch is the data you are looking for within the csv or internal JSON data files
        # search this for the required data
        with open('cachedFlightData.csv') as f:
            csvReader = csv.reader(f)


    def visualiseData(self):
        quit(0)
        # placeholder function for all visualisations later on.

if __name__=="__main__":
    MenuObj=menuObj()
    menuObj.displayMenu()