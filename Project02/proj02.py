import pandas as pd


users = pd.read_table("./Project02/user.txt", sep="|", index_col="user_id")

# 1. 데이터의 개수를 확인하시오
print(len(users), end="\n============================")
"""
943
"""

# 2. 데이터프레임의 앞의 5개와 뒤의 5개의 행을 확인하세요.
print(users.head(5), end="\n\n")
print(users.tail(5), end="\n===========================\n")
"""
         age gender occupation zip_code
user_id
1         24      M     artist    85711
2         53      F     artist    94043
3         23      M   educator    32067
4         24      M     artist    43537
5         33      F     artist    15213

         age gender occupation zip_code
user_id
939       26      F    student    33319
940       32      M   engineer    02215
941       20      M    student    97229
942       48      F   educator    78209
943       22      M    student    77841
"""

# 3. users라는 데이터프레임의 occupation과 age 열만을 포함하는 데이터프레임을 만들고, 이를 users_age에 할당하세요.
users_age = pd.DataFrame(users, columns=["occupation", "age"])
print(users_age, end="\n======================\n")
"""
        occupation  age
user_id
1           artist   24
2           artist   53
3         educator   23
4           artist   24
5           artist   33
...            ...  ...
939        student   26
940       engineer   32
941        student   20
942       educator   48
943        student   22
"""

# 4. users_age의 앞의 5개의 행을 확인하세요.
print(users_age.head(5), end="\n============================\n")
"""
        occupation  age
user_id
1           artist   24
2           artist   53
3         educator   23
4           artist   24
5           artist   33
"""

# 5. 직업(occupation) 별 나이에 대한 사분위수를 이용한 이상치처리를 하세요. 이때, users_age에는 Lower, Upper, Outlier 열이 추가되어야 합니다.
users_age["Lower"] = users_age.groupby("occupation")["age"].transform(
    lambda x: x.quantile(q=0.25) - 1.5 * (x.quantile(q=0.75) - x.quantile(q=0.25)))
users_age["Upper"] = users_age.groupby("occupation")["age"].transform(
    lambda x: x.quantile(q=0.75) + 1.5 * (x.quantile(q=0.75) - x.quantile(q=0.25)))
users_age["Outlier"] = (users_age["age"] > users_age["Upper"]) | (
    users_age["age"] < users_age["Lower"])
print(users_age, end="\n===================\n")
"""
        occupation  age  Lower  Upper  Outlier
user_id
1           artist   24    3.5   63.5    False
2           artist   53    3.5   63.5    False
3         educator   23    4.0   76.0    False
4           artist   24    3.5   63.5    False
5           artist   33    3.5   63.5    False
...            ...  ...    ...    ...      ...
939        student   26    8.5   36.5    False
940       engineer   32    6.5   66.5    False
941        student   20    8.5   36.5    False
942       educator   48    4.0   76.0    False
943        student   22    8.5   36.5    False
"""

# 6. 이상치가 몇 개 있는지 확인하세요.
print(users_age.groupby("Outlier").size(), end="\n=========================\n")
"""
Outlier
False    929
True      14
dtype: int64
"""

# 7. 이상치의 값들을 각 직업별 중앙값(median)으로 변경하세요.
for i in range(len(users_age)):
    if users_age.iloc[i]["Outlier"] == True:
        users_age["age"].iloc[i] = users_age.groupby(
            "occupation")["age"].median().loc[users_age["occupation"].iloc[i]]
print(users_age[users_age["Outlier"] == True], end="\n\n")
print("[참고: 직업별 나이의 중간값]")
print(users_age.groupby("occupation")["age"].median())
"""
        occupation  age  Lower  Upper  Outlier
user_id
30         student   22    8.5   36.5     True
39         student   22    8.5   36.5     True
188        student   22    8.5   36.5     True
211         artist   31    3.5   63.5     True
418        student   22    8.5   36.5     True
423         artist   31    3.5   63.5     True
559       engineer   36    6.5   66.5     True
565        student   22    8.5   36.5     True
767       engineer   36    6.5   66.5     True
803       engineer   36    6.5   66.5     True
839        student   22    8.5   36.5     True
861        student   22    8.5   36.5     True
915        student   22    8.5   36.5     True
926        student   22    8.5   36.5     True

[참고: 직업별 나이의 중간값]
occupation
artist      31
educator    40
engineer    36
retired     63
student     22
Name: age, dtype: int64
"""
