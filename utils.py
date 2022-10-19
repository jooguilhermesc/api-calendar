import pandas as pd
from datetime import datetime

class workdays_calendar:
    
    def __init__(self, start='2017-12-01', end = datetime.today().strftime('%Y-%m-%d')):
        self.start = start 
        self.end = end 
        self.url = 'calendario.csv' #'https://docs.google.com/spreadsheets/d/e/2PACX-1vTtYOgUPr8G8kWqXlqXDZ_-6_0mzPxGq_WPUqglOan50uUYa8L1QA1E9ZjxAWqNLGBhUX3YxleOw_ja/pub?output=csv'
        
    def holidays(self):
        holidays = pd.read_csv(self.url,encoding='utf-8')
        df = list(holidays["dt_feriado"])

        return df
    
    def create_date_table(self):
        df = pd.DataFrame({"Date": pd.date_range(self.start, self.end)})
        df["Day"] = df.Date.dt.dayofweek
        df["Week"] = df.Date.dt.isocalendar().week
        df["Month"] = df.Date.dt.month
        df["Quarter"] = df.Date.dt.quarter
        df["Year"] = df.Date.dt.year
        df["Year_half"] = (df.Quarter + 1) // 2
        
        lista_feriados = self.holidays()
        df["workday"] = df.apply(lambda x: 0 if (x.Date.strftime('%d-%m') in lista_feriados) or (x.Day in (0,6)) else 1,axis=1)
            
        return df