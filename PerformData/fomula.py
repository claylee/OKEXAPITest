import sys
from stageData import dataSchema
import numpy as np
import time

TradePrice = dataSchema.TradePrice


def ConstructTensor():
    # BtcList = dataSchema.TradePrice.filter(
    #     str.upper(TradePrice.SetCoin) == 'BTC')
    # LtcList = dataSchema.TradePrice.filter(
    #     str.upper(TradePrice.SetCoin) == 'LTC')
    dict = {}
    # btcTensor = np.empty(len(BtcList),2)
    # ltcTensor = np.empty(len(LtcList), 2)
    # for b in BtcList:
    #     np.append(btcTensor, [[b.date, b.buy]], axis=0)

    # for l in LtcList:
    #     np.append(ltcTensor, [[l.date, l.buy]], axis=0)
    cList = TradePrice.query.all()

    for l in cList:
        if l.date is None or l.SetCoin is None:
            continue

        dt = time.mktime(l.date.timetuple())
        if dt not in dict:
            dict[dt] = [0, 0]

        if str.upper(l.SetCoin) == "BTC":
            dict[dt][0] = l.buy
        elif str.upper(l.SetCoin) == "LTC":
            dict[dt][1] = l.buy

    npList = np.empty([len(dict.keys()), 3])
    pList = []
    for k, v in dict.items():
        pList.append([k, v[0], v[1]])

    npList = np.array(pList)

    print(npList)
    return npList