# Quantitative Results AES-T1600 Variant
Unless explicitly stated otherwise, all models utilized 32-feature latent space vectors as input, encoded with an autoencoder trained on 20 epochs. Latent space vectors were then scaled to improve feature detection, this has shown to improve select models but most notably those in the neural network class.
### Probabilistic

| Algorithmn | ROC-AUC  | PR-AUC   | Notes           |
| ---------- | -------- | -------- | --------------- |
| Sampling   | 0.528396 | 0.687833 |                 |
| KDE        | 0.513442 | 0.670577 |                 |
| ABOD       | 0.512661 | 0.670774 |                 |
| GMM        | 0.510805 | 0.668868 |                 |
| QMCD       | 0.510220 | 0.670142 |                 |
| SOS        | 0.503450 | 0.671669 |                 |
| COPOD      | 0.488217 | 0.651671 | scores inverted |
| ECOD       | 0.465481 | 0.637811 | scores inverted |

### Probabilistic - Mean Absolute Deviation (MAD)
| Algorithm | ROC-AUC  | PR-AUC   | Notes                               |
| --------- | -------- | -------- | ----------------------------------- |
| MAD       | 0.530685 | 0.683308 | used raw (unencoded), scaled data * |
### Linear

| Algorithmn | ROC-AUC  | PR-AUC   | Notes |
| ---------- | -------- | -------- | ----- |
| LMDD       | 0.598778 | 0.762990 |       |
| KPCA       | 0.518348 | 0.674000 |       |
| OCSVM      | 0.514283 | 0.671304 |       |
| PCA        | 0.511762 | 0.669698 |       |
| MCD        | 0.507626 | 0.665683 |       |
| CD         | 0.282208 | 0.534942 |       |
### Proximity-Based

| Algorithmn | ROC-AUC  | PR-AUC   | Notes             |
| ---------- | -------- | -------- | ----------------- |
| SOD        | 0.590644 | 0.726697 | scores inverted   |
| KNN        | 0.513472 | 0.668163 |                   |
| HBOS       | 0.508644 | 0.669633 |                   |
| LOF        | 0.503733 | 0.664592 |                   |
| CBLOF      | 0.501529 | 0.661961 | `n_clusters = 20` |
| ROD        | 0.498377 | 0.662425 |                   |
| HDBSCAN    | 0.495813 | 0.659118 |                   |
| COF        | 0.493957 | 0.662160 |                   |
|            |          |          |                   |
### Outlier Ensembles

| Algorithmn      | ROC-AUC  | PR-AUC   | Notes                                                 |
| --------------- | -------- | -------- | ----------------------------------------------------- |
| iForest         | 0.519201 | 0.679086 |                                                       |
| SUOD            | 0.515638 | 0.671158 |                                                       |
| LSCP            | 0.513101 | 0.670403 |                                                       |
| iNNE            | 0.508882 | 0.667516 |                                                       |
| Feature Bagging | 0.507984 | 0.666311 |                                                       |
| DIF             | 0.504638 | 0.666847 |                                                       |
| LODA            | 0.482418 | 0.653563 |                                                       |
| XGBOD           | -        | -        | Omitted, not compatible with semi-supervised approach |
### Neural Networks

| Algorithmn  | ROC-AUC  | PR-AUC   | Notes                    |
| ----------- | -------- | -------- | ------------------------ |
| MO_GAAL     | 0.574926 | 0.719048 | 60 epochs                |
| SO_GAAL     | 0.557985 | 0.705870 | 60 epochs                |
| AE1SVM      | 0.539541 | 0.694075 |                          |
| VAE         | 0.513219 | 0.671680 | 16,8 hidden layer config |
| AutoEncoder | 0.512151 | 0.669853 | 16,8 hidden layer config |
| ALAD        | 0.497431 | 0.668295 |                          |
| AnoGAN      | 0.492108 | 0.659049 |                          |
| DeepSVDD    | 0.475601 | 0.649006 | 100 epochs               |
### Time-Series Outlier Detection

| Algorithmn        | ROC-AUC  | PR-AUC   | Notes |
| ----------------- | -------- | -------- | ----- |
| Time-Series OD    | 0.537066 | 0.677935 |       |
| KShape            | 0.522110 | 0.690103 |       |
| LSTMAD            | 0.514667 | 0.673342 |       |
| SAND              | 0.510888 | 0.679749 |       |
| Spectral Residual | 0.494996 | 0.659365 |       |

### Graph-Based Embeddings 
| Algorithmn  | ROC-AUC | PR-AUC | Notes                                |
| ----------- | ------- | ------ | ------------------------------------ |
| LUNAR       | 0.5     | 0.5    |                                      |
| RGraph      | -       | -      | Omitted                              |
| EmbeddingOD | -       | -      | Omitted, not compatible with dataset |