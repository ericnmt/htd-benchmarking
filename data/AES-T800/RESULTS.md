# Quantitative Results AES-T800 Variant
Unless explicitly stated otherwise, all models utilized 32-feature latent space vectors as input, encoded with an autoencoder trained on 20 epochs. Latent space vectors were then scaled to improve feature detection, this has shown to improve select models but most notably those in the neural network class.
### Probabilistic

| Algorithmn | ROC-AUC  | PR-AUC   | Notes           |
| ---------- | -------- | -------- | --------------- |
| KDE        | 0.999896 | 0.999943 |                 |
| GMM        | 0.999701 | 0.999829 |                 |
| ABOD       | 0.998169 | 0.998736 |                 |
| Sampling   | 0.990140 | 0.993052 |                 |
| QMCD       | 0.967183 | 0.975335 |                 |
| COPOD      | 0.960804 | 0.982019 | scores inverted |
| ECOD       | 0.837205 | 0.932958 | scores inverted |
| SOS        | 0.529366 | 0.716585 |                 |

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
## Non-Encoded Results
The following results are not fed through the encoding process, and are testing with raw data only.
### Probabilistic Models
| Algorithmn | ROC-AUC  | PR-AUC   | Notes                                                                               |
| ---------- | -------- | -------- | ----------------------------------------------------------------------------------- |
| ABOD       | 1.000000 | 1.000000 |                                                                                     |
| KDE        | 1.000000 | 1.000000 |                                                                                     |
| Sampling   | 1.000000 | 1.000000 |                                                                                     |
| GMM        | 1.000000 | 1.000000 |                                                                                     |
| QMCD       | -        | -        | Omitted,                                                                            |
| COPOD      | 0.999687 | 0.999876 | scores inverted                                                                     |
| ECOD       | 0.999418 | 0.999783 | scores inverted                                                                     |
| SOS        | -        | -        | Omitted,                                                                            |
| MAD        | 1.000000 | 1.000000 | Result is consistent with encoded trial since raw data was used for train and test. |
### Linear Models
| Algorithmn | ROC-AUC  | PR-AUC   | Notes            |
| ---------- | -------- | -------- | ---------------- |
| PCA        | 1.000000 | 1.000000 |                  |
| KPCA       | 1.000000 | 1.000000 |                  |
| OCSVM      | 1.000000 | 1.000000 |                  |
| CD         | -        | -        | Omitted, timeout |
| MCD        | -        | -        | Omitted, timeout |
| LMDD       | -        | -        | Omitted, timeout |
### Proximity-Based Models
| Algorithmn | ROC-AUC  | PR-AUC   | Notes                    |
| ---------- | -------- | -------- | ------------------------ |
| LOF        | 1.000000 | 1.000000 |                          |
| CBLOF      | 1.000000 | 1.000000 |                          |
| HBOS       | 1.000000 | 1.000000 |                          |
| KNN        | 1.000000 | 1.000000 |                          |
| HDBSCAN    | 0.971803 | 0.978466 |                          |
| SOD        | 0.940608 | 0.926032 | scores inverted          |
| COF        | 0.503248 | 0.693217 |                          |
| ROD        | -        | -        | Omitted, memory overflow |
### Outlier Ensembles

| Algorithmn      | ROC-AUC  | PR-AUC   | Notes                                                    |
| --------------- | -------- | -------- | -------------------------------------------------------- |
| SUOD            | 1.000000 | 1.000000 |                                                          |
| iNNE            | 1.000000 | 1.000000 |                                                          |
| Feature Bagging | 1.000000 | 1.000000 |                                                          |
| LODA            | 1.000000 | 1.000000 |                                                          |
| iForest         | 0.999773 | 0.999857 |                                                          |
| DIF             | 0.699637 | 0.806146 |                                                          |
| LSCP            | -        | -        | Omitted, timeout                                         |
| XGBOD           | -        | -        | Omitted, not compatible with semi-supervised application |
### Neural Networks

| Algorithmn  | ROC-AUC  | PR-AUC   | Notes                    |
| ----------- | -------- | -------- | ------------------------ |
| DeepSVDD    | 1.000000 | 1.000000 | 100 epochs               |
| VAE         | 1.000000 | 1.000000 | 16,8 hidden layer config |
| SO_GAAL     | 0.491656 | 0.662963 | 60 epochs                |
| AutoEncoder | 1.000000 | 1.000000 | 16,8 hidden layer config |
| MO_GAAL     | 0.047836 | 0.460333 | 60 epochs                |
| AE1SVM      | 1.000000 | 1.000000 |                          |
| AnoGAN      | 1.000000 | 1.000000 |                          |
| ALAD        | 0.036743 | 0.456214 |                          |
### Time-Series Outlier Detection

| Algorithmn        | ROC-AUC  | PR-AUC   | Notes            |
| ----------------- | -------- | -------- | ---------------- |
| Time-Series OD    | 1.000000 | 1.000000 |                  |
| LSTMAD            | 0.995025 | 0.998333 |                  |
| KShape            | -        | -        | Omitted, timeout |
| SAND              |          |          |                  |
| Spectral Residual | 0.518977 | 0.676493 | Omitted, timeout |

### Graph-Based Embeddings 
| Algorithmn  | ROC-AUC  | PR-AUC   | Notes                                |
| ----------- | -------- | -------- | ------------------------------------ |
| LUNAR       | 1.000000 | 1.000000 |                                      |
| RGraph      | -        | -        | Omitted                              |
| EmbeddingOD | -        | -        | Omitted, not compatible with dataset |
