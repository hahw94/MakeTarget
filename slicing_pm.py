'''
region_name에 지역 이름을 쓰면 지역명,연월일,PM10,Pm25 순으로 정렬되어 나온다.
'''

import pandas as pd
import torch
import numpy as np

def is_work():
    print("working")

def get_region_data(total_dataset, region_name=None, Normalize=False):
    num = 366 * 24
    region_data = total_dataset[total_dataset['지역'] == region_name]
    if len(region_data) % 366 != 0:
        return print('Exist missing value')
    data_list = []
    for YMD in total_dataset['측정일시']:
        YMD = str(YMD)
        data = YMD[:8]
        data_list.append(int(data))
    date = pd.DataFrame(data_list)
    region_data['연월일'] = date
    temp_group = region_data.groupby(['지역', '연월일'])
    df = temp_group.sum()
    df['PM25'] = df['PM25'] / 24
    df['PM10'] = df['PM10'] / 24
    if (len(total_dataset[total_dataset['지역'] == region_name]) / num) > 1:
        df['PM25'] = df['PM25'] / len(total_dataset[total_dataset['지역'] == region_name]) * num
        df['PM10'] = df['PM10'] / len(total_dataset[total_dataset['지역'] == region_name]) * num
    df = df.reset_index()
    df = df[['지역', '연월일', 'PM10', 'PM25']]
    df['PM10'][df['PM10'] == 0]
    df['PM10'] = df['PM10'].interpolate()
    df['PM25'] = df['PM25'].interpolate()
    if Normalize == True:
        df['PM10'] = (df['PM10'] - df['PM10'].mean()) / df['PM10'].std()
        df['PM25'] = (df['PM25'] - df['PM25'].mean()) / df['PM25'].std()

    return df


def region_data_to_tensor(total_dataset, region_list, extract_type, Normalize = False):
    count = 0
    for region_name in region_list:
        df = get_region_data(total_dataset, region_name, Normalize)
        target_data = torch.tensor(df[extract_type]).view(366, -1)
        if count >= 1 :
            previous_data = np.c_[previous_data, target_data]
        if count == 0:
            previous_data = np.array(target_data)
            count += 1
    return previous_data