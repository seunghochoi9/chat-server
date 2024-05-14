import pandas as pd
from Backend.app.api.context.domains import DataSets


class Models:

    def __init__(self) -> None:
        self.ds = DataSets()
        this = self.ds
        this.dname = './data'
        this.sname = './data'
        this.context = './app/api/titanic/data'

    def new_model(self, fname) -> object:
        this = self.ds
        # index_col=0 해야 기존 index 값이 유지된다.
        # 0 은 컬럼명 중에서 첫번째를 의미한다.(배열구조)
        # pd.read_csv(f'경로/파일명/csv', index_col=0 = '인덱스로 지정할 column 명') Index 지정


        return pd.read_csv(f'{this.dname}{fname}', index_col=0)
    
    def new_dframe(self, fname) -> object:
        this = self.ds
        # pd.read_csv('경로/파일명.csv') Index를 지정하지 않음
        return pd.DataFrame(f'{this.dname}{fname}')
    
    def save_model(self, fname, dframe) -> object:
        this = self.ds
        '''
        풀옵션은 다음과 같다.
        df.to_csv(f'{self.ds.sname}{fname}',sep=',',na_rep='NaN',
                         float_format='%.2f',                        # 2 decimal places
                         columns=['ID', 'X2'],                       # columns to write
                         index=False)                                # do not write index
        '''
        return dframe.to_csv(f'{this.sname}{fname}', sep=',', na_rep='NaN')