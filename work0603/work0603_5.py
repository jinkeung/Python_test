import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")
flight=sns.load_dataset("flights")
year=flight.year
passengers=flight.passengers

sns.barplot(data=passengers,x=year,y=passengers)
plt.show()

sns.barplot(x="year",y="passengers",data=flight)
plt.show()


flight=sns.load_dataset("flights").groupby("year")["passengers"].mean().reset_index()
print(flight)
sns.barplot(x=year,y=passengers,data=flight)
plt.show()