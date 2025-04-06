# Report - Training

After fiddling around with the numbers a bit, these are the results for each model:

## Linear Regression

Couldn't get its mse below 900, infact, it has the worst mse of all models.

Verdict: Do not use.

## Random Forest Regression

Couldn't get its mse below 400.

Verdict: Maybe usable, but there are better models.

## Ada Boost Regression

Couldn't get its mse below 800. Second worst model.

Verdict: Do not use.

## Gradient Boosting Regression

Couldn't get its mse below 500.

Verdict: Do not use.

## Extra Trees Regression

This was the best model (mse around 320, mse deviation below 32), but after the dataset has been extended to 2 weeks, I couldn't get its mse below 350.

Verdict: Usable.

## Bagging Regression

Best model (mse around 330, mse deviation below 32).

Verdict: Use this one.

## Decision Tree Regression

Couldn't get its mse below 400.

Verdict: Maybe usable, but there are better models.

## Extra Tree Regression

Couldn't get its mse below 400.

Verdict: Maybe usable, but there are better models.

## Neural Network

Couldn't get its mse below 400.

Verdict: Maybe usable, but there are better models. I imagine this model will become key when the data is expanded to the entire city.

# Final Verdict

Use either Bagging or Extra Trees regression.