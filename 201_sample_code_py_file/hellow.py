import pandas as pd
import datetime,time

i=0
li=[datetime.datetime.now(),i]
df = pd.DataFrame([li])

for i in range(300):
    time.sleep(0.01)
    i=i+1
    li=[datetime.datetime.now(),i]
    df=df.append([li], ignore_index=True)
df.columns=["time", "value"]
df.to_csv("test.csv")