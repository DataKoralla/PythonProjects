import pandas as pd
from stackapi import StackAPI
import json
import pandas as pd
import os



if __name__ == '__main__':
    python_file = open("example.py", "w")
    SITE = StackAPI('stackoverflow')
    comments = SITE.fetch('users',page=20)
    with open('users.txt', 'w') as json_file:
         json.dump(comments, json_file)
    # df=pd.read_json('person.txt')
    with open('person.txt', 'r') as f:
        data = json.loads(f.read())
    # Flatten data
    df_nested_list = pd.json_normalize(data, record_path=['items'])
    # print(df_nested_list)
    print(df_nested_list.info(verbose=True))
    os.makedirs('output', exist_ok=True)
    df_nested_list.to_csv('output/out.csv')
    df_nested_list.to_excel("output100.xlsx")
