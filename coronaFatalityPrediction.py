import numpy as np
import matplotlib.pyplot as plt

txtAgeGroups = ["0-19","20-29","30-59","60-79","80+"]
deathsPerAge = [2,6,265,1995,4010]                              #source: https://de.statista.com/statistik/daten/studie/1104173/umfrage/todesfaelle-aufgrund-des-coronavirus-in-deutschland-nach-geschlecht/ (4.5.2020)
ageDistribution = [15294000,9801000,34547000,17988000,5389000]  #source: https://www.deutschlandinzahlen.de/tab/deutschland/demografie/bevoelkerung-nach-altersklassen-deutschland (4.5.2020)
totalFatalityRate = 0.0037                                      #source: https://www.n-tv.de/wissen/Heinsberg-Studie-entraetselt-Coronavirus-article21704605.html (4.5.2020)
fatalityRateAge = []

estimatedTotalCases = sum(deathsPerAge)/totalFatalityRate

print("\n\nestimated Total Cases:",format(estimatedTotalCases,'.0f'),", based on", sum(deathsPerAge),"fatal cases and a fatality rate of",totalFatalityRate,"\n")

populationNr = sum(ageDistribution)
print("Population:",populationNr,",estimated cases:",format(sum(ageDistribution)/(populationNr/estimatedTotalCases),'.0f'),"divided per group:")

for i in range(len(ageDistribution)):
    ageDistribution[i] = ageDistribution[i] / (populationNr/estimatedTotalCases)
    print(txtAgeGroups[i],"\t:",format(ageDistribution[i],'.0f'))

print("-----------------------\n\nFatality Rate per Age:")
for i in range(len(ageDistribution)):
    fatalityRateAge.append((deathsPerAge[i]/ageDistribution[i])*100)
    print(txtAgeGroups[i],"\t:",format(fatalityRateAge[i],'.5f'),"%")
    
print("\nNote: assumed that distribution of cases is even across all age groups. Fatality rate at the higher age groups might be higher if more younger people are infected in total, in that case, the fatality rate in the younger groups would be lower. Individual risk factors are not included.")
    
print("checksum total fatality Rate:",(sum(deathsPerAge)/sum(ageDistribution)))

#show graph
plt.title("Covid-fatality rate per age group")
plt.xlabel("Age Groups")
plt.ylabel("Probability for fatal cases in %")
plt.plot(txtAgeGroups,fatalityRateAge)
plt.show()