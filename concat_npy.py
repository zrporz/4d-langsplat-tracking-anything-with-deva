import numpy as np
import os.path as osp
import os
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--base_dir",type=str)
    args = parser.parse_args()
len_ = len(os.listdir(os.path.join(args.base_dir,"default","origin_mask_default")))
# base_dir = "/n/holylfs05/LABS/pfister_lab/Lab/coxfs01/pfister_lab2/Lab/zhourenping/workspace/Tracking-Anything-with-DEVA/example/output/chickenchicken"
ans = np.load(os.path.join(args.base_dir,"default","origin_mask_default","000001.npy"))
save_dir = os.path.join(args.base_dir,"video_mask_concat")
os.makedirs(save_dir,exist_ok = True)
for i in range(1,len_+1):
    output = np.zeros((4,ans.shape[0],ans.shape[1]))
    output[0] = np.load(osp.join(args.base_dir,"default",'origin_mask_default',f'{i:06}.npy'))
    output[1] = np.load(osp.join(args.base_dir,'small','origin_mask_small',f'{i:06}.npy'))
    output[2] = np.load(osp.join(args.base_dir,'middle','origin_mask_middle',f'{i:06}.npy'))
    output[3] = np.load(osp.join(args.base_dir,'large','origin_mask_large',f'{i:06}.npy'))
    np.save(osp.join(save_dir,f"{i:06}.npy"), output)

print(output.shape)