import pandas as pd

def getxlsxtojson():
    # 读取excel表格
    df = pd.read_excel('01.xlsx', sheet_name='01')
    print(df)
    # 转换成json字符串
    json_data = df.to_json(orient='records',force_ascii=False)
    print(json_data)
    return json_data

def getxlsxtojson2():
    # 读取excel表格
    df = pd.read_excel('2022年园区高企、科小清单.xlsx', sheet_name=[0, 1])
    print(df)
    # 转换成json字符串
    json_data1 = df[0].to_json(orient='records',force_ascii=False)
    print(json_data1)
    json_data2 = df[1].to_json(orient='records', force_ascii=False)
    print(json_data2)
    payload = {'园区有效期内高企清单': json_data1, '2022年科技型中小企业清单': json_data2}
    return payload


if __name__ == '__main__':
    getxlsxtojson()
    getxlsxtojson2()