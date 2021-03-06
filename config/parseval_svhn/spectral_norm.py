from config.parseval_svhn.base import *
from src.model.wide_resnet_cb import WideResNet
from src.model.classifier import LMTraining
from src.hook.spectral_norm_regularization import SpectralNormRegularization
from src.extension.margin import Margin

mode = ['default']
predictor = WideResNet(k=4, n_layer=16, drop=.4)
model = LMTraining(predictor, preprocess)
extension += [(Margin(dataset[1], predictor, preprocess, batchsize), (epoch, 'epoch'))]
hook = [SpectralNormRegularization(0.01)]
