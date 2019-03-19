import GPy
# you would need to install this e.g. pip install GPy

def TrainModel(X_train,y_train):
    """ use this to train the model.
    inputs:
       X_train is the X training data
    of size (N,p) where N is number of datapoints and p is the number of variables
    (e.g. N= 500 training datapoints, p =10 variables to describe trajectory
       y_train is the output data you want to predict, where this is size N,k where 
    N is number of datapoints (eg.500) and k is the number of variables to predict 
    (we have k=2, one of mean longitude, one is mean latitude)
    outputs:
       returns model, and kernel. you wont need the kernel so just look at the model. this is
    a GPy object, find info about it with print(m) """
    print("Training Model...")
    # GP Model
    (N,p) = X_train.shape
    kern = GPy.kern.RBF(p,ARD=True)

    print("kernel used: {}".format(kern))

    m = GPy.models.GPRegression(X_train,y_train,kern)
    m.optimize()

    print("Model optimized: {}".format(m))
    return(m,kern)

def TestModel(m,X_test):
    """this makes the prediction and gives back the predction and error
    inputs:
       m = model which is returned from TrainModel
       X_test = the X points you want to test the model at, size N,p 
     where N is the number of test points, e.g. 100, and p is the number of variables, 
     e.g. 10 trajectory signature variables
    outputs:
       y_pred, the prediction of size N,k, where N is the number of test points you have 
     for X_test and  where k=2 for mean lon, mean lat
       gp_err, the error for 1 std deviation i.e the variance for each point predicted 
     same size as y_pred
    """
    # Validation
    print("Validation Stage: Predicting and plotting... ")
    y_pred,cov = m.predict(X_test,full_cov=True)
    print(X_test.shape)
    err = m.predict_quantiles(X_test)
    print(err)
    gp_err = y_pred- (err[0])
    print(gp_err.shape)
    return(y_pred,gp_err)
