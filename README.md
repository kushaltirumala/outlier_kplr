# outlier_kplr

directory information:
- true_points contains the full dmdt image representations (for all 2500 light curves)
- all files prefixed with "dmdt_" were used to experiment with/create DMDT images
- outlier_verification_pipeline_tsne documents the first umap/tsne results, along with some "outliers" detected
- stabilizing_experiments contains the code for testing hyperparamaters of tsne
- checking_umap_tsne contains code to check (on artificial dataset) the accuracy of tsne/umap
- updates contains code for (most) work done in the recent week (but you will not see dendogram creation there, as I removed it to stop lag)
- stabilization_experiments/ contains graphs for the hyperparameter range testing
- dendogram/ contains dendograms for different embedding sequence experiments (as well as original data)
