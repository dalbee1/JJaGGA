import time
import pyupbit
import datetime
import pandas
import json
import random
import talib

access = ""
secret = ""

# 로그인
upbit = pyupbit.Upbit(access, secret)
print("가쥬아")

coinArray = pyupbit.get_tickers(fiat="KRW")
coinArray = random.shuffle(coinArray)
count = 0


def get_start_time(ticker):
    """시작 시간 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=1)
    start_time = df.index[0]
    return start_time

#def get_buy_average(currency):                # 평균매수가
#    balances = upbit.get_balances()
#    for b in balances:
#        if b['currency'] == currency:
#            if b['avg_buy_price'] is not None:
#                return float(b['avg_buy_price'])
#            else:
#                return 0
###### 코코넛 설정 ######
def coconut() :
    global tiktok
    global delete_coin

tiktok = 0

def search() :
    global count
   
    try :
        
        count +=1
        coinArray = pyupbit.get_tickers(fiat="KRW")
        coinArray = list(reversed(coinArray))
        
        if tiktok == 0:
            ccoin = "KRW-BTC"
        else :
            ccoin = delete_coin
        
        coinArray.remove(ccoin)
        #coinArray.remove("KRW-NEO")
        
        now = datetime.datetime.now()
        start_time = get_start_time("KRW-BTC")
        buystart_time = start_time + datetime.timedelta(minutes=90)
        buy_time = start_time + datetime.timedelta(minutes=1410)
        
        if buystart_time < now < buy_time :
            for i in coinArray :
            
                df = pyupbit.get_ohlcv(i, "minute5")
               
                
                CurHigh = float(df.iloc[-1]['high'])
                Close  = float(df.iloc[-2]['close'])
                
                EMA17 = talib.EMA(df['close'], 17 )
                ma17A = EMA17[-1]
                ma17B = EMA17[-2]
                EMA17A = EMA17[-18]
                EMA17B = EMA17[-19]
                EMA33 = talib.EMA(df['close'], 33 )
                ma33 =  EMA33[-1]
                EMA53 = talib.EMA(df['close'], 53 )
                ma53 =  EMA53[-1]
                EMA80 = talib.EMA(df['close'], 80 )
                ma80 =  EMA80[-1]
                EMA115 = talib.EMA(df['close'], 115 ) 
                #ma199B =  EMA130[-2]
                
                sonarA = ((ma17A-EMA17A)/EMA17A)*100
                sonarB = ((ma17B-EMA17B)/EMA17B)*100
                
                EMA90 = talib.EMA(df['close'], 90 )
                EMA90_1 = EMA90[-1]
                EMA90_2 = EMA90[-2]
                EMA90_3 = EMA90[-3]
                EMA90_4 = EMA90[-4]
                EMA90_5 = EMA90[-5]
                EMA90_6 = EMA90[-6]
                EMA90_7 = EMA90[-7]
                EMA90_8 = EMA90[-8]
                EMA90_9 = EMA90[-9]
                EMA90_10 = EMA90[-10]
                EMA90_11 = EMA90[-11]
                EMA90_90 = EMA90[-91]
                EMA90_91 = EMA90[-92]
                EMA90_92 = EMA90[-93]
                EMA90_93 = EMA90[-94]
                EMA90_94 = EMA90[-95]
                EMA90_95 = EMA90[-96]
                EMA90_96 = EMA90[-97]
                EMA90_97 = EMA90[-98]
                EMA90_98 = EMA90[-99]
                EMA90_99 = EMA90[-100]
                EMA90_100 = EMA90[-101]
                
                SONAR90_1 = (EMA90_1-EMA90_90)
                SONAR90_2 = (EMA90_2-EMA90_91)
                SONAR90_3 = (EMA90_3-EMA90_92)
                SONAR90_4 = (EMA90_4-EMA90_93)
                SONAR90_5 = (EMA90_5-EMA90_94)
                SONAR90_6 = (EMA90_6-EMA90_95)
                SONAR90_7 = (EMA90_7-EMA90_96)
                SONAR90_8 = (EMA90_8-EMA90_97)
                SONAR90_9 = (EMA90_9-EMA90_98)
                SONAR90_10 = (EMA90_10-EMA90_99)
                SONAR90_11 = (EMA90_11-EMA90_100)
                                              
                OPEN1 = float(df.iloc[-1]['open'])
                OPEN2 = float(df.iloc[-2]['open'])
                OPEN3 = float(df.iloc[-3]['open'])
                OPEN4 = float(df.iloc[-4]['open'])
                OPEN5 = float(df.iloc[-5]['open'])
                OPEN6 = float(df.iloc[-6]['open'])

                Close = float(df.iloc[-1]['close'])
                CClose = float(df.iloc[-2]['close'])
                CCClose = float(df.iloc[-3]['close'])
                CCCClose = float(df.iloc[-4]['close'])
                CCCCClose = float(df.iloc[-5]['close'])
                CCCCCClose = float(df.iloc[-6]['close'])
                CCCCCCClose = float(df.iloc[-7]['close'])
                #High = float(df.iloc[-1]['high'])
                HIGH = float(df.iloc[-1]['high'])
                HHIGH = float(df.iloc[-2]['high'])
                HHHIGH = float(df.iloc[-3]['high'])
                HHHHIGH = float(df.iloc[-4]['high'])
                HHHHHIGH = float(df.iloc[-5]['high'])
                HHHHHHIGH = float(df.iloc[-6]['high'])
                
                LOW = float(df.iloc[-1]['low'])
                LLOW = float(df.iloc[-2]['low'])
                LLLOW = float(df.iloc[-3]['low'])
                LLLLOW = float(df.iloc[-4]['low'])
                LLLLLOW = float(df.iloc[-5]['low'])
                LLLLLLOW = float(df.iloc[-6]['low'])

                ALLHIGH1 = max(HIGH, HHIGH)
                ALLLOW1 = min(LOW, LLOW)                                
                ALLHIGH2 = max(HIGH, HHIGH, HHHIGH)
                ALLLOW2 = min(LOW, LLOW, LLLOW)                                
                ALLHIGH3 = max(HIGH, HHIGH, HHHIGH, HHHHIGH)
                ALLLOW3 = min(LOW, LLOW, LLLOW, LLLLOW)                                
                ALLHIGH4 = max(HIGH, HHIGH, HHHIGH, HHHHIGH, HHHHHIGH)
                ALLLOW4 = min(LOW, LLOW, LLLOW, LLLLOW, LLLLLOW)                                
                ALLHIGH5 = max(HIGH, HHIGH, HHHIGH, HHHHIGH, HHHHHIGH, HHHHHHIGH)
                ALLLOW5 = min(LOW, LLOW, LLLOW, LLLLOW, LLLLLOW, LLLLLLOW)                                
                Price = pyupbit.get_current_price(i)
                orderbook = pyupbit.get_orderbook(i)
                #BID = orderbook['bids']
                #d["BlockDMask"]
                bid_ask = orderbook['orderbook_units']
                bid_ask1 = bid_ask[0]
                ask1 = bid_ask1['ask_price']
                ask1 = float(ask1)
                bid1 = bid_ask1['bid_price']
                #print("매도호가:")
                #print(ask1)
                #print("매수호가:")
                #print(bid1)
                #print('매수호가: '+ bid1)
                #print(bids)
                #print(asks)

                outputA = talib.SAR(df['high'], df['low'], 0.01, 0.1 )
                sarA = outputA[-1]
                sarAA = outputA[-2]
                sarAAA = outputA[-3]
                sarAAAA = outputA[-4]
                sarAAAAA = outputA[-5]
                sarAAAAAA = outputA[-6]
                sarAAAAAAA = outputA[-7]

                outputB = talib.SAR(df['high'], df['low'], 0.02, 0.2 )
                sarB = outputB[-1]
                sarBB = outputB[-2]
                sarBBB = outputB[-3]
                sarBBBB = outputB[-4]
                sarBBBBB = outputB[-5]
                sarBBBBBB = outputB[-6]
                sarBBBBBBB = outputB[-7]
                
                cci = talib.CCI(df['high'], df['low'], df['close'], 130)
                cci_1 = cci[-1]
                cci_2 = cci[-2]
                cci_3 = cci[-3]
                cci_4 = cci[-4]
                cci_5 = cci[-5]
                cci_6 = cci[-6]
                cci_7 = cci[-7]
                cci_8 = cci[-8]
                cci_9 = cci[-9]
                cci_10 = cci[-10]
                volume = df['volume'].rolling(1).mean().iloc[-1]
                #volume5B = df['volume'].rolling(5).mean().iloc[-2]
                #volume10A = df['volume'].rolling(10).mean().iloc[-1]
                #volume10B = df['volume'].rolling(10).mean().iloc[-2]
                volume15A = df['volume'].rolling(15).mean().iloc[-1]
                #volume15B = df['volume'].rolling(15).mean().iloc[-2]
                
                
                slowk, slowd = talib.STOCH(df['high'], df['low'], df['close'],
                               fastk_period=14, slowk_period=3, slowk_matype=0, slowd_period=3, slowd_matype=0)                          
                slowK_1 = slowk[-1]
                slowK_2 = slowk[-2]
                
                
                
                
                BBAND_UPPER, BBAND_MIDDLE, BBAND_LOWER = talib.BBANDS(df['close'],20,2.2)
                UPPER1 = BBAND_UPPER[-1]
                UPPER2 = BBAND_UPPER[-2]
                UPPER3 = BBAND_UPPER[-3]
                UPPER4 = BBAND_UPPER[-4]
                UPPER5 = BBAND_UPPER[-5]
                UPPER6 = BBAND_UPPER[-6]
                MIDDLE1 = BBAND_MIDDLE[-1]
                MIDDLE2 = BBAND_MIDDLE[-2]
                MIDDLE3 = BBAND_MIDDLE[-3]
                MIDDLE4 = BBAND_MIDDLE[-4]
                MIDDLE5 = BBAND_MIDDLE[-5]
                MIDDLE6 = BBAND_MIDDLE[-6]
                LOWER1 = BBAND_LOWER[-1]
                LOWER2 = BBAND_LOWER[-2]
                LOWER3 = BBAND_LOWER[-3]
                LOWER4 = BBAND_LOWER[-4]
                LOWER5 = BBAND_LOWER[-5]
                LOWER6 = BBAND_LOWER[-6]
                
                Bandwidth1 = (UPPER1-LOWER1) / MIDDLE1
                Bandwidth2 = (UPPER2-LOWER2) / MIDDLE2
                Bandwidth3 = (UPPER3-LOWER3) / MIDDLE3
                Bandwidth4 = (UPPER4-LOWER4) / MIDDLE4
                Bandwidth5 = (UPPER5-LOWER5) / MIDDLE5

                Bandwidth = (Bandwidth1 + Bandwidth2 + Bandwidth3 + Bandwidth4 + Bandwidth5)/5 
                
                talib_dmp = talib.MINUS_DI(df["high"], df["low"], df["close"], timeperiod=14)
                D_MINUS1 = talib_dmp[-1]

                #ATR = talib.ATR(df['high'], df['low'], df['close'], 30)
                #atr = ATR[-1]
                #atrr = atr / ma30
                
                #orderbook = pyupbit.get_orderbook(i)
                #bids_asks = orderbook[0]['orderbook_units']
                #for bid_ask in bids_asks:
                #    print(bid_ask)
                #print(bids_asks)
                
                print("***  업비트7  ***")
                print("***  "+ i + "   ***")
                print('현재가' + '/' + str(Price))                
                #print('7분봉 / 45분봉' + str(sarAA) + '/' + str(sarA))
                #print('7분봉 / 45분봉' + str(slowK) + '/' + str(slowKK))
                #print('7분봉 / 45분봉' + int(Price))
                
                if  ((0.4 <= float(Price) < 1 or 4 <= float(Price) < 10 or 40 <= float(Price) < 100 or 400 <= float(Price) < 1000 or 2000 <= float(Price)) 
                     #and ma17A > ma130 
                     #and ma33 > ma53 > ma80 > ma115 #> ma130
                     #and ma33 > sarB and ma33 > sarA and (sarBB > sarB or sarAA > sarA) and Close < sarAAA
                     #and sarBBBBBB > sarBBBBB > sarBBBB > sarBBB > sarBB > sarB and CurHigh < sarB < CurHigh*1.003
                     and (volume * float(Price)) > 30000000 #):
                     #and cci_10 > 77 and cci_9 > 77 and cci_8 > 77 and cci_7 > 77 and cci_6 > 77 and cci_5 > 77 and cci_4 > 77 and cci_3 > 77 and cci_2 > 77 and cci_1 > 77 
                     #and slowK < 70 #and slowK > slowD and slowKma5 > slowKma10 
                     #and ((sarAA > CClose and sarA < float(Price) and sarBBB > CCClose) or (sarBB > CClose and sarB < float(Price) and sarAAA > CCClose)) and LOWER > sarB >= sarA > LOWER * 0.996
                     #and (Close < sarBB and float(Price) > sarB) #and sarA < ma130 
                     #and ((ALLHIGH - ALLLOW) * 0.5 > (float(Price) - ALLLOW))
                     and Bandwidth > 0.023
                     and D_MINUS1 > 8
                     and OPEN2 * -0.02 < OPEN2 - CClose < OPEN2 * 0.02
                     and((((sarAAAAAAA > CCCCCCClose and sarAAAAAA < CCCCCClose) or (sarBBBBBBB > CCCCCCClose and sarBBBBBB < CCCCCClose))
                          and sarAAAAAA < LOWER6 and sarBBBBBB < LOWER6)
                          and (sarAAAAA < CCCCClose and sarAAAA < CCCClose and sarAAA < CCClose and sarAA < CClose 
                          and sarBBBBB < CCCCClose and sarBBBB < CCCClose and sarBBB < CCClose and sarBB < CClose)
                          and ((UPPER6 - MIDDLE6) * 0.5) > (OPEN6 - MIDDLE6)
                          and ((OPEN6 * 1.001) < CCCCCClose < (OPEN6 * 1.015))                          
                          and ((ALLHIGH5 - ALLLOW5) * 0.65 > (ask1 - ALLLOW5)) or
                         
                         (((sarAAAAAA > CCCCCClose and sarAAAAA < CCCCClose) or (sarBBBBBB > CCCCCClose and sarBBBBB < CCCCClose))
                          and sarAAAAA < LOWER5 and sarBBBBB < LOWER5) 
                          and (sarAAAA < CCCClose and sarAAA < CCClose and sarAA < CClose 
                          and sarBBBB < CCCClose and sarBBB < CCClose and sarBB < CClose) 
                          and ((UPPER5 - MIDDLE5) * 0.5) > (OPEN5 - MIDDLE5)
                          and ((OPEN5 * 1.001) < CCCCClose < (OPEN5 * 1.015))                          
                          and ((ALLHIGH4 - ALLLOW4) * 0.65 > (ask1 - ALLLOW4)) or
                         
                         (((sarAAAAA > CCCCClose and sarAAAA < CCCClose) or (sarBBBBB > CCCCClose and sarBBBB < CCCClose))
                          and sarAAAA < LOWER4 and sarBBBB < LOWER4) 
                          and (sarAAA < CCClose and sarAA < CClose
                          and sarBBB < CCClose and sarBB < CClose) 
                          and ((UPPER4 - MIDDLE4) * 0.5) > (OPEN4 - MIDDLE4)
                          and ((OPEN4 * 1.001) < CCCClose < (OPEN4 * 1.015))                          
                          and ((ALLHIGH3 - ALLLOW3) * 0.65 > (ask1 - ALLLOW3)) or 
                         
                         (((sarAAAA > CCCClose and sarAAA < CCClose) or (sarBBBB > CCCClose and sarBBB < CCClose))
                          and sarAAA < LOWER3 and sarBBB < LOWER3) 
                          and (sarAA < CClose
                          and sarBB < CClose) 
                          and ((UPPER3 - MIDDLE3) * 0.5) > (OPEN3 - MIDDLE3)
                          and ((OPEN3 * 1.001) < CCClose < (OPEN3 * 1.015))
                          and ((ALLHIGH2 - ALLLOW2) * 0.65 > (ask1 - ALLLOW2)) or 
                     
                         (((sarAAA > CCClose and sarAA < CClose) or (sarBBB > CCClose and sarBB < CClose))
                          and sarAA < LOWER2 and sarBB < LOWER2)
                          and ((UPPER2 - MIDDLE2) * 0.5) > (OPEN2 - MIDDLE2)
                          and ((OPEN2 * 1.001) < CClose < (OPEN2 * 1.015))
                          and ((ALLHIGH1 - ALLLOW1) * 0.65 > (ask1 - ALLLOW1)) )):

                     #and HIGH < (Close * 1.025) and (Close * 1.01) < float(Price) < (Close * 1.025)) :
                     #and UPPER > ma17A and UPPER > ma33 and UPPER > ma53 and UPPER > ma80 and UPPER > ma115 and UPPER > ma130
                     #and (LOWER > float(Price) or LOWER > LOW)
                     #and slowK_1 >= 75
                     #and (atrr > 0.0028 or atrr < 0.0018)
                     #and SONAR90_11 < SONAR90_10 < SONAR90_9 < SONAR90_8 < SONAR90_7 < SONAR90_6 < SONAR90_5 < SONAR90_4 < SONAR90_3 < SONAR90_2 < SONAR90_1 ) :
                     #and sonarA > 0 ) :
                     #and volume5A > volume10A and volume5A > volume5B and volume10A > volume10B ) :
                    
                    print("!!!!!!!급등코인!!!!!!!!")
                    return i
                    break
                #time.sleep(0.5)
    except :
        print("다시조회합니다. {} 회 반복중".format(count))
        time.sleep(1)
        search()           
         
    




while True:                                  # 급등코인 매수
    try:
        i = search()                         # 급등코인 결정
        krw = upbit.get_balance("KRW")
        orderbook = pyupbit.get_orderbook(i)
        bid_ask = orderbook['orderbook_units']
        bid_ask1 = bid_ask[0]
        ask1 = bid_ask1['ask_price']
        ask1 = float(ask1)
        bid1 = bid_ask1['bid_price']
        bid1 = float(bid1)
        
        ###### 호가 단위 계산 ######
        firstPrice = pyupbit.get_current_price(i)
        if float(str(firstPrice)) < 10:
            hoga_val = 0.01
        elif float(str(firstPrice)) < 100:
            hoga_val = 0.1
        elif float(str(firstPrice)) < 1000:
            hoga_val = 1
        elif float(str(firstPrice)) < 10000:
            hoga_val = 5
        elif float(str(firstPrice)) < 100000:
            hoga_val = 10
        elif float(str(firstPrice)) < 500000:
            hoga_val = 50
        elif float(str(firstPrice)) < 1000000:
            hoga_val = 100
        elif float(str(firstPrice)) < 2000000:
            hoga_val = 500
        else:
            hoga_val = 1000
 
        
        ###### 매수주문 ######
        
        ###### 매수 1차 ######
        upbit.buy_market_order(i, krw*0.1)
        print("<<<< " + str(i) + " 구매완료 >>>>")
        
        ###### 결제 금액 ######
        buy_average = float(upbit.get_avg_buy_price(i))
        goomae = buy_average
        firstPrice = pyupbit.get_current_price(i)
        print("구매금액 : " + str(buy_average))
        
        A = 1 
        while A < 4:
            now = datetime.datetime.now()
            current_price = pyupbit.get_current_price(i)
            buy_average = float(upbit.get_avg_buy_price(i))
            winrate = ((current_price / buy_average)*100) - 100
            print("<<< 업비트7 >>>")
            print("<<<<<<<< " + str(A) +"차 구매완료 >>>>>>>>")
            print("<<<< 구매코인: " + str(i) + " >>>>")
            print("현재가: " + str(current_price))
            print("평균구매가: " + str(buy_average))
            print("수익률: " + str(winrate) + "%")
            time.sleep(0.5)

            # 매수 1차
            #if A==0
            #    upbit.buy_market_order(i, krw*0.1)
            #    time.sleep(1)
            #    buy_average = get_buy_average(currency)
            #    A += 1                
            #    print("%dst Buy OK" % (A))              

            ###### 매수 2차 ######
            if A <= 1 and current_price < firstPrice*0.997:
                upbit.buy_market_order(i, krw*0.2)
                time.sleep(1)
                A += 1
                buy_average = float(upbit.get_avg_buy_price(i))
                print("%dnd Buy OK" % (A))
                print("매수평균가 : " + str(buy_average))
            
            ###### 매수 3차 ######
            if  2.5 >= A >= 1.5 and current_price < firstPrice*0.985:
                #### 지정가 매수 ####
                ORDER_PRICE = current_price - hoga_val
                ORDER_SOO = (krw*0.3) / ORDER_PRICE
                ret = upbit.buy_limit_order(i, ORDER_PRICE, ORDER_SOO)
                uuid3 = ret['uuid']
                
                time.sleep(1)
                A += 1
                buy_average = float(upbit.get_avg_buy_price(i))
                print("%drd Buy OK" % (A))
                print("매수평균가 : " + str(buy_average))
            
            ###### 매수 4차 ######
            if  3.5 >= A >= 2.5 and current_price < firstPrice*0.975:
                #### 지정가 매수 ####
                ORDER_PRICE = current_price - hoga_val
                ORDER_SOO = (krw*0.39) / ORDER_PRICE
                ret = upbit.buy_limit_order(i, ORDER_PRICE, ORDER_SOO)
                uuid4 = ret['uuid']
                
                time.sleep(1)
                A += 1
                buy_average = float(upbit.get_avg_buy_price(i))
                print("%drd Buy OK" % (A))
                print("매수평균가 : " + str(buy_average))

            ###### 손절, 익절 목표가 도달시 브레이크 ######
            if (buy_average*0.96 > current_price) or (buy_average *1.005 < current_price):
                useCoin = upbit.get_balance(i)
                upbit.sell_market_order(i, useCoin)
                A = 4
                break
        
        ####### 미체결 지정가 주문 취소 #########
        upbit.cancel_order(uuid3)
        upbit.cancel_order(uuid4)
        
        while True :
            now = datetime.datetime.now()
            start_time = get_start_time("KRW-BTC")
            
            ####### 손절, 익절 조건만족시 일괄매도 ######
            if  1 < 2 :
                useCoin = upbit.get_balance(i)
                upbit.sell_market_order(i, useCoin)
                tiktok += 1
                delete_coin = i
                print("<<<< " + str(i) + " 판매완료 >>>>")
                time.sleep(5)
                print("현재 보유 KRW : " + str(upbit.get_balance("KRW")))
                break
                
            else :
                  current_price = pyupbit.get_current_price(i)
                  buy_average = float(upbit.get_avg_buy_price(i))
                  winrate = ((current_price / buy_average)*100) - 100
                  print("<<<< 구매코인: " + str(i) + " >>>>")
                  print("현재가: " + str(current_price))
                  print("평균구매가: " + str(buy_average))
                  print("수익률: " + str(winrate) + "%")
                  time.sleep(2)
        
        print('판매코인 현재가 : ' + str(pyupbit.get_current_price(i)))
        time.sleep(5)
        
    except Exception as e:
        print(e)
        time.sleep(1)