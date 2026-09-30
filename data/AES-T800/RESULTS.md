# Quantitative Results
Unless explicitly stated otherwise, all models utilized 32-feature latent space vectors as input, encoded with an autoencoder trained on 20 epochs. Latent space vectors were then scaled to improve feature detection, this has shown to improve select models but most notably those in the neural network class.
### Probabilistic

| Algorithmn | ROC-AUC  | PR-AUC   | Notes                               |
| ---------- | -------- | -------- | ----------------------------------- |
| KDE        | 0.999896 | 0.999943 |                                     |
| GMM        | 0.999701 | 0.999829 |                                     |
| ABOD       | 0.998169 | 0.998736 |                                     |
| Sampling   | 0.990140 | 0.993052 |                                     |
| QMCD       | 0.967183 | 0.975335 |                                     |
| COPOD      | 0.960804 | 0.982019 | scores inverted                     |
| ECOD       | 0.837205 | 0.932958 | scores inverted                     |
| SOS        | 0.529366 | 0.716585 |                                     |

### Probabilistic - Mean Absolute Deviation (MAD)
| Algorithm | ROC-AUC | PR-AUC | Notes                               |
| --------- | ------- | ------ | ----------------------------------- |
| MAD       | 1.00    | 1.00   | used raw (unencoded), scaled data * |
### Linear

| Algorithmn | ROC-AUC  | PR-AUC   | Notes |
| ---------- | -------- | -------- | ----- |
| KPCA       | 0.999238 | 0.999376 |       |
| OCSVM      | 0.946877 | 0.965130 |       |
| PCA        | 0.944988 | 0.963730 |       |
| CD         | 0.871326 | 0.879415 |       |
| MCD        | 0.702989 | 0.697887 |       |
| LMDD       | 0.531450 | 0.747944 |       |
### Proximity-Based

| Algorithmn | ROC-AUC  | PR-AUC   | Notes           |
| ---------- | -------- | -------- | --------------- |
| KNN        | 0.999868 | 0.999928 |                 |
| LOF        | 0.999841 | 0.999907 |                 |
| SOD        | 0.995954 | 0.997972 | scores inverted |
| CBLOF      | 0.975261 | 0.981405 |                 |
| HBOS       | 0.939486 | 0.954940 |                 |
| HDBSCAN    | 0.597633 | 0.707587 |                 |
| COF        | 0.527136 | 0.683053 |                 |
| ROD        | 0.357676 | 0.602221 |                 |
### Outlier Ensembles

| Algorithmn      | ROC-AUC  | PR-AUC   | Notes                                                 |
| --------------- | -------- | -------- | ----------------------------------------------------- |
| Feature Bagging | 0.999665 | 0.999772 |                                                       |
| SUOD            | 0.999439 | 0.999595 |                                                       |
| LSCP            | 0.989450 | 0.994635 |                                                       |
| iNNE            | 0.984715 | 0.989581 |                                                       |
| iForest         | 0.958246 | 0.971360 |                                                       |
| LODA            | 0.874939 | 0.894117 |                                                       |
| DIF             | 0.826402 | 0.912018 |                                                       |
| XGBOD           | -        | -        | Omitted, not compatible with semi-supervised approach |
### Neural Networks

| Algorithmn  | ROC-AUC  | PR-AUC   | Notes                    |
| ----------- | -------- | -------- | ------------------------ |
| DeepSVDD    | 1.000000 | 1.000000 | 100 epochs               |
| VAE         | 0.984656 | 0.989002 | 16,8 hidden layer config |
| SO_GAAL     | 0.928562 | 0.942863 | 60 epochs                |
| AutoEncoder | 0.885322 | 0.892301 | 16,8 hidden layer config |
| MO_GAAL     | 0.879511 | 0.903334 | 60 epochs                |
| AE1SVM      | 0.880220 | 0.912368 |                          |
| AnoGAN      | 0.818057 | 0.882860 |                          |
| ALAD        | 0.486475 | 0.650561 |                          |
### Time-Series Outlier Detection

| Algorithmn        | ROC-AUC  | PR-AUC   | Notes |
| ----------------- | -------- | -------- | ----- |
| Time-Series OD    | 1.000000 | 1.000000 |       |
| LSTMAD            | 0.974082 | 0.979507 |       |
| KShape            | 0.527746 | 0.655265 |       |
| SAND              | 0.483546 | 0.646385 |       |
| Spectral Residual | 0.415979 | 0.612389 |       |

### Graph-Based Embeddings 
| Algorithmn  | ROC-AUC  | PR-AUC   | Notes                                |
| ----------- | -------- | -------- | ------------------------------------ |
| LUNAR       | 1.000000 | 1.000000 |                                      |
| RGraph      | -        | -        | Omitted                              |
| EmbeddingOD | -        | -        | Omitted, not compatible with dataset |
