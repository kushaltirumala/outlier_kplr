# outlier_kplr

Novel unsupervised methods for time series anomaly detection, tested on Kepler light-curve dataset. See paper at `https://arxiv.org/pdf/2009.06760.pdf`.

### Directory information:

v1/exploration: directory information:
- true_points contains the full dmdt image representations (for all 2500 light curves)
- all files prefixed with "dmdt_" were used to experiment with/create DMDT images
- outlier_verification_pipeline_tsne documents the first umap/tsne results, along with some "outliers" detected
- stabilizing_experiments contains the code for testing hyperparamaters of tsne
- checking_umap_tsne contains code to check (on artificial dataset) the accuracy of tsne/umap
- stabilization_experiments/ contains graphs for the hyperparameter range testing
- dendogram/ contains dendograms for different embedding sequence experiments (as well as original data)

main directory:
- recreating_dense_light_curve_results.ipynb contains full pipeline to generate dense light curve analysis + results for paper (dense curves)
- recreating_sparse_light_curve_results.ipynb contains full pipeline to generate spsrse light curve analysis + results for paper (sparse curves)
