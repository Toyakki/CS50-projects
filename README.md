# CS50-projects
I completed CS50 course in January 1st, 2023. I would show my basic final projects that I worked on. Please enjoy!

## EZ Stock information scraper ref from:https://stooq.com/q/d/?s=4784.jp

## Video Demo:
https://youtu.be/G5q6GGRXnAE

## Background:
Stock price acquisition is easy. Simply specify the type of original data, the period covered, and the stock code. Let's try to get the stock price of GMO Ad Partners (4784) for this year.There are two types of source data that can be used to obtain Japanese stock prices, stooq and Yahoo.Stooq is a Polish site and seems to be able to retrieve information from the following site.https://stooq.com/q/d/?s=4784.jpYahoo(U.S.A.)This site is not YAHOO!(yahoo.co.jp) in Japan, but YAHOO(finance.yahoo.com) in the US. https://finance.yahoo.com/quote/4784.T/history?p=4784.T

## Caution:
Both of these sites offer free CSV downloads from their homepages, so even if you cannot write a program, you can download the data from their homepages and obtain it. In Japan, there is often a charge for this service, so I think this is very conscientious. In this program, I only used stooq website as a reference.

## Code description
Now, I will describe how to get the stock price data from both sites in python. The values that can be obtained are as follows. * Date * Open

High
Low
Close
Volume Adj Close Adjusted Close (Yahoo Finance only) Now, let's try to get the stock price. How to get stock quotes with stooq The following is how to get the stock price with stooq. The stock code is added because it is difficult to use it for later analysis.
So this time, we have introduced the method of acquiring stock price data. This time, we used pandas_datareader to acquire stock prices, but it seems that you can also acquire economic indicators, financial statements, and national statistical data other than stock prices. If you are interested in other indicators or statistical data, please refer to the following pandas_datareader explanation page. https://pandas-datareader.readthedocs.io/en/latest/index.html

## What is pandas_datareader?
It is a library that can retrieve stock prices, economic indicators, financial statements, and national statistical data.

How to obtain stock prices on stooq
The following is the method of acquiring stock prices on stooq. We have added the code of the stock since it is difficult to use it for analysis later.

import os import datetime as dt import pandas_datareader.data as web os.getcwd() os.listdir(os.getcwd())

#input ticker symbol ticker_symbol= input("Enter ticker_symbol you are interested in: ")

ticker_symbol_dr=ticker_symbol + ".JP"

Record stock price from 2022-01-01
start='2022-01-01' end = dt.date.today()

Obtain datas
df = web.DataReader(ticker_symbol_dr, data_source='stooq', start=start,end=end)

Adding ticker_symbol from the second row
df.insert(0, "code", ticker_symbol, allow_duplicates=False)

Save csv
df.to_csv('stock_data_'+ ticker_symbol + '.csv')

print("Sucessfully saved!")

The following data can be obtained using stooq. If you do not specify any sorting, the data is sorted by date in descending order.

Date,code,Open,High,Low,Close,Volume 2022-12-29,7177,500,508,500,508,324400 2022-12-28,7177,510,511,501,503,539700 2022-12-27,7177,502,513,502,512,546100 2022-12-26,7177,504,506,497,500,703800 2022-12-23,7177,505,508,501,505,384000 2022-12-22,7177,508,510,504,506,446500 2022-12-21,7177,514,515,505,506,431700 2022-12-20,7177,520,521,511,515,731100 2022-12-19,7177,527,529,517,520,427300 2022-12-16,7177,531,531,526,529,304100 2022-12-15,7177,528,532,525,529,324000 2022-12-14,7177,519,531,519,528,435500 2022-12-13,7177,521,521,517,519,317700 2022-12-12,7177,522,525,519,519,214900 2022-12-09,7177,519,523,517,523,326600 2022-12-08,7177,525,525,516,518,613300 2022-12-07,7177,528,531,523,524,300200 2022-12-06,7177,533,535,525,527,306900 2022-12-05,7177,539,539,527,531,490600 2022-12-02,7177,532,541,532,539,444900 2022-12-01,7177,529,536,527,535,393500 2022-11-30,7177,529,529,522,525,1080800 2022-11-29,7177,528,538,525,529,1045700 2022-11-28,7177,536,539,529,535,356000 2022-11-25,7177,536,541,533,536,313300 2022-11-24,7177,526,536,525,535,423400 2022-11-22,7177,520,533,516,533,676600 2022-11-21,7177,535,536,519,522,752700 2022-11-18,7177,544,544,534,538,393100 2022-11-17,7177,542,544,537,542,307900 2022-11-16,7177,553,553,542,542,423500 2022-11-15,7177,552,558,551,555,180400 2022-11-14,7177,566,571,552,552,531000 2022-11-11,7177,569,570,562,565,285500 2022-11-10,7177,558,565,555,559,227300 2022-11-09,7177,572,572,565,566,186200 2022-11-08,7177,559,572,558,566,336700 2022-11-07,7177,553,559,546,556,370400 2022-11-04,7177,551,558,547,552,504500 2022-11-02,7177,581,583,554,556,982300 2022-11-01,7177,576,581,570,576,320200 2022-10-31,7177,570,577,562,571,660400 2022-10-28,7177,580,584,571,571,692400 2022-10-27,7177,602,609,572,578,1611000 2022-10-26,7177,627,632,609,609,2089100 2022-10-25,7177,710,714,708,711,64500 2022-10-24,7177,714,715,708,709,95200 2022-10-21,7177,715,716,708,714,68100 2022-10-20,7177,718,719,710,710,112900 2022-10-19,7177,715,719,712,718,93100 2022-10-18,7177,710,715,708,709,117500 2022-10-17,7177,707,710,702,707,207000 2022-10-14,7177,705,714,703,714,152600 2022-10-13,7177,702,702,697,699,100300 2022-10-12,7177,702,705,700,700,106000 2022-10-11,7177,707,709,702,702,138200 2022-10-07,7177,715,717,712,715,86200 2022-10-06,7177,718,723,716,718,91600 2022-10-05,7177,719,722,716,718,76100 2022-10-04,7177,711,720,710,720,117600 2022-10-03,7177,711,712,693,708,248500 2022-09-30,7177,712,719,711,716,111200 2022-09-29,7177,710,721,710,721,126000 2022-09-28,7177,731,731,711,722,275600 2022-09-27,7177,726,734,726,729,80200 2022-09-26,7177,730,736,724,726,199200 2022-09-22,7177,733,737,727,737,169600 2022-09-21,7177,737,739,735,735,69900 2022-09-20,7177,738,741,735,741,108600 2022-09-16,7177,737,740,736,739,50500 2022-09-15,7177,743,743,737,737,75400 2022-09-14,7177,735,743,731,743,103100 2022-09-13,7177,743,743,737,741,101600 2022-09-12,7177,735,741,734,741,100700 2022-09-09,7177,727,733,727,731,121200 2022-09-08,7177,727,728,720,728,226400 2022-09-07,7177,742,743,722,725,376200 2022-09-06,7177,740,742,740,742,46300 2022-09-05,7177,743,744,735,739,218400 2022-09-02,7177,753,754,742,744,197600 2022-09-01,7177,756,756,750,750,267600 2022-08-31,7177,756,759,753,759,255800 2022-08-30,7177,758,764,758,761,166500 2022-08-29,7177,755,760,752,758,149600 2022-08-26,7177,762,764,758,761,169800 2022-08-25,7177,759,763,758,760,109400 2022-08-24,7177,764,765,759,760,182900 2022-08-23,7177,762,765,761,764,102200 2022-08-22,7177,765,769,762,768,93600 2022-08-19,7177,773,773,765,769,161200 2022-08-18,7177,770,773,768,772,60900 2022-08-17,7177,768,773,767,769,128600 2022-08-16,7177,768,768,764,768,64300 2022-08-15,7177,767,768,764,768,61000 2022-08-12,7177,767,767,763,766,83300 2022-08-10,7177,764,765,760,761,83000 2022-08-09,7177,768,769,765,766,53800 2022-08-08,7177,763,769,762,768,115000 2022-08-05,7177,755,763,755,762,105200 2022-08-04,7177,760,761,755,760,129300 2022-08-03,7177,756,760,754,760,139200 2022-08-02,7177,775,777,751,755,585500 2022-08-01,7177,786,786,776,781,144500 2022-07-29,7177,786,786,778,784,95800 2022-07-28,7177,782,786,778,786,91400 2022-07-27,7177,782,786,779,781,65300 2022-07-26,7177,777,788,775,787,164000 2022-07-25,7177,789,790,784,785,82900 2022-07-22,7177,789,791,786,790,96600 2022-07-21,7177,788,790,785,790,105600 2022-07-20,7177,781,788,779,788,192100 2022-07-19,7177,773,777,771,776,54100 2022-07-15,7177,774,775,768,772,100700 2022-07-14,7177,773,778,769,778,91000 2022-07-13,7177,772,777,771,774,37200 2022-07-12,7177,776,780,769,771,109300 2022-07-11,7177,782,783,777,778,119100 2022-07-08,7177,774,783,772,781,196100 2022-07-07,7177,774,779,772,777,111000 2022-07-06,7177,776,778,772,777,73500 2022-07-05,7177,769,776,769,776,75400 2022-07-04,7177,765,771,765,769,106600 2022-07-01,7177,772,773,764,764,155900 2022-06-30,7177,776,778,771,777,106300 2022-06-29,7177,778,779,764,777,464800 2022-06-28,7177,790,795,785,791,388100 2022-06-27,7177,798,801,789,796,238300 2022-06-24,7177,787,796,780,796,245100 2022-06-23,7177,776,784,774,784,182400 2022-06-22,7177,774,776,769,770,142000 2022-06-21,7177,768,771,764,768,182700 2022-06-20,7177,777,781,761,764,201100 2022-06-17,7177,773,780,770,777,250400 2022-06-16,7177,779,787,778,781,158300 2022-06-15,7177,784,785,775,781,109400 2022-06-14,7177,770,777,769,775,149600 2022-06-13,7177,783,785,778,782,178900 2022-06-10,7177,791,792,786,792,132200 2022-06-09,7177,798,798,790,791,127600 2022-06-08,7177,797,797,793,794,122000 2022-06-07,7177,795,797,794,794,72700 2022-06-06,7177,796,797,791,796,124700 2022-06-03,7177,800,801,792,796,299400 2022-06-02,7177,790,799,788,797,231300 2022-06-01,7177,785,792,778,789,226700 2022-05-31,7177,790,791,777,777,379300 2022-05-30,7177,783,791,780,791,215700 2022-05-27,7177,770,780,770,775,292900 2022-05-26,7177,755,766,755,759,140600 2022-05-25,7177,755,762,754,762,122900 2022-05-24,7177,771,772,758,758,192500 2022-05-23,7177,761,768,759,765,153400 2022-05-20,7177,747,758,742,754,348700 2022-05-19,7177,756,758,746,749,367500 2022-05-18,7177,768,772,760,764,228000 2022-05-17,7177,765,772,760,768,284700 2022-05-16,7177,781,782,762,765,344300 2022-05-13,7177,771,784,769,782,242700 2022-05-12,7177,784,787,773,774,344600 2022-05-11,7177,793,797,786,786,163400 2022-05-10,7177,793,797,787,795,212700 2022-05-09,7177,804,806,795,799,206500 2022-05-06,7177,810,811,800,804,200500 2022-05-02,7177,804,812,801,804,214000 2022-04-28,7177,807,811,799,808,182000 2022-04-27,7177,800,808,798,808,146000 2022-04-26,7177,812,812,802,808,93400 2022-04-25,7177,810,811,803,807,217900 2022-04-22,7177,823,823,814,816,188000 2022-04-21,7177,832,832,824,828,96500 2022-04-20,7177,832,834,826,827,181400 2022-04-19,7177,822,831,821,829,160300 2022-04-18,7177,822,826,816,817,118400 2022-04-15,7177,824,831,823,827,88500 2022-04-14,7177,825,829,823,829,118800 2022-04-13,7177,827,827,822,823,116200 2022-04-12,7177,820,829,820,823,130400 2022-04-11,7177,834,837,824,831,151800 2022-04-08,7177,823,832,822,832,162000 2022-04-07,7177,825,831,821,821,143000 2022-04-06,7177,835,843,833,838,193500 2022-04-05,7177,848,850,837,846,296800 2022-04-04,7177,832,847,827,846,442800 2022-04-01,7177,821,826,814,822,144700 2022-03-31,7177,830,832,820,823,198500 2022-03-30,7177,830,837,823,837,284500 2022-03-29,7177,821,841,819,841,407700 2022-03-28,7177,819,821,815,818,138100 2022-03-25,7177,820,821,814,815,187700 2022-03-24,7177,811,818,808,817,183800 2022-03-23,7177,813,820,809,820,281300 2022-03-22,7177,806,813,805,808,297800 2022-03-18,7177,804,809,802,807,181300 2022-03-17,7177,815,815,804,807,175800 2022-03-16,7177,804,810,801,803,101200 2022-03-15,7177,803,805,799,803,80400 2022-03-14,7177,801,808,799,800,133200 2022-03-11,7177,793,806,793,806,145700 2022-03-10,7177,798,804,794,804,215900 2022-03-09,7177,778,792,778,784,192600 2022-03-08,7177,785,795,777,778,313400 2022-03-07,7177,794,797,785,791,261700 2022-03-04,7177,810,814,797,800,305500 2022-03-03,7177,806,817,806,813,162000 2022-03-02,7177,809,810,801,805,151500 2022-03-01,7177,819,821,812,812,246800 2022-02-28,7177,800,813,799,813,209200 2022-02-25,7177,792,802,792,802,208000 2022-02-24,7177,795,804,784,788,417200 2022-02-22,7177,793,803,790,802,198500 2022-02-21,7177,802,804,794,800,237900 2022-02-18,7177,803,812,800,809,206400 2022-02-17,7177,816,821,808,811,285800 2022-02-16,7177,805,816,804,816,356300 2022-02-15,7177,815,818,798,800,574000 2022-02-14,7177,825,826,810,817,415700 2022-02-10,7177,832,835,826,830,248100 2022-02-09,7177,829,832,825,832,182200 2022-02-08,7177,840,840,823,827,292500 2022-02-07,7177,819,839,819,834,384200 2022-02-04,7177,828,840,815,824,962700 2022-02-03,7177,863,863,840,843,431900 2022-02-02,7177,854,864,851,864,204200 2022-02-01,7177,857,858,843,843,262700 2022-01-31,7177,849,856,842,853,226100 2022-01-28,7177,828,845,828,844,284800 2022-01-27,7177,840,845,819,825,412100 2022-01-26,7177,830,839,828,837,181100 2022-01-25,7177,843,847,825,831,566100 2022-01-24,7177,844,855,839,853,339400 2022-01-21,7177,849,856,842,854,400200 2022-01-20,7177,850,866,848,859,238300 2022-01-19,7177,866,873,851,855,348300 2022-01-18,7177,880,889,874,877,209300 2022-01-17,7177,888,891,875,880,194300 2022-01-14,7177,887,891,876,885,307600 2022-01-13,7177,874,891,872,889,289700 2022-01-12,7177,880,885,874,876,205400 2022-01-11,7177,859,880,859,880,323400 2022-01-07,7177,863,872,858,866,511200 2022-01-06,7177,855,859,845,851,438000 2022-01-05,7177,856,865,850,864,337800 2022-01-04,7177,855,859,846,852,368600

## About CS50
CS50 is a openware course from Havard University and taught by David J. Malan

Introduction to the intellectual enterprises of computer science and the art of programming. This course teaches students how to think algorithmically and solve problems efficiently. Topics include abstraction, algorithms, data structures, encapsulation, resource management, security, and software engineering. Languages include C, Python, and SQL plus students’ choice of: HTML, CSS, and JavaScript (for web development).

Thank you for all CS50.

Where I get CS50 course? https://cs50.harvard.edu/x/2020/
