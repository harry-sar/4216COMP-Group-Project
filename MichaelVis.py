import flightTourismDataLoader
import matplotlib.pyplot as plt

def DailyOvernightVis():
    daData=[] # in the form overnight,same day
    daList=[c for c in flightTourismDataLoader.load_tourism_data()["Country"]]
    daList=list(set(daList))
    tourismDatas=flightTourismDataLoader.load_tourism_data()

    tourismOvernight=tourismDatas["overnightStay"]
    tourismDaily=tourismDatas["SameDay"]


    fig, ax = plt.subplots(figsize=(8,8)) #sameday:overnight
    fig.suptitle("Difference between Overnight visitors and same day visitors", fontsize=18)
    ax.set_title("Sameday:Overnight visitors", fontsize=14)
    ax.set_xlabel("Same Day")
    ax.set_ylabel("Overnight")
    ax.scatter(tourismDaily,tourismOvernight)
    plt.show()

if '__main__'==__name__:
    DailyOvernightVis()