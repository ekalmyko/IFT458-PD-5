import urllib.request
import json

KEY = 'YPZJSID38O2K7RV3' # API key generated, by signing up on the link mentioned in the document


def getStockData(symbol):
    URL = 'https://www.alphavantage.co/query?function=BATCH_STOCK_QUOTES&symbols=' + symbol + '&apikey=' + KEY
    connection = urllib.request.urlopen(URL)
    responseString = connection.read().decode()
    return responseString


def main():
    # take user input
    userChoice = input("Please enter the stock symbol to get data or type 'quit' to exit the program: ") 

    if(userChoice == 'quit'):
        # terminate the program
        exit() 


    response = getStockData(userChoice)
    print("JSON-formatted response: ", response)

    # convert server response into python dictionary
    jsonResponse = json.loads(response) 
    print("The current price of " + userChoice + " is: ", jsonResponse["Stock Quotes"][0]["2. price"])

    
    main() 

# call the main function
main()
