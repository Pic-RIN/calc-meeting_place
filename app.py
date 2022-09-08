# -*- coding: utf-8 -*-
import geocoder as geocoder
import streamlit as st
import pandas as pd
import numpy as np
import geocoder
from statistics import mean


def main():
	data = []
	data_mean = []
	text = st.text_input(label='最寄り駅を入力', value='')

	if 'text_list' not in st.session_state:
		st.session_state["text_list"] = []

	col1, col2 = st.columns(2)

	with col1:
		if st.button("追加", key=2):
			st.session_state["text_list"].append(text)

	with col2:
		if st.button("削除", key=3):
			st.session_state["text_list"].remove(text)

	for output_text in st.session_state["text_list"]:
		st.write("", output_text)
		location = output_text
		ret = geocoder.osm(location, timeout=5.0)
		data.append(ret.latlng)
	if data:
		data_mean.append(np.mean(data, axis=0))
		map_data = pd.DataFrame(data, columns=['lat', 'lon'])
		map_data_mean = pd.DataFrame(data_mean, columns=['lat', 'lon'])
		# 地図に散布図を描く
		st.title("入力地点")
		st.map(map_data)
		st.title("平均座標地点")
		st.map(map_data_mean)


if __name__ == '__main__':
	main()
