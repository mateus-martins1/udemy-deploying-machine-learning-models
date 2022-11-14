# Aula 49
# Transformer's to perform transformations. 
# 1 Capture the difference between the year in which the house was sold and the year in wich the house 
# was built or remodeled
import numpy as np
import pandas as pd

from sklearn.base import BaseEstimator, TransformerMixin
# Base... define the parameters and the Transformer to inherit the fit transform functionality



class TemporalVariableTransformer(BaseEstimator, TransformerMixin):
	# Temporal elapsed time transformer

# variables: the list of variables that we want to calculate
# reference_variable: the variable against which we're going to calculate the difference
    def __init__(self, variables, reference_variable):
        
        if not isinstance(variables, list): # Se n for uma lista da erro
            raise ValueError('variables should be a list')
        
        self.variables = variables
        self.reference_variable = reference_variable

    def fit(self, X, y=None): # É só para ser compatível com SkLearn Pipeline
        # we need this step to fit the sklearn pipeline
        return self

    def transform(self, X): # Permite calcular a diferença

    	# so that we do not over-write the original dataframe
        X = X.copy()
        
        for feature in self.variables:
            X[feature] = X[self.reference_variable] - X[feature]

        return X



# categorical missing value imputer
class Mapper(BaseEstimator, TransformerMixin):

    def __init__(self, variables, mappings): # Variables: which variables need to remapping
                                            # Mappings: wich are the mappings that should be used to replace the variables.

        if not isinstance(variables, list):
            raise ValueError('variables should be a list')

        self.variables = variables
        self.mappings = mappings

    def fit(self, X, y=None):
        # we need the fit statement to accomodate the sklearn pipeline
        return self

    def transform(self, X):
        X = X.copy() # para n reescrever o original
        for feature in self.variables:
            X[feature] = X[feature].map(self.mappings)

        return X