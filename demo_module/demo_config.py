import numpy as np

dummy_grasp = [
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


'''
    "/home/jisoo/data2/Dexterous_Grasp/mesh/brown_ramen_von/brown_ramen_von_transformed_remesh.obj"
'''
def return_data(guidance, mesh_path, category_id=None, obj_id=None, action_id=None):
    base_dict = {
            "cate_id": "ramen" if category_id is None else category_id,
            "obj_id": "D00001" if obj_id is None else obj_id,
            "action_id": "0001" if action_id is None else action_id,
            "mesh_path": mesh_path,
            "dex_grasp": dummy_grasp,
            "guidance": guidance
        }
    return base_dict


import os, sys
from pathlib import Path

demo_dir = Path(__file__).parent
idgc_model_path = demo_dir/'pretrained_model/idgc/epoch200_minus_loss_-2.6318_latest.pth'
qgc_model_path = demo_dir/'pretrained_model/qgc/epoch100_minus_loss_-4.1409_latest.pth'

project_dir = Path(__file__).parent.parent
idgc_train_cfg_path = project_dir/'config'/'idgc.yaml'
qgc_train_cfg_path = project_dir/'config'/'qgc.yaml'
idgc_demo_cfg_path = project_dir/'config'/'infer_idgc_demo.yaml'
qgc_demo_cfg_path = project_dir/'config'/'infer_qgc_demo.yaml'