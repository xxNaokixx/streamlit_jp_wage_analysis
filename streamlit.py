import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import pydeck as pdk
from PIL import Image
import time

st.title("タイトル表示")
st.header("ヘッダーの表示")
st.subheader("サブヘッダーの表示")
st.text("テキストの表示")

df = pd.DataFrame({
    "first column":[1,2,3,4],
    "second column": [40,30,20,10]
})

st.write(df)
st.dataframe(df)
st.dataframe(df, width = 200, height = 200)
st.dataframe(df.style.highlight_max(axis=1) )
st.table(df)

df

x = 100
x

"""
# マジックコマンドを使う

```
import pandas as pd
```

"""

df1 = pd.DataFrame(np.random.randn(20,3), columns = ["a", "b", "c"])


df1

st.line_chart(df1)
st.area_chart(df1)
st.bar_chart(df1)

fig = plt.figure(figsize = (10,5))
ax = plt.axes()
x = [105, 210, 301,440, 500]
y = [10,20,30,50,60]
ax.plot(x,y)

st.pyplot(fig)

tokyo_lat = 35.69
tokyo_lon = 139.69

df_tokyo = pd.DataFrame(
    np.random.randn(1000,2)/[50,50]+[tokyo_lat, tokyo_lon],
    columns = ["lat", "lon"]
)
df_tokyo

st.map(df_tokyo)


view = pdk.ViewState(latitude = tokyo_lat, longitude = tokyo_lon, pitch = 50, zoom = 11)
hexagon_layer = pdk.Layer("hexagonLayor",data = df_tokyo, get_position = ["lon", "lat"], elevation_scale = 6, radius = 200, extruded = True)
layer_map = pdk.Deck(layers = hexagon_layer, initial_view_state = view)

st.pydeck_chart(layer_map)

image = Image.open("test.png")
st.image(image, caption = "サンプル1", use_column_width = True)

option_button = st.button("ボタン")

if option_button == True:
    st.write("ボタンが押されました")
else:
    st.write("ボタンを押してください")

option_radio = st.radio(
    "好きな果物を選んでください",
    ("バナナ", "林檎", "オレンジ", "その他")
)

st.write("あなたが選んだ果物は", option_radio)

option_check = st.checkbox("DataFrameの表示")

if option_check == True:
    st.write(df)

option_select = st.selectbox(
    "どれか一つを選んでください",
    ("A", "B", "C")
)

st.write("あなたが選んだのは：", option_select)

option_multi = st.multiselect(
    "どれか2つを選んでください",
    ["A", "B", "C", "D"],
    ["A","B"]
)

age = st.slider("あなたの年齢を教えてください", min_value=0, max_value = 130, step=1, value=20)
st.write("私の年齢は", age, "です")

values = st.slider(
    "数値の範囲を入力してください",
    0.0, 100.0, (25.0, 75.0)
)
st.write("Values", values)

height = st.sidebar.slider("あなたの身長を教えてください", min_value=0, max_value = 200, step=1, value=170)
st.write("私の身長は", height, "です")

progress_button = st.button("プログレスボタン")
if progress_button == True:
    st.write("処理を開始します")
    my_bar = st.progress(0)
    for percent_complete in range(100):
        time.sleep(0.01)
        my_bar.progress(percent_complete+1)
    st.text('処理が終了しました')
else:
    st.write("プログレスボタンを押してください")







