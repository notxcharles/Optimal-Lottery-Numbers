import csv
from bs4 import BeautifulSoup
import requests

current_year = 2022


def createCSV(name, header):
    with open(f"{name}_results.csv", "w", newline="") as f:
        w = csv.writer(f, delimiter="|")
        w.writerow(header)
        f.close()


def writeToCSV(name, results):
    # date, balls, special_balls, jackpot
    with open(f"{name}_results.csv", "a", newline="") as f:
        writer = csv.writer(f, delimiter="|")
        writer.writerow(results)
        f.close()


createCSV(
    "EuroMillions",
    [
        "Draw Date",
        "Ball 1",
        "Ball 2",
        "Ball 3",
        "Ball 4",
        "Ball 5",
        "Lucky 1",
        "Lucky 2",
        "Jackpot",
    ],
)

headers = {
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Methods": "GET",
    "Access-Control-Allow-Headers": "Content-Type",
    "Access-Control-Max-Age": "3600",
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0",
}
euromillions_results_url = "https://www.lottery.co.uk/euromillions/results/archive-"
lotto_results_url = "https://www.lottery.co.uk/lotto/results/archive-2022"

for year in range(2004, current_year + 1):

    req = requests.get(euromillions_results_url + str(year), headers)
    soup = BeautifulSoup(req.content, "html.parser")
    results = soup.find_all("tr")

    for result in results:
        if results[0] == result:
            continue
        date = result.find(class_="smallerHeading").string
        balls = result.find_all(class_="euromillions-ball")
        regular_balls = [int(ball.string) for ball in balls]
        balls = result.find_all(class_="euromillions-lucky-star")
        special_balls = [int(ball.string) for ball in balls]
        try:
            jackpot = result.find("strong").string.replace("£", "")
            jackpot = jackpot.replace(",", "")
        except AttributeError:
            jackpot = None

        resultsToWrite = []
        resultsToWrite.append(date)

        for ball in regular_balls:
            resultsToWrite.append(ball)
        for ball in special_balls:
            resultsToWrite.append(ball)
        resultsToWrite.append(jackpot)

        # print(date, regular_balls, special_balls, jackpot)
        writeToCSV("EuroMillions", resultsToWrite)
