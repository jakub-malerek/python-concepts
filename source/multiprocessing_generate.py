import pandas as pd
import numpy as np
import time

df = pd.read_excel("../SampleData/SampleData.xlsx",sheet_name=1)

def generate_data(rows, mode = "a"):
    OrderDate = pd.date_range(df["OrderDate"].min(),df["OrderDate"].max())
    Region = df["Region"].unique()
    Rep = df["Rep"].unique()
    Item = df["Item"].unique()
    min_units = df["Units"].min()
    max_units = df["Units"].max()
    max_unit_cost = df["Unit Cost"].quantile(0.75)
    min_units_cost = df["Unit Cost"].min()

    data = pd.DataFrame(dict(zip(df.columns,[
    np.random.choice(OrderDate,size=rows),
    np.random.choice(Region,size=rows),
    np.random.choice(Rep,size=rows),
    np.random.choice(Item,size=rows),
    np.random.randint(min_units,max_units+1,size=rows),
    np.random.uniform(min_units_cost,max_unit_cost,size=rows).round(2)

    ])))


    data["Total"] = data["Units"] * data["Unit Cost"]


    data.to_csv("dummy_data.csv",mode=mode,header=None)    
    
import multiprocessing

def worker(args):
    generate_data(args)


def multiprocessing_generate(rows_per_batch,n_batches):
    with multiprocessing.Pool() as pool:
        pool.map(worker,[rows_per_batch]*n_batches)


if __name__ == "__main__":
    start = time.time()
    multiprocessing_generate(10000000,10)
    print("multi",time.time()-start)

    start = time.time()
    generate_data(100000000,mode="w")
    print("no mulit",time.time()-start)