import pickle
import json
import config
import numpy as np

class MedicalInsurence():
    def __init__(self,age, sex, bmi,children,smoker, region):
        self.age = age
        self.sex = sex
        self.bmi =bmi
        self.children = children
        self.smoker = smoker
        self.region = 'region_'+  region

    def load_model(self):
        with open(config.MODEL_FILE_PATH,'rb') as f:
            self.model = pickle.load(f)

        with open(config.JSON_FILE_PATH,'r') as f:
            self.json_data = json.load(f)

    def get_predicted_charges(self):
        self.load_model()
        print("*"*30,self.json_data)
        region_index = self.json_data['columns'].index(self.region)

        test_array = np.zeros(len(self.json_data['columns']))
        test_array[0] = self.age
        test_array[1] = self.json_data['sex'][self.sex]
        test_array[2] = self.bmi
        test_array[3] = self.children
        test_array[4] = self.json_data['smoker'][self.smoker]
        test_array[region_index] = 1

        print("Test Array :",test_array) # 9 values

        predicted_charges = np.around(self.model.predict([test_array])[0],2)
        return predicted_charges

if __name__ == "__main__":
    age = 54.0
    sex = 'male'
    bmi = 28.3
    children = 3
    smoker = 'yes'
    region = 'southeast'

    med_ins = MedicalInsurence(age, sex, bmi,children,smoker, region)
    med_ins.get_predicted_charges()