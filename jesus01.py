import pandas as pd
import csv

#################################
## 함수 정의
#################################


def get_stock():
    df = pd.DataFrame()
    for page in range(0,1000,25):
        # 일별 시세 url

        url = 'https://www.uniprot.org/uniprot/?query=*&columns=id%2centry+name%2creviewed%2cprotein+names%2cgenes%2corganism%2clength&offset={page}'.format(page=page)
        print(url)
        current_df = pd.read_html(url, header=0)[0]
        df = df.append(current_df, ignore_index=True)

    return df

df = get_stock()
print(df)
df.to_csv('test_1000.csv')

#################################
## 함수 호출
#################################
# 종목 코드 가져오기


# 일별 시세 가져오기



# 일별 시세 클린징
