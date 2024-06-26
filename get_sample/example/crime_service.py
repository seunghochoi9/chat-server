import os
import sys
from dotenv import load_dotenv


sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from crime_model import CrimeModel
from crime_util import Reader
from konlpy.tag import Kkma, Komoran, Okt, Hannanum
from nltk.tokenize import word_tokenize
import konlpy
import nltk
import re
import pandas as pd
from nltk import FreqDist
from wordcloud import WordCloud 
import matplotlib.pyplot as plt
from icecream import ic
import tweepy


'''
문제정의 !
서울시의 범죄현황과 CCTV현황을 분석해서
정해진 예산안에서 구별로 다음해에 배분하는 기준을 마련하시오.
예산금액을 입력하면, 구당 할당되는 CCTV 카운터를 자동으로
알려주는 AI 프로그램을 작성하시오.
'''


class Crime_Service:

    def __init__(self):
        self.data = CrimeModel()
        self.data.cctv = 'cctv_in_seoul.csv'
        self.data.crime = 'crime_in_seoul.csv'
        self.data.sname = 'C:\\Users\\bitcamp\\kubernetes\\chat-server\\get_sample\\example\\save'
        self.data.dname = 'C:\\Users\\bitcamp\\kubernetes\\chat-server\\get_sample\\example\\data'
        self.crime_rate_columns = ['살인검거율', '강도검거율', '강간검거율', '절도검거율', '폭력검거율']
        self.crime_columns = ['살인', '강도', '강간', '절도', '폭력']
        self.arrest_columns = ['살인검거', '강도검거', '강간검거', '절도검거', '폭력검거']

    def new_dataframe_cctv(self) -> pd.DataFrame:
        return pd.read_csv(f'{self.data.dname}\\{self.data.cctv}', encoding='utf-8', thousands=',')
    
    def new_dataframe_crime(self) -> pd.DataFrame:
        return pd.read_csv(f'{self.data.dname}\\{self.data.crime}', encoding='utf-8', thousands=',')


    def save_police_position(self) -> None:
        station_names = []
        crime = self.new_dataframe_crime()
        for name in crime['관서명']:
            station_names.append('서울' + str(name[:-1]) + '경찰서')
        station_address = []
        station_lats = []
        station_lngs = []
        reader = Reader()
        gmaps = reader.gmaps()
        for name in station_names:
            t = gmaps.geocode(name, language='ko')
            print(t)
            station_address.append(t[0].get("formatted_address"))   
            t_loc = t[0].get("geometry")
            station_lats.append(t_loc['location']['lat'])
            station_lngs.append(t_loc['location']['lng'])

        gu_names = []
        for name in station_address:
            tmp = name.split()
            tmp_gu = [gu for gu in tmp if gu[-1] == '구'][0]
            gu_names.append(tmp_gu)
        
        crime['구별'] = gu_names
        # 구 와 경찰서의 위치가 다른 경우 수작업
        crime.loc[crime['관서명'] == '혜화서', ['구별']] = '종로구'
        crime.loc[crime['관서명'] == '서부서', ['구별']] = '은평구'
        crime.loc[crime['관서명'] == '강서서', ['구별']] = '양천구'
        crime.loc[crime['관서명'] == '종암서', ['구별']] = '성북구'
        crime.loc[crime['관서명'] == '방배서', ['구별']] = '서초구'
        crime.loc[crime['관서명'] == '수서서', ['구별']] = '강남구'
        crime.to_csv(f'{self.data.sname}\\police_position.csv')


if __name__ == "__main__":
    crime = Crime_Service()
    ic(crime.new_dataframe_cctv())
    ic(crime.new_dataframe_crime())
    ic(crime.save_police_position())


