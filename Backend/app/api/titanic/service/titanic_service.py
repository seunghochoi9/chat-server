from app.api.titanic.model.titanic_model import TitanicModel
import pandas as pd


class TitanicService:

    model = TitanicModel()

    def process(self):
        print(f'프로세스 시작')
        this = self.model
        this.train = self.new_model('train.csv')
        this.test = self.new_model('test.csv')
        print(f'트레인 컬럼 : {this.train.columns}')
        print(f'테스트 컬럼 : {this.test.columns}')
        this.id = this.test['PassengerId']

        this = self.drop_feature(this, 'Ticket', 'Name', 'Embarked', 'Cabin')

        self.df_info(this)


        this = self.create_train(this)

    @staticmethod
    def drop_feature(this, *feature) -> object:
        # for i in feature:
        #     this.train = this.train.drop([i], axis=1)
        #     this.test = this.test.drop([i], axis=1)
        # for i in [this.train, this.test]:
        #     for j in feature:
        #         i.drop(j, axis=1, inplace=True)
        [i.drop(j, axis=1, inplace=True) for j in feature for i in [this.train, this.test]] 
        return this
    
    @staticmethod
    def df_info(this):
        [print(f'테스트 상세 정보 :\n{i}') for i in [this.train, this.test]]
        return this
        


    def new_model(self, payload) -> object:
        this = self.model
        this.context = './app/api/titanic/data/'
        this.fname = payload
        return pd.read_csv(this.context + this.fname)
    
    @staticmethod
    def create_train(this) -> str:
        return this.train.drop('Survived', axis=1) # 0: 행, 1: 열
    
    @staticmethod
    def create_label(this) -> str:
        return this.train['Survived']
    
