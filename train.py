"""How to Learning?

python train.py {args}

examples
- python train.py -m DP -ne 100
- python train.py -m MC -ne 1000
- python train.py -m TD -n 3 -ne 1000

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
    parser.add_argument("-ne", "--episode", type=int, default=100, help="Number of Episodes")
    return parser.parse_known_args()[0] if known else parser.parse_args()


def main(opt):
    # validation
    if opt.learningMethod not in ["DP", "TD", "MC"]:
        print("Invalid argument input :", opt.learningMethod)
        return "Training Fail ..."
    elif opt.learningMethod == "DP":
        print("Training Start DP with {} episode".format(opt.episode))
        # train_dp(opt.learningMethod, opt.episode)
    elif opt.learningMethod == "MC":
        print("Training Start MC with {} episode".format(opt.episode))
        # train_mc(opt.learningMethod, opt.episode)
    elif opt.learningMethod == "TD":
        print("Training Start {}-step TD with {} episode".format(opt.nstep, opt.episode))
        # train_td(opt.learningMethod, opt.nstep, opt.episode)
    return "Training Finish!"


if __name__ == "__main__":
    opt = parge_opt()
    print(main(opt))
