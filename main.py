import streamlit as st
import time

st.title('Streamlit_TEST')

st.write('プログレスバーの表示')
'Start!!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration{i+1}')
    bar.progress(i+1)
    time.sleep(0.1)

'Done!!!' 

left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

expander1 = st.expander('カタリスト1')
expander1.write('カタリスト1の回答')
expander2 = st.expander('カタリスト2')
expander2.write('カタリスト2の回答')
expander3 = st.expander('カタリスト3')
expander3.write('カタリスト3の回答')

text = st.text_input('あなたの銘柄を教えてください。')
condition = st.slider('あなたのモメンタムは？', 0,100,50)

'あなたの銘柄：',text
'モメンタム:',condition



