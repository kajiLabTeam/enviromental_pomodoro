import requests

def environmental_sensor_data():
    url = 'https://sensor-api.sysken.net/get/sensor'

    try:
        response = requests.get(url)
        response.raise_for_status()  # エラーがあれば例外を発生させる
        sensor_data = response.json()  # JSONレスポンスをPythonのリストに変換
        return sensor_data[:17]  # データを返す
    except requests.exceptions.RequestException as e:
        print("センサーデータを取得できませんでした:", e)
        return None

# センサーデータを取得する
data = environmental_sensor_data()
if data:
    print("取得したデータ:", data)
else:
    print("データを取得できませんでした")