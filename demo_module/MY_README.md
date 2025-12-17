Run the command with below and make json file like ./demo.json 
the "dex_grasp" component is the dummy grasp

Change this two config file using new demo.json path and change the pose_path of qgc following save_path 
idgc_demo_cfg_path = project_dir/'config'/'infer_idgc_demo.yaml'
qgc_demo_cfg_path = project_dir/'config'/'infer_qgc_demo.yaml'


```
python ./demo_module/demo.py --idgc_checkpoint "/home/jisoo/data2/Dexterous_Grasp/Grasp_as_You_Say/Experiments/idgc/resume_from_60/epoch200_minus_loss_-2.6318_.pth" --qgc_checkpoint "/home/jisoo/data2/Dexterous_Grasp/Grasp_as_You_Say/Experiments/qgc/epoch100_minus_loss_-4.1409_latest.pth"
```
```

```
python ./demo/demo.py --qgc_checkpoint "/home/jisoo/data2/Dexterous_Grasp/Grasp_as_You_Say/Experiments/qgc/epoch100_minus_loss_-4.1409_latest.pth"
```
