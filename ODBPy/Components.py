#!/usr/bin/env python3
import os.path
from collections import namedtuple
from .LineRecordParser import *
from .SurfaceParser import *
from .PolygonParser import *
from .ComponentParser import *
from .Decoder import *
from .Treeifier import *
from .Units import *
import os

Components = namedtuple("Components", ["top", "bot"])

def read_components(directory):
    #Need to support directory layout for ODB++ 8.1: <product_model_name>/steps/<step_name>/layers/<layer_name>/features (orfeatures.Z)
    product_model = (os.listdir(f"{directory}/steps")[-1::][0]) #this should still work with with v7 ODB++
    print(product_model)
    top_path = os.path.join(directory, f"steps/{product_model}/layers/comp_+_top/components2")
    print(top_path)
    top_components = read_linerecords(top_path) if os.path.isfile(top_path) else {}
    bot_path = os.path.join(directory, f"steps/{product_model}/layers/comp_+_bot/component2")
    bot_components = read_linerecords(bot_path) if os.path.isfile(bot_path) else {}
    return Components(parse_components(top_components), parse_components(bot_components))
