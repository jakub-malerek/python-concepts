import multiprocessing
import time
import random
import pandas as pd

def multiprocessing_explicit(func):

    start = time.time()

    processes = []

    
    for x in range(1000,1100):

        process = multiprocessing.Process(target=func,args=(x,start))
        processes.append(process)
        process.start()


    for process in processes:
        process.join()

    perf = time.time()-start 
    print(f"Process took: {perf}s")

    return perf



def boost(x,start):
    t = random.randrange(10)/10
    time.sleep(t)
    result = round((x**100)**(1/100),2)
    print(f"Processing for {x} -> {result} finished in {time.time()-start}s")
    return result,f"Processing for {x} -> {result} finished in {time.time()-start}s"


def multiprocessing_automate(func):
    start = time.time()
    with multiprocessing.Pool() as pool:
        result = pool.starmap(func,zip(range(1000,1100),[start for _ in range(1100-1000)]),chunksize=25)

    perf = time.time()-start     
    print(f"Process took: {perf}s")

    return result, perf


def run_tests():
    r1 = multiprocessing_automate(boost)
    print("automate end ---------------------------------------------")
    r2 = multiprocessing_explicit(boost)

    print(f"automate/explicit rate is {(r1[1]/r2)}")
    print("------------------------------")
    print([e[0] for e in r1[0]])


import multiprocessing
import time

def multi_process_batches(func, data, postfix):
    start = time.time()
    with multiprocessing.Pool() as pool:
        # Wrap each data batch with the static postfix before processing
        pool.starmap(func, [(batch, postfix) for batch in data])

    print(f"Execution time {time.time() - start}")

def customers_process(batch, postfix):
    batch.drop(columns="Index", inplace=True)
    batch["Subscription Date"] = batch["Subscription Date"].apply(lambda x: x[-5:-3] + "/" + x[-2:] + "/" + x[:4])
    batch["Domain"] = batch["Website"].str.split("//").str[1].str.split("/").str[0].str.replace("www.", "", regex=False)

    batch.to_csv(f"clean_customers{postfix}.csv", mode="a", header=False)

def sequential_process_batches(func, data, postfix):
    start = time.time()
    for batch in data:
        func(batch, postfix)

    print(f"Execution time {time.time() - start}")

if __name__ == "__main__":
    import pandas as pd

    df = pd.read_csv("../../Downloads/customers-2000000.csv", chunksize=100_000)


    sequential_process_batches(customers_process, df, "seq")


    df = pd.read_csv("../../Downloads/customers-2000000.csv", chunksize=500_000)

    multi_process_batches(customers_process, df, "multi")



    



