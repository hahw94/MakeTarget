import pandas as pd


class importData:
    def __init__(self, path_1, path_2, path_3, path_4):
        self.path_1 = path_1
        self.path_2 = path_2
        self.path_3 = path_3
        self.path_4 = path_4
        dataset_1 = pd.read_csv(self.path_1, encoding='euc-kr', index_col='지역')
        dataset_2 = pd.read_csv(self.path_2, encoding='euc-kr', index_col='지역')
        dataset_3 = pd.read_csv(self.path_3, encoding='euc-kr', index_col='지역')
        dataset_4 = pd.read_csv(self.path_4, encoding='euc-kr', index_col='지역')
        total_dataset = pd.concat([dataset_1, dataset_2, dataset_3, dataset_4])
        total_dataset = total_dataset.reset_index()
        self.total_dataset = total_dataset
        # 에어코리아 4분기 데이터 기준으로 해당 파일의 경로를 path_1~4에 넣고 불러오면 total_dataset에 4개의 파일을 합쳐서 저장하게 된다.



    def check_region(self):
        return self.total_dataset['지역'].unique()
    # 합친 파일들의 지역명을 불러온다.