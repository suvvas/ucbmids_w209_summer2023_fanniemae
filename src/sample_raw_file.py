import pandas as pd
import numpy as np

columns_to_keep = [
                    'POOL_ID', 
                    'LOAN_ID', 
                    'ACT_PERIOD', 
                    'DLQ_STATUS', 
                    'PMT_HISTORY',
                    'ISSUE_SCOREB',
                    'ISSUE_SCOREC',
                    'CURR_SCOREB'
                    ]

tb = pd.read_csv('../data/processed_2019q1_partial.csv', header=0,
                usecols=columns_to_keep)

