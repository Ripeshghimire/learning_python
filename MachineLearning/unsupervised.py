# # Unsupervised learning Iris Dimentionality
#
# # we first reduce the dimensionality of the Iris data to visualize there are 4 features
# # The work of dimension redcution is to find suitable lower dimension that retains essential feature of data
# # this helps in visualization of data
#
# import seaborn
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns
#
# sns.set()
# # getting the data set form the seaborn
# iris_data = seaborn.load_dataset('iris')
# # extraction of only the feature set
# X_iris = iris_data.drop('species', axis=1)
# # extraction of target set
# y_iris = iris_data['species']
#
# # Using PCA ( Principal Component Analysis )
# # 1 Choose the model
# from sklearn.decomposition import PCA
#
# # 2 Instantiate with hyper parameter
# # ncomponents states how many dimension to change
# model = PCA(n_components=2)
# # 3 Fit the data
# model.fit(X_iris)
# # 4 Predict the data
# X_2D = model.transform(X_iris)
#
# # Visualizing the data
# iris_data['PCA1'] = X_2D[:, 0]
# iris_data['PCA2'] = X_2D[:, 1]
# sns.lmplot(x="PCA1",y= "PCA2", hue='species', data=iris_data, fit_reg=False)
# plt.show()
#
# # We see that in the two-dimensional representation, the species are fairly well separa‐
# # ted, even though the PCA algorithm had no knowledge of the species labels! This
# # indicates to us that a relatively straightforward classification will probably be effective
# # on the dataset, as we saw before.
#
#
# # Using Gaussian Mixture Model
# from sklearn.mixture import GaussianMixture
#
# model = GaussianMixture(n_components=2, covariance_type='full')
# model.fit(X_iris)
# y_gmm = model.predict(X_iris)
#
# # adding the cluster into original data and plotting with seaborn
# iris_data['cluster'] = y_gmm
# sns.lmplot(x="PCA1", data=iris_data, hue='species',
#            col='cluster', fit_reg=False)
# plt.show()
#
# # By splitting the data by cluster number, we see exactly how well the GMM algorithm
# # has recovered the underlying label: the setosa species is separated perfectly within
# # cluster 0, while there remains a small amount of mixing between versicolor and vir‐
# # ginica. This means that even without an expert to tell us the species labels of the indi‐
# # vidual flowers, the measurements of these flowers are distinct enough that we could
# # automatically identify the presence of these different groups of species with a simple
# # e different groups of species with a simple