#Mutliprocessing : Is Same Like Multithreading But It Runs On Processors

import multiprocessing
import requests

def Downloader(url,name):
    print(f"Started Downloading {name}")
    response = requests.get(url)
    open(f"files/file{name}.jpg","wb").write(response.content)
    print(f"Finished Downloading{name}")
    
if __name__ == "__main__":
    url = "https://picsum.photos/200/300"
    pros = []
    for i in range(10):
        p = multiprocessing.Process(target=Downloader,args=[url,i])
        p.start()
        pros.append(p)
    
    for p in pros:
        p.join()

#Thanks
