# https://github.com/pytorch/serve/tree/master/examples/image_classifier/resnet_18

wget https://download.pytorch.org/models/resnet18-f37072fd.pth
wget https://raw.githubusercontent.com/pytorch/serve/master/examples/image_classifier/index_to_name.json
wget https://raw.githubusercontent.com/pytorch/serve/master/examples/image_classifier/resnet_18/model.py
torch-model-archiver \
    --model-name resnet-18 \
    --version 1.0 \
    --model-file model.py \
    --serialized-file resnet18-f37072fd.pth \
    --handler image_classifier \
    --extra-files index_to_name.json
mkdir model_store
mv resnet-18.mar model_store/
