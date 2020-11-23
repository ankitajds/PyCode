params =  {"cluster_column" : "cluster","min_k" : 2,"init" : "plus_plus","max_k" : 21, "nfolds" : 15, "max_iterations" : 10000}
_helper.tablename='my new cluster file'
    
from h2o.estimators import H2OKMeansEstimator
from h2o.grid.grid_search import H2OGridSearch
import pandas as pd
import numpy as np
import h2o
import json
import matplotlib.pyplot as plt

def main():
	h2o.init(min_mem_size = "5G", max_mem_size = "200G", enable_assertions=False)

	dataset = _helper.data()
	h_df = h2o.H2OFrame(dataset)
	#print(h_df.columns)
	col_ls = h_df.columns
	# Performing grid search
	kmeans_params1 = {'k': list(np.arange(params["min_k"], params["max_k"]))}
	hkmeans = H2OKMeansEstimator(nfolds=params["nfolds"], max_iterations = params["max_iterations"], init = params["init"])
	grid_kmeans = H2OGridSearch(model=hkmeans, grid_id='grid_kmeans', hyper_params=kmeans_params1)

	# Build and Train the model:
	grid_kmeans.train(x=h_df.columns, training_frame=h_df)
	sorted_grid = grid_kmeans.get_grid(sort_by = 'tot_withinss', decreasing = False)
	best_model = sorted_grid.models[0]
	best_model.download_model(base_path)

	# Add Clusters
	clustered_data = best_model.predict(h_df)
	clust_df = clustered_data.as_data_frame()
	#print(clust_df['predict'])
	dataset[params["cluster_column"]] = clust_df['predict']
	#dataset.to_csv(config["file_path"], index = False)
	h2o.shutdown()
	return _helper.publish(dataset,publish_path)
    
