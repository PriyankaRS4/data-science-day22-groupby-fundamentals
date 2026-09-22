import pandas as pd
df=pd.read_csv("titanic.csv")
for c in ["pclass","survived","age","fare"]: df[c]=pd.to_numeric(df[c],errors="coerce")
print(df.groupby("pclass")["fare"].sum())
print(df.groupby("pclass")["fare"].mean())
print(df.groupby("sex")["survived"].count())
print(df.groupby("embarked")["fare"].agg(["min","max"]))
print(df.groupby("pclass").agg(passengers=("pclass","count"),total_fare=("fare","sum"),average_fare=("fare","mean"),min_fare=("fare","min"),max_fare=("fare","max")))
print(df.groupby(["sex","pclass"]).agg(passengers=("survived","count"),survivors=("survived","sum"),average_fare=("fare","mean")))
