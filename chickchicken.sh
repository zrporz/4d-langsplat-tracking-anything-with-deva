hypernerf_path=../../data/hypernerf
output_path=./output
for level in 'default' 'small' 'middle' 'large' 
do
export LEVEL=$level
echo $LEVEL
python demo/demo_automatic.py --chunk_size 4 \
--img_path ${hypernerf_path}/chickchicken/rgb/2x \
--amp --temporal_setting semionline \
--size 480 \
--output ${output_path}/${level}
done

python concat_npy.py --base_dir ${output_path}