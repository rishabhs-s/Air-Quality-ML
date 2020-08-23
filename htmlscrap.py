import os
import time
import sys
import requests

def retrieve_html():
    for year in range(2013,2019):
        for month in range(1,13):
            if (month<10):
                url="https://en.tutiempo.net/climate/0{}-{}i/ws-421810.html".format(month,year)
            else:
                url="https://en.tutiempo.net/climate/{}-{}i/ws-421810.html".format(month,year)

            texts=requests.get(url)
            text_utf=texts.text.encode("utf=8")


            if not os.path.exists("Data/Html_Data/{}".format(year)):
                os.makedirs("Data/Html_Data/{}".format(year))
            with open("Data/Html_Data/{}/{}.html".format(year,month), "wb") as output:
                output.write(text_utf)
        sys.stdout.flush()

if __name__ == "__main__":
    start_time=time.time()
    retrieve_html()
    stop_time=time.time()
    print("Time taken {}".format(stop_time-start_time))

