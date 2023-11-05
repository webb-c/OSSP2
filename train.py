"""How to Learning?

python train.py {args}

examples
- python train.py -m DP -ne 100
- python train.py -m MC -ne 1000
- python train.py -m TD -n 3 -ne 10000 -a 0.01

"""

import numpy as np
import argparse
from method.DP import train_dp
from method.TD import train_td
from method.MC import train_mc


def str2bool(v):
    if isinstance(v, bool):
        return v
    if v.lower() in ('true', 'yes', 't'):
        return True
    elif v.lower() in ('false', 'no', 'f'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')


def parge_opt(known=False):
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--learningMethod", type=str, default="DP", help="rearning method (DP, TD, MC)")
    parser.add_argument("-n", "--nstep", type=int, default=1, help="n-step TD")
    parser.add_argument("-ne", "--episode", type=int, default=1000, help="Number of Episodes")
    # additional args
    parser.add_argument("-s", "--sub", type=str, default="v", help="DP method (p, v)")
    parser.add_argument("-g", "--gamma", type=float, default=1.0, help="gamma")
    parser.add_argument("-a", "--alpha", type=float, default=0.001, help="alpha")
    # data save?
    parser.add_argument("-r","--isRepeat", type=str2bool, default=False, help="do you want't repeat experiment 100 tiems?")
    parser.add_argument("-d", "--isSave", type=str2bool, default=True, help="do you want save a value table?")
    return parser.parse_known_args()[0] if known else parser.parse_args()


def main(opt):
    # validation
    if opt.learningMethod not in ["DP", "TD", "MC"]:
        print("Invalid argument input :", opt.learningMethod)
        return "Training Fail ..."
    # start training
    elif opt.learningMethod == "DP":
        print("Training Start DP with {} episode\n".format(opt.episode))
        train_dp(opt.learningMethod, opt.sub, opt.episode, opt.gamma, opt.isRepeat, opt.isSave)
    elif opt.learningMethod == "MC":
        print("Training Start MC with {} episode\n".format(opt.episode))
        train_mc(opt.learningMethod, opt.episode, opt.gamma, opt.alpha, opt.isRepeat, opt.isSave)
    elif opt.learningMethod == "TD":
        print("Training Start {}-step TD with {} episode\n".format(opt.nstep, opt.episode))
        train_td(opt.learningMethod, opt.nstep, opt.episode, opt.gamma, opt.alpha, opt.isRepeat, opt.isSave)
    return "Training Finish!"


if __name__ == "__main__":
    opt = parge_opt()
    print(main(opt))
