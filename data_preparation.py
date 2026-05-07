import os
import json

def precheck_datageneration(model_name, row_numbers, data_type):
    file_exnsion = model_name.split('.')[1]
    if file_exnsion == "pkl":
        if isinstance(row_numbers, int):
            if row_numbers > 0:
                if data_type == 'SingleTable':
                    model_file_path = os.getcwd() + "/" + model_name
                    path = os.path.exists(model_file_path)

                    if path:
                        dataset = {'Status': 'Success', 'Message': "File " + model_name + " is present",
                                   'Result': " "}
                    else:
                        dataset = {'Status': 'Failed', 'Message': "File " + model_name + " is not present",
                                   'Result': " "}
                elif data_type == 'MultiTable':
                    model_file_path = os.getcwd() + "/" + model_name
                    path = os.path.exists(model_file_path)
                    if path:
                        dataset = {'Status': 'Success', 'Message': "File " + model_name + " is present",
                                   'Result': " "}
                    else:
                        dataset = {'Status': 'Failed', 'Message': "File " + model_name + " is not present",
                                   'Result': " "}
                else:
                    dataset = {'Status': 'Failed',
                               'Message': data_type + " is not a valid Out put Data Use MultiTable or SingleTable",
                               'Result': " "}
            else:
                dataset = {'Status': 'Failed', 'Message': "File " + model_name + " insufficient Data", 'Result': " "}
        else:
            dataset = {'Status': 'Failed', 'Message': "Number of rows allowed only integer value" , 'Result': " "}
    else:
        dataset = {'Status': 'Failed', 'Message': "Model type is Only .pkl", 'Result': " "}
    return dataset

if __name__ == '__main__':
    model_name = "Datagen_01.pkl"
    row_numbers = 100
    data_type = "SingleTable"
    dataset = precheck_datageneration(model_name, row_numbers, data_type)
    json_str = json.dumps(dataset, indent=4)
    print(json_str)
