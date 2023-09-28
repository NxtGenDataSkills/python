from NSE import NSE
from Dates import Dates
from os.path import getmtime, getsize

dates = Dates()
nse = NSE()

def downloadNseBhav(nse: NSE,year,folder_month,file_month,dt_str2,exitOnError=True):

    """Download the daily report for Equity bhav copy and
    return the saved file path. Exit if the download fails"""
    
    # dt_str = dates.dt.strftime('%d%b%Y').upper()
    # month = dt_str[2:5].upper()

    url = f'https://archives.nseindia.com/content/historical/EQUITIES/{dates.dt.year}/{month}/cm{dt_str}bhav.csv.zip'
    print(url)
    
    bhavFile = nse.download(url,year,folder_month)

    # if not bhavFile.is_file() or getsize(bhavFile) < 5000:
    #     bhavFile.unlink()
    #     if exitOnError:
    #         exit('Download Failed: ' + bhavFile.name)
    #     else:
    #         raise FileNotFoundError()

    return bhavFile

if __name__ == "__main__":
    
    from datetime import date, timedelta,datetime

    print(datetime.combine(datetime.today(), datetime.min.time()))
    
    start_date = date(2023, 7, 20)
    day_count = 70

    for single_date in (start_date + timedelta(n) for n in range(day_count)):

        folder_month = str(single_date).split("-")[1]
        year = str(single_date).split("-")[0]
        dt_str = single_date.strftime('%d%b%Y').upper()
        print("dt_str : {}".format(dt_str))
        month = dt_str[2:5].upper()
        downloadNseBhav(nse,year,folder_month,month,dt_str)