import os
import importData
import glob
import slicing_pm
import numpy as np



def MakeData(region_list):
    directory = "C:\\Users\\hahw9\\OneDrive - edy\\Coding\\DUST\\PreProcessing(for Target)\\PM Data(Target Data)\\Dataset"
    # 에어코리아 4분기 데이터(4개)가 들어있는 디렉토리 경로명을 지정해준다.
    os.chdir(directory)
    data = glob.glob("*")
    for i in range(len(data)):
        data[i] = os.getcwd() + "\\" + data[i]
    # 위에서 지정해준 디렉토리에 들어가 해당 데이터의 경로를 뽑아온다.

    temp = importData.importData(data[0], data[1], data[2], data[3])
    # 뽑아온 데이터의 경로에서 데이터를 불러오는 역할을 하고 importData 클래스에 있는대로 concat을 해주어 데이터가 합쳐지게 된다.

    print(len(temp.total_dataset))
    # 합쳐진 데이터의 개수 확인 가능

    data = slicing_pm.region_data_to_tensor(temp.total_dataset, region_list, "PM10", Normalize=False)

    return data

def save_data(data, filename ,save_path = None):
    save_data = data
    np.save(save_path + "\\" +filename, save_data)


#save_data(data, "saving", save_path ="/")
#temp = MakeData(['서울','대전 유성구'])
#print(temp)