for level in 'default' 'small' 'middle' 'large' 
do
export LEVEL=$level
echo $LEVEL
cam_num=${cam_num}
echo $cam_num
python demo/demo_automatic.py --chunk_size 4 \
--img_path <PATH TO YOUR IMAGE>/ims/cam${cam_num} \
--amp --temporal_setting semionline \
--size 480 \
--output ./output/${level}
done
