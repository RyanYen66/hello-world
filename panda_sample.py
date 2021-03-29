import pandas as pd
scores = pd.Series({'小明':90, '小華':80, '小李':70})
#Series簡單的創建方法，直接給一個dictionary
#新增資料的方法，有點像是陣列
scores['小強'] = 55
print(scores > 60)