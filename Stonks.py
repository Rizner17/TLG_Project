#!/usr/bin/env python3
""" AJRodriguez | Stock market analysis"""

import datetime
import requests
import matplotlib.pyplot as plt

#Stock Ticker is the symbol i.e. AAPL, date is in format: YYYY-MM-DD

#API_KEY = ("/home/student/MyProject/polygonAPI.key") <--Location of my private key

def poly():
    """first I want to read my credentials from my file"""
    with open("/home/student/MyProject/polygonAPI.key", "r") as stonks:#opens the polygonAPI.key file in read mode
        poly = stonks.readline()#reads the only line in the file to assign my api key to poly
    return poly#returns poly for use in the main function below

def main():
    """Main code"""
    stockticker = input("What stock would you like to request?")#stockticker is the 3-4 letter code for a stock /n
    #user inputs their stock code that will pull from the api
    prices = []#an empty list for prices we append to for use in the graph
    dates = []#an empty list for dates we append to for use in the graph
    for i in range(7):#start of a loop looking for 7 days of the week to loop through
        today = datetime.date.today()#defines today's date as the starting point
        oneday = datetime.timedelta(days=i)
        date = today - oneday#subtracts one day from today's date through the loop for 7 instances
        try:
            if date.weekday() in [5, 6]:#weekday is 0-6, 5 & 6 are the weekends when the market is closed
                continue#continues through the loop of days

            polygonapi = f"https://api.polygon.io/v1/open-close/{stockticker}/{date}?unadjusted=true&apiKey={poly()}"#api url which takes the stockticker input and the date above to get us our last weeks data
            polyresp = requests.get(polygonapi)#sends a get request to the api
            polydata = polyresp.json()#pulls the json data format

            print(polydata["close"])#prints the closing price string of each of our days
            prices.append(polydata["close"])#appends the price list above for use in the graph
            dates.append(date)#appends the date list above for use in our graph
        except:#an except and pass to passover the weekend days (our api is limited to 5 calls a min)
            pass

        figure, axis = plt.subplots()
        axis.plot(dates, prices, label= stockticker)
        plt.ylabel("Closing Price")#labels the y-axis "Closing Prices"
        plt.xlabel("Date")#labels the x-axis "Dates"
        plt.title("Weekly Stonk review")#labels the graph as "weekly Stonk Review"
        axis.legend()
        plt.xticks(rotation= 35)#rotates the x-axis 35 degrees down for legibility
        
        #display the graph
        plt.show()
        plt.savefig(f"/home/student/mycode/graphing/WeeklyStonks{stockticker}.pdf")
        #save copy to "~/static" (the "files" view)
        plt.savefig(f"/home/student/static/WeeklyStonks{stockticker}.pdf")

if __name__ == "__main__":
    main()
