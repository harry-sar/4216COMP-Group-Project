import flightTourismDataLoader
import matplotlib.pyplot as plt

def DailyOvernightVis():
    input_values = [1, 2, 3, 4, 5]
    squares = [1, 4, 9, 16, 25]
    daData=[] # in the form overnight,same day
    daList=[c for c in flightTourismDataLoader.load_tourism_data()["Country"]]
    daList=list(set(daList))
    tourismDatas=flightTourismDataLoader.load_tourism_data()

    tourismOvernight=tourismDatas["overnightStay"]
    tourismDaily=tourismDatas["SameDay"]


    print(daList,"::",daData,"\n")
    fig, ax = plt.subplots(figsize=(8,8)) #sameday:overnight
    fig.suptitle("Difference between Overnight visitors and same day visitors", fontsize=18)
    ax.set_title("Sameday:Overnight visitors", fontsize=14)
    ax.set_xlabel("Same Day")
    ax.set_ylabel("Overnight")
    ax.scatter(tourismDaily,tourismOvernight)
    ax.legend()
    plt.show()



if '__main__'==__name__:
    DailyOvernightVis()