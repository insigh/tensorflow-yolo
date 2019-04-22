import os.path as osp
import sys

this_dir=osp.dirname(__file__)
sys.path.insert(0, this_dir)

import net
import yolo_net
import yolo_tiny_net
