from config.lower_bounds_cifar10.base import *
from src.model.classifier import LMTraining
from chainer.optimizer import WeightDecay

mode = ['default']
model = LMTraining(predictor, preprocess)
hook = [WeightDecay(5e-4)]
