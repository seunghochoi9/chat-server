from app.api.titanic.model.titanic_model import TitanicModel
import pandas as pd


class TitanicService:

    model = TitanicModel()

    def process(self):
        print(f'프로세스 시작')
        this = self.model
        feature = ['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp', 'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked']
        this.train = self.new_model('train.csv')
        this.test = self.new_model('test.csv')
        print(f'트레인 컬럼 : {this.train.columns}')
        print(f'테스트 컬럼 : {this.test.columns}')
        this.id = this.test['PassengerId']

        this = self.name_nominal(this)
        this = self.drop_feature(this, 'Name', 'Parch', 'SibSp', 'Ticket', 'Cabin')
        this = self.create_train(this)
        self.df_info(this)
        this = self.pclass_ordinal(this)
        this = self.sex_nominal(this)
        this = self.age_ratio(this)
        this = self.fare_ratio(this)
        this = self.embarked_ordinal(this)
        self.df_info(this)




    
    def df_info(self, this):
        [print(f'테스트 상세 정보 : {i}') for i in [this.train, this.test]]


    
    @staticmethod
    def create_train(this) -> str:
        return this.train.drop('Survived', axis=1) # 0: 행, 1: 열
    
    @staticmethod
    def create_label(this) -> str:
        return this.train['Survived']
    
    # ['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp', 'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked']
    
    @staticmethod
    def pclass_ordinal(this) -> object:
        return this
    
    @staticmethod
    def sex_nominal(this) -> object:
        return this
    
    @staticmethod
    def age_ratio(this) -> object:
        return this
    
    @staticmethod
    def fare_ratio(this) -> object:
        return this
    
    @staticmethod
    def embarked_ordinal(this) -> object:
        return this
    
    @staticmethod
    def name_nominal(this) -> object:
        return this
    
    @staticmethod
    def extract_title(this) -> object:
        combine = [this.train, this.test]
        for i in combine:
            i['Title'] = i['Name'].str.extract('([A-Za-z]+)\.')
        return this