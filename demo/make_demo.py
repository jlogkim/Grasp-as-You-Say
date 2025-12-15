import sys, os
import json

import numpy as np 
import math, copy


dummpy_grasp = [
            0.1368691772222519,
            -0.021919019520282745,
            -0.02601059153676033,
            -0.3945882320404053,
            -1.6243696212768555,
            -0.6810823082923889,
            -0.2785188555717468,
            0.2636035978794098,
            0.6286080479621887,
            0.28813788294792175,
            -0.24815425276756287,
            0.618667721748352,
            0.37502115964889526,
            0.4368041753768921,
            -0.16725826263427734,
            0.42284655570983887,
            1.1188902854919434,
            1.002602219581604,
            0.5361297726631165,
            -0.18395759165287018,
            0.9128856658935547,
            0.3561803102493286,
            0.2746677100658417,
            0.33289748430252075,
            0.6225526928901672,
            -0.10777510702610016,
            0.22552181780338287,
            -0.16228024661540985
        ]

base_dict = {
        "cate_id": "ramen",
        "obj_id": "D00001",
        "action_id": "0001",
        "mesh_path": "/home/jisoo/data2/Dexterous_Grasp/mesh/brown_ramen_von/brown_ramen_von_transformed_remesh.obj",
        "dex_grasp": None,
        "guidance": None
    }


demo_data_list = []
for polar in range(0, 180, 30):
    for azimuth in range(0, 360, 40):

        if polar < 30:
            finger = "pinch lightly from above"
        elif polar < 70:
            finger = "wrap the fingers along the surface"
        elif polar < 110:
            finger = "wrap from the side for stability"
        else:
            finger = "scoop upward while curling the fingers"

        guidance = (
            f"To grasp ramen in polar {polar}° and azimuth {azimuth}° position, "
            f"orient the fingers toward azimuth {azimuth}° and {finger}."
        )

        dict_item = copy.deepcopy(base_dict)
        dict_item['dex_grasp'] = dummpy_grasp
        dict_item['guidance'] = guidance
        demo_data_list.append(dict_item)

json.dump(demo_data_list, open('/home/jisoo/data2/Dexterous_Grasp/Grasp-as-You-Say/demo/demo_w_specific_condition.json','w'), indent=4)
