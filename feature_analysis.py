#!/usr/bin/env python
# coding: utf-8

# In[274]:


import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.feature_selection import SelectFromModel
import numpy as np
import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from xgboost import XGBRegressor
from sklearn.cluster import KMeans
pd.set_option("display.max_columns", None)
plt.style.use('dark_background')
plt.rcParams["figure.figsize"] = (8,6)
from functions import *



def Featue_Analysis(filename):
	data = create_data('train.pkl')


	data.describe()

	corr_matrix(data, ['Low Emergence_mean', 'New yield risk_mean', 'Nutrient Deficiency_mean',
	'Replant Risk_mean', 'harvest_mean'])


	hist_feature(data, 'harvest_mean')


	plot_feature_scatter(data, 'Low Emergence_mean', 'harvest_mean')

	plot_features_dist(data, 'Low Emergence_mean', 'harvest_mean')

	plot_distribution(data, 'Low Emergence_mean', 'harvest_mean')

	plot_distribution_for_groups(data, 'Low Emergence_mean', 'harvest_mean')
	
	
	plot_feature_scatter(data, 'New yield risk_mean', 'harvest_mean')

	plot_features_dist(data, 'New yield risk_mean', 'harvest_mean')

	plot_distribution(data, 'New yield risk_mean', 'harvest_mean')

	plot_distribution_for_groups(data, 'New yield risk_mean', 'harvest_mean')



	plot_feature_scatter(data, 'Nutrient Deficiency_mean', 'harvest_mean')

	plot_features_dist(data, 'Nutrient Deficiency_mean', 'harvest_mean')

	plot_distribution(data, 'Nutrient Deficiency_mean', 'harvest_mean')

	plot_distribution_for_groups(data, 'Nutrient Deficiency_mean', 'harvest_mean')


	plot_feature_scatter(data, 'Replant Risk_mean', 'harvest_mean')

	plot_features_dist(data, 'Replant Risk_mean', 'harvest_mean')

	plot_distribution(data, 'Replant Risk_mean', 'harvest_mean')

	plot_distribution_for_groups(data, 'Replant Risk_mean', 'harvest_mean')


	plot_clusters(data, ['Low Emergence_mean', 'New yield risk_mean', 'Nutrient Deficiency_mean',
	'Replant Risk_mean', 'harvest_mean'])

	#new features
	data['Nutrient > 0.4 and Emergence > 0.1'] = np.where((data['Nutrient Deficiency_mean'] > 0.4)
		              & (data['Low Emergence_mean'] > 0.1), 1, 0)
	data['Nutrient risk more than 0.8'] = np.where((data['Nutrient Deficiency_mean']  > 0.8), 1, 0)
	data['all alerts less than 0.1'] = np.where((data.iloc[:,:4].sum(axis = 1) < 0.1), 1, 0)
	data['Replant and yield risk more than 0.1'] = np.where((data['Replant Risk_mean'] > 0.1) 
		             & (data['New yield risk_mean'] > 0.1), 1, 0)
	data['all alerts more than 0.4'] = np.where((data.iloc[:,:4].sum(axis = 1) > 0.4), 1, 0)




	new_feature_list = ['Nutrient > 0.4 and Emergence > 0.1', 'Nutrient risk more than 0.8',
	'all alerts less than 0.1', 'Replant and yield risk more than 0.1',
	'all alerts more than 0.4']


	corr_matrix(data, new_feature_list)

	plot_sepeartaed_groups(data, new_feature_list)



	tabel_between_features(data, 'Low Emergence_mean', 'Nutrient Deficiency_mean')

	tabel_between_features(data, 'New yield risk_mean', 'Nutrient Deficiency_mean')

	tabel_between_features(data, 'Replant Risk_mean', 'Nutrient Deficiency_mean')

	tabel_between_features(data, 'New yield risk_mean', 'Low Emergence_mean')

	tabel_between_features(data, 'Replant Risk_mean', 'Low Emergence_mean')

	tabel_between_features(data, 'Replant Risk_mean', 'New yield risk_mean')


	# ### features importance: information gain based on entropy

	feature_imp(data[['Low Emergence_mean', 'New yield risk_mean', 'Nutrient Deficiency_mean',
	'Replant Risk_mean']], data['harvest_mean'])


	# ## outlier detection


	feauture_list = ['Low Emergence_mean', 'New yield risk_mean', 'Nutrient Deficiency_mean',
	'Replant Risk_mean']



	feature_outlier(data, feauture_list)

	df = data.reset_index()
	df_nooutlier =  iqr(df, feauture_list)
	df_outlier = df[~df.index.isin(df_nooutlier.index)]


	hist_feature(df_nooutlier, 'harvest_mean', title = 'without outlier')

	print(f'outlier count: {df_outlier.shape[0]}')
	hist_feature(df_outlier, 'harvest_mean', title = 'outlier')


	# ## Other features

	corr_matrix(data, ['ndvi_mean', 'ndvi_std', 'harvest_mean'])
	

	plot_feature_scatter(data, 'ndvi_std', 'harvest_mean')

	plot_feature_scatter(data, 'ndvi_mean', 'harvest_mean')

	plot_features_dist(data, 'ndvi_mean', 'harvest_mean')

	plot_features_dist(data, 'ndvi_std', 'harvest_mean')



	ndvi_feature_list = ['ndvi_hist_1','ndvi_hist_2', 'ndvi_hist_3', 'ndvi_hist_4','ndvi_hist_5', 'ndvi_hist_6', 'ndvi_hist_7', 
		      'ndvi_hist_8', 'ndvi_hist_10', 'ndvi_hist_11', 'ndvi_hist_12', 'ndvi_hist_13', 'ndvi_hist_14', 
	       'ndvi_hist_15', 'ndvi_hist_16', 'ndvi_hist_17','ndvi_hist_18', 'ndvi_hist_9', 'ndvi_mean', 'ndvi_std']



	scale_norm_ndvi = scaling(data[ndvi_feature_list])
	X_ndvi = scale_norm_ndvi.transform(data[ndvi_feature_list])
	pca_ndvi, principalDf_ndvi = pca_method(X_ndvi, data[ndvi_feature_list].index, 5)
	# plot_pca(pca_ndvi)



	planter_feature_list = ['planter_hist_2', 'planter_hist_3', 'planter_hist_4', 'planter_hist_5',  'planter_mean', 'planter_std']
	corr_matrix(data, ['planter_hist_2', 'planter_hist_3', 'planter_hist_4', 'planter_hist_5',  'planter_mean', 'planter_std', 'harvest_mean'])

	plot_feature_scatter(data, 'planter_mean', 'harvest_mean')

	plot_features_dist(data, 'planter_mean', 'harvest_mean')


	scale_norm_plant = scaling(data[planter_feature_list])
	X_plant = scale_norm_plant.transform(data[planter_feature_list])
	pca_plant, principalDf_plant = pca_method(X_plant, data[planter_feature_list].index, 3)
	# plot_pca(pca_plant)


	data_other = pd.concat([principalDf_ndvi, principalDf_plant, data['harvest_mean']], axis=1)
	data_other.columns = ['PC_ndvi1','PC_ndvi2','PC_ndvi3','PC_ndvi4','PC_ndvi5', 
		      'PC_plant1', 'PC_plant2', 'PC_plant3', 'harvest_mean']

	corr_matrix(data_other, data_other.columns)

	feature_imp(data_other[['PC_ndvi1','PC_ndvi2','PC_ndvi3','PC_ndvi4','PC_ndvi5', 
		      'PC_plant1', 'PC_plant2', 'PC_plant3']], data_other['harvest_mean'])



	plot_features_dist(data_other, 'PC_plant1', 'harvest_mean')

	plot_features_dist(data_other, 'PC_ndvi3', 'harvest_mean')


Featue_Analysis('train.pkl')
