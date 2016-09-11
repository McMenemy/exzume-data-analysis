import csv
import matplotlib.pyplot as plt

reader = csv.reader(open("./QJ_data_formated.csv"))

print(reader)

data_array = []
for row in reader:
    data_array.append(row)

satisfaction = []
happiness = []
stress = []
masturbation = []
sex = []

for entry in data_array[1:]:
    for i, value in enumerate(entry):
        print(i)
        if i == 44:
            stress.append(int(value[0]))
        elif i == 43:
            happiness.append(int(value[0]))
        elif i == 40:
            masturbation.append(int(value[0]))
        elif i == 42:
            satisfaction.append(int(value[0]))
        elif i == 39:
            sex.append(int(value[0]))

print(stress)
print(happiness)
print(masturbation)
print(satisfaction)

plt.plot(sex)
plt.ylabel('amount')
plt.xlabel('day')
plt.title('Sex Over Time - it can only go up from here, right?')
plt.savefig('sex.png')
plt.clf()

plt.plot(satisfaction, label='satisfaction')
plt.plot(stress, label='stress')
plt.plot(happiness, label='happiness')
plt.plot(masturbation, label='masturbation')
plt.title('Quantified Josh')
plt.ylabel('score')
plt.xlabel('day')
plt.legend()
plt.savefig('Quantified Josh')
