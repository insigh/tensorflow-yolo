# add a test for git  22223 
import os.path as osp
import sys

this_dir=osp.dirname(__file__)
sys.path.insert(0, this_dir)


import yolo.dataset
import yolo.net
import yolo.solver
