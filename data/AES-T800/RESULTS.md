Unless explicitly stated otherwise, all models utilized 32-feature latent space vectors as input, constructed with an autoencoder trained on 20 epochs. 
### Probabilistic Models

| Algorithmn | ROC-AUC  | PR-AUC   | Notes           |
| ---------- | -------- | -------- | --------------- |
| ECOD       | 0.837205 | 0.932958 | scores inverted |
| COPOD      | 0.960804 | 0.982019 | scores inverted |
| ABOD       | 0.999013 | 0.999408 |                 |
| MAD        | 1.000000 | 1.000000 |                 |
| SOS        | 0.530220 | 0.717609 |                 |
| QMCD       | 0.967183 | 0.975335 |                 |
| KDE        | 0.998933 | 0.999347 |                 |
| Sampling   | 0.977878 | 0.983202 |                 |
| GMM        | 0.999701 | 0.999829 | *               |
### Linear Models

| Algorithmn | ROC-AUC  | PR-AUC   | Notes                                                  |
| ---------- | -------- | -------- | ------------------------------------------------------ |
| PCA        | 0.944988 | 0.963730 |                                                        |
| KPCA       | 0.999989 | 0.999995 |                                                        |
| MCD        | 0.660521 | 0.673363 | Fitted on a T4 GPU, is not compatible with cpu devices |
| CD         | 0.824883 | 0.840560 |                                                        |
| OCSVM      | 0.999716 | 0.999821 |                                                        |
| LMDD       | 0.659279 | 0.782633 |                                                        |
### Proximity-Based Models

| Algorithmn | ROC-AUC  | PR-AUC   | Notes           |
| ---------- | -------- | -------- | --------------- |
| LOF        | 0.999999 | 0.999999 |                 |
| COF        | 0.523104 | 0.679135 |                 |
| CBLOF      | 0.992727 | 0.993488 |                 |
| HBOS       | 0.940641 | 0.955360 |                 |
| HDBSCAN    | 0.484096 | 0.634134 |                 |
| KNN        | 0.999979 | 0.999989 |                 |
| SOD        | 0.996474 | 0.998236 | scores inverted |
| ROD        | 0.357677 | 0.602221 |                 |
### Outlier Ensemble Models

| Algorithmn      | ROC-AUC  | PR-AUC   | Notes                                                 |
| --------------- | -------- | -------- | ----------------------------------------------------- |
| iForest         | 0.958247 | 0.971361 |                                                       |
| iNNE            | 0.992674 | 0.995021 |                                                       |
| DIF             | 0.826406 | 0.912020 |                                                       |
| Feature Bagging | 0.999977 | 0.999988 |                                                       |
| LSCP            | 0.999325 | 0.999650 |                                                       |
| XGBOD           | -        | -        | Omitted, not compatible with semi-supervised approach |
| LODA            | 0.874217 | 0.913766 |                                                       |
| SUOD            | 0.999946 | 0.999972 |                                                       |
### Neural Networks

| Algorithmn  | ROC-AUC  | PR-AUC   | Notes                    |
| ----------- | -------- | -------- | ------------------------ |
| AutoEncoder | 0.885323 | 0.892302 | 16,8 hidden layer config |
| VAE         | 0.984707 | 0.989077 | 16,8 hidden layer config |
| DeepSVDD    | 1.000000 | 1.000000 | 100 epochs               |
| SO_GAAL     | 0.501138 | 0.664208 | 60 epochs                |
| MO_GAAL     | 0.446923 | 0.622320 | 60 epochs                |
| AnoGAN      | 0.768856 | 0.845012 |                          |
| ALAD        | 0.408874 | 0.594573 |                          |
| AE1SVM      | 0.867766 | 0.902186 |                          |
| LUNAR       | 1.000000 | 0        |                          |
### Time-Series Outlier Detection

| Algorithmn        | ROC-AUC  | PR-AUC   | Notes |
| ----------------- | -------- | -------- | ----- |
| Time-Series OD    | 0.999990 | 0.999995 |       |
| Spectral Residual | 0.527746 | 0.655265 |       |
| KShape            | 0.381997 | 0.589081 |       |
