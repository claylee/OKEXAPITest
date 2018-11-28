import sys
from stageData import dataSchema
import numpy as np
import time

TradePrice = dataSchema.TradePrice

def reorderHour(tickerList):
    print(tickerList)
    print("tickerList")
    dict = {}
    for t in tickerList:
        if t[0] not in dict:

            dict[t[0]] = []
        dict[t[0]].append(t[1]);
    return dict

def DateTicks(dictHour):
    for l in dictHour:
        print(l)


def ConstructTensor(cList):
    # BtcList = dataSchema.TradePrice.filter(
    #     str.upper(TradePrice.SetCoin) == 'BTC')
    # LtcList = dataSchema.TradePrice.filter(
    #     str.upper(TradePrice.SetCoin) == 'LTC')
    dict = {}
    dictHour = {}
    # btcTensor = np.empty(len(BtcList),2)
    # ltcTensor = np.empty(len(LtcList), 2)
    # for b in BtcList:
    #     np.append(btcTensor, [[b.date, b.buy]], axis=0)

    # for l in LtcList:
    #     np.append(ltcTensor, [[l.date, l.buy]], axis=0)
    #cList = TradePrice.query.all()

    for l in cList:
        if l.date is None or l.SetCoin is None:
            continue

        timeTp = l.date.timetuple()
        daterStr = "{}-{}-{}".format(timeTp.tm_year,timeTp.tm_mon,timeTp.tm_mday)
        timeStr = "{}-{}-{} {}".format(timeTp.tm_year,timeTp.tm_mon,timeTp.tm_mday,timeTp.tm_hour)
        dt = time.mktime(l.date.timetuple())
        if daterStr not in dictHour:
            dictHour[daterStr] = {}

        if timeStr not in dictHour[daterStr]:
            dictHour[daterStr][timeStr] = [[],[]]

        if dt not in dict:
            dict[dt] = [0, 0]

        if str.upper(l.SetCoin) == "BTC":
            dict[dt][0] = l.buy
            dictHour[daterStr][timeStr][0].append(l.buy)

        elif str.upper(l.SetCoin) == "LTC":
            dict[dt][1] = l.buy
            dictHour[daterStr][timeStr][1].append(l.buy)

        print(timeStr,len(dictHour[daterStr][timeStr]))

    npList = np.empty([len(dict.keys()), 3])
    pList = []
    for k, v in dict.items():
        pList.append([k, v[0], v[1]])

    npList = np.array(pList)

    print(len(npList))
    return npList, dictHour
