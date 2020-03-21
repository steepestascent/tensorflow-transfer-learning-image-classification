set BOTTLENECK_PATH=C:\tmp\bottleneck
set OUTPUT_GRAPH=C:\tmp\output_graph.pb
set OUTPUT_LABELS=C:\tmp\output_labels.txt
set IMAGE_DIR=".\data"
set MODEL_DIR="C:\tmp\model"

python retrain.py^
    --bottleneck_dir=%BOTTLENECK_PATH%^
    --how_many_training_steps=100^
    --output_graph=%OUTPUT_GRAPH%^
    --output_labels=%OUTPUT_LABELS%^
    --image_dir=%IMAGE_DIR%^
    --saved_model_dir=%MODEL_DIR%