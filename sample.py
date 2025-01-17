import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# タイトルの設定
st.title('投資ファンドの計算式')

# 年の選択
year = st.selectbox('表示したい年を選択してください:', [2018, 2019, 2020, 2021])

# データ取得
ticker = 'SPY'
start_date = f'{year}-01-01'
end_date = f'{year}-12-31'

# Yahoo Financeからデータをダウンロード
data = yf.download(ticker, start=start_date, end=end_date)

# データの確認
st.write(data.head())  # データの最初の数行を表示

# ユーザーからの入力を受け取る
window_size = st.number_input('移動平均の期間（日数）を選択してください:', min_value=1, max_value=756, value=30)

# 移動平均線の計算
data['移動平均'] = data['Close'].rolling(window=window_size).mean()

# 結果の表示
col1, col2 = st.columns(2)  # 2つのカラムを作成

with col1:
    st.write("終値")
    st.dataframe(data[['Close']], use_container_width=True)  # 終値を表示

with col2:
    st.write("移動平均")
    st.dataframe(data[['移動平均']], use_container_width=True)  # 移動平均を表示

# グラフの描画
plt.figure(figsize=(14, 7))
plt.plot(data['Close'], label='price moment', color='blue')  # 終値のプロット
plt.plot(data['移動平均'], label='moving average line', color='orange')  # 移動平均線のプロット
plt.title(f'S&P500 closing price and moving average ({year})')  
plt.xlabel('date')  # x軸ラベル
plt.ylabel('price')  # y軸ラベル
plt.legend(title='trend guide')  # 凡例の表示
plt.grid()  # グリッドの表示

# Streamlitでグラフを表示
st.pyplot(plt)  # グラフをStreamlitに表示

# トレンドの把握
st.subheader('トレンドの把握')
st.write('終値は市場の価格変動を示しており、明確なトレンドや急激な変動が見られます。')

# サポートとレジスタンス
st.subheader('サポートとレジスタンス')
st.write('移動平均線は、価格がその線の上にあるときは上昇トレンド、下にあるときは下降トレンドを示すことが多いです。')

# 売買シグナル
st.subheader('売買シグナル')
st.write('移動平均線を超えると、売買シグナルを生成することがあります。例えば、終値が移動平均線を上抜けると買いシグナル、下抜けると売りシグナルとなることがあります。')