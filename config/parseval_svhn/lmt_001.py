from config.parseval_svhn.base import *
from src.model.wide_resnet_cb import WideResNet
from src.model.classifier import LMTraining
from src.extension.margin import Margin
from chainer.optimizer import WeightDecay

mode = ['lmt', 'lmt-fc']
predictor = WideResNet(k=4, n_layer=16, drop=.4)
model = LMTraining(predictor, preprocess, c=1e-2)
hook = [WeightDecay(5e-4)]
extension += [(Margin(dataset[1], predictor, preprocess, batchsize), (epoch, 'epoch'))]
