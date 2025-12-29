# CSV(Comma Sepreited Values), CSV files using for sending datas, read examples in documents, doing different to seeing
# for power in partition, statistic, mean([x,y]), list(), founding meaning of they numbers
# don't think complete way for codin just doing and way is showed hemlesf(Flowing Natural), %1.2f, %4s
import csv
from statistics import mean

with open(
    "E:/0 Plans/1 Job(Money)/7 Gain professional experience/0 Git, GitHub/1 Repos/Jadi/src/Jadi/1 Basic of Python/S4/1.csv"
) as f:
    reader = csv.reader(f)
    for vibration in reader:
        Names = vibration[0]
        Listing = list()
        for vibration_2 in vibration[1:]:
            vibration_2 = int(vibration_2)
            Listing.append(vibration_2)
            Mean = mean(Listing)
        print("Average Number of %11s is %1.2f" % (Names, Mean))
