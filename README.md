###### Hawaii_RegimesPredictors

**_Parsing Human and Biophysical Drivers of Coral Reef Regimes_**
---

This repository includes data and analysis scripts to accompany:

Jouffray JB, Wedding L.M., Norstrom A.V., Donovan M.K., Williams G.J., Crowder L.B., Erickson A.L., Friedlander A.M., Graham N.A.J., Gove J.M., Kappel C.V., Kittinger J.N., Lecky J., Oleson K.L.L., Selkoe K.A., White C., Williams I.D., Nystrom M. 2019. Parsing Human and Biophysical Drivers of Coral Reef Regimes. _Proc. R. Soc. B._

**Author:** Jean-Baptiste Jouffray (2019)

**Correspondence:** jean-baptiste.jouffray@su.se

***

### *Description*

The study uses machine learning to model the occurrence of four distinct reef regimes, defined by both fish and benthic communities, using the most spatially extensive predictor dataset available across the Hawaiian Islands. We apply boosted regression trees to quantify the relative influence of each biophysical and anthropogenic predictor, identify relationships between predictors and regimes, and characterize interaction patterns. Disentangling the relative contribution of biophysical and anthropogenic predictors provides a deeper understanding of what underpins coral reef regimes and how a reef's natural setting may either expand or narrow the opportunity space for effective management.

### *Content*

* Script:

**Hawaii_RegimesPredictors.Rmd**: Rmarkdown script of the analyses in the paper and supplementary material.

* Data:

**RegimesPredictors.txt:** main data file containing the regimes and predictors values for 620 sites.

**PredictorsCategories.txt:** categorization of the predictors as either "Anthropogenic" or "Biophysical".

**scale_500.txt; scale_1000.txt; scale_1500.txt; scale_2500.txt; scale_4000.txt:** predictor raster datasets extracted at multiple standardized grain sizes (500m, 1000m, 1500m, 2500m, 4000m) and associated to regimes aggregated following a two-thirds majority within each cell resolution. 

**ModelPerf_Across_Scales.txt:** model performance for each regime at mutliple grain sizes.

**RelInfluence_Across_Scales.txt:** anthropogenic relative influence for each regime at mutliple grain sizes.


