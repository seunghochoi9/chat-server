import pandas as pd
pd.set_option('display.max_rows', 10000)
import numpy as np
from icecream import ic
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import KFold, cross_val_score

from app.api.context.domains import DataSets
from app.api.context.models import Models


class TitanicModel(object):
    model = Models()
    dataset = DataSets()

    def preprocess(self, train_fname, test_fname) -> pd.DataFrame:
        this = self.dataset
        that = self.model
        feature = ['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp', 'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked']
        this.train = that.new_dataframe_no_index(train_fname)
        this.test = that.new_dataframe_no_index(test_fname)
        this.id = this.test['PassengerId']
        this.label = this.train['Survived']
        this = self.drop_train_feature(this, 'Survived')
        this = self.drop_feature(this, 'Parch', 'SibSp', 'Ticket', 'Cabin')
        this = self.extract_title_from_name(this)
        title_mapping = self.remove_duplicate_title(this)
        this = self.title_nominal(this, title_mapping)
        this = self.drop_feature(this, 'Name')  
        this = self.sex_nominal(this)
        this = self.drop_feature(this, 'Sex')
        this = self.embraked_nominal(this)

        this = self.age_ratio(this)
        this = self.drop_feature(this, 'Age')

        this = self.fare_ratio(this)
        this = self.drop_feature(this, 'Fare')

        self.df_info(this)

        return this
    

    @staticmethod
    def new_dataframe_no_index(this) -> pd.DataFrame:
        return pd.read_csv(f'{this.dataset.context}/{this.dataset.fname}')

    @staticmethod
    def drop_feature(this, *feature) -> pd.DataFrame:
        # for i in feature:
        #     this.train = this.train.drop([i], axis=1)
        #     this.test = this.test.drop([i], axis=1)
        # for i in [this.train, this.test]:
        #     for j in feature:
        #         i.drop(j, axis=1, inplace=True)
        [i.drop(j, axis=1, inplace=True) for j in feature for i in [this.train, this.test]] 
        return this
    
    @staticmethod
    def drop_train_feature(this, feature) -> pd.DataFrame:
        this.train.drop(feature, axis=1, inplace=True)
        return this
    
    @staticmethod
    def extract_title_from_name(this) -> pd.DataFrame:
        for i in [this.train, this.test]:
            i['Title'] = i['Name'].str.extract('([A-Za-z]+)\.', expand=False)
        return this
    
    @staticmethod
    def remove_duplicate_title(this) -> pd.DataFrame:
        a = []
        for these in [this.train, this.test]:
            a += list(set(these['Title']))
        
        a = list(set(a))
        print(a)
        '''
        ['Mr', 'Sir', 'Major', 'Don', 'Rev', 'Countess', 'Lady', 'Jonkheer', 'Dr',
        'Miss', 'Col', 'Ms', 'Dona', 'Mlle', 'Mme', 'Mrs', 'Master', 'Capt']
        Royal : ['Countess', 'Lady', 'Sir']
        Rare : ['Capt','Col','Don','Dr','Major','Rev','Jonkheer','Dona','Mme' ]
        Mr : ['Mlle']
        Ms : ['Miss']
        Master
        Mrs
        '''
        title_mapping = {'Mr':1, 'Ms':2, 'Mrs':3, 'Master':4, 'Royal':5, 'Rare':6}
        return title_mapping
    
    @staticmethod
    def title_nominal(this, title_mapping) -> None:
        for these in [this.train, this.test]:
            these['Title'] = these['Title'].replace(['Countess', 'Lady', 'Sir'], 'Royal')
            these['Title'] = these['Title'].replace(['Capt','Col','Don','Dr','Major','Rev','Jonkheer','Dona','Mme'], 'Rare')
            these['Title'] = these['Title'].replace(['Mlle'], 'Mr')
            these['Title'] = these['Title'].replace(['Miss'], 'Ms')
            # Master 는 변화없음
            # Mrs 는 변화없음
            these['Title'] = these['Title'].fillna(0)
            these['Title'] = these['Title'].map(title_mapping)
        return this
        
    @staticmethod
    def age_ratio(this) -> pd.DataFrame:
        train = this.train
        test = this.test
        age_mapping = {'Unknown':0 , 'Baby': 1, 'Child': 2, 'Teenager' : 3, 'Student': 4,
                       'Young Adult': 5, 'Adult':6,  'Senior': 7}
        train['Age'] = train['Age'].fillna(-0.5)
        test['Age'] = test['Age'].fillna(-0.5) # 왜 NaN 값에 -0.5 를 할당할까요 ?
        bins = [-1, 0, 5, 12, 18, 24, 35, 60, np.inf] # 이것을 이해해보세요
        labels = ['Unknown', 'Baby', 'Child', 'Teenager', 'Student', 'Young Adult', 'Adult', 'Senior']

        for these in train, test:
            pass # pd.cut()을 사용하시오. 다른 곳은 고치지 말고 다음 두줄만 완성하시오.
            these['Age'] = pd.cut(these['Age'], bins, labels=labels)
            these['AgeGroup'] = these['Age'].map(age_mapping) # map() 사용
        return this
    
    @staticmethod
    def sex_nominal(this) -> pd.DataFrame:
        gender_mapping = {'male':0, 'female':1}
        for these in [this.train, this.test]:
            these['Gender'] = these['Sex'].map(gender_mapping)
        return this
    

    @staticmethod
    def embraked_nominal(this) -> pd.DataFrame:
        embarked_mapping = {'S':1, 'C':2, 'Q':3, 'NaN':0}
        for these in [this.train, this.test]:
            these['Embarked'] = these['Embarked'].fillna('NaN')
            these['Embarked'] = these['Embarked'].map(embarked_mapping)
        return this
    
    @staticmethod
    def fare_ratio(this) -> pd.DataFrame:
        bins = [-1, 8, 15, 31, np.inf]
        labels=['Unknown', 'Low', 'Mid', 'High']
        fare_mapping = {'Unknown':0, 'Low':1, 'Mid':2, 'High':3}
        for these in [this.train, this.test]:
            these['FareBand'] = pd.cut(these['Fare'], bins, labels=labels)
            these['FareBand'] = these['FareBand'].map(fare_mapping)
            these['FareBand'] = these['FareBand'].fillna(0)

        return this
          
    def learning(self, train_fname, test_fname) -> pd.DataFrame:
        this = self.preprocess(train_fname, test_fname)
        print(f'학습 시작')
        k_fold = self.create_k_fold()
        accuracy = self.get_accuracy(this, k_fold)
        ic(f'사이킷런 알고리즘 정확도: {accuracy}')
        return accuracy
        
    @staticmethod
    def create_k_fold() -> object:
        return KFold(n_splits=10, shuffle=True, random_state=0)

    @staticmethod
    def get_accuracy(this, k_fold) -> object:
        score = cross_val_score(RandomForestClassifier(), this.train, 
                                this.label, cv=k_fold, n_jobs=1, scoring='accuracy')
        return round(np.mean(score)*100, 2)


    def df_info(self, this):
        ic('='*50)
        ic(type(this.train))
        ic(this.train.columns)
        ic(this.train)
        ic(this.train.isnull().sum())
        ic(type(this.test))
        ic(this.test.columns)
        ic(this.test.head())
        ic(this.test.isnull().sum())
        ic('='*50)
