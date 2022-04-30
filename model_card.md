# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details

Xiaonan created the model which is a Gradient Boosting Classifier using the default hyperparameters in scikit-learn.

## Intended Use

Prediction task is to determine whether a person makes over 50K a year.

## Training Data

Data is coming from https://archive.ics.uci.edu/ml/datasets/census+income ; training is done using 80% of this data.

## Evaluation Data

Data is coming from https://archive.ics.uci.edu/ml/datasets/census+income ; evaluation is done using 20% of this data.

## Metrics

The model was evaluated using Accuracy score where he value is around 0.833.

## Ethical Considerations

Variables contain race, gender and country of origin which may lead bias to the model. Further adjustment might be needed.

## Caveats and Recommendations
More variables related to social-economic status might be relevant for such prediction task, e.g. family information.
