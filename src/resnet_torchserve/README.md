# ResNet TorchServe

TorchServeを利用して画像分類APIを作るサンプルです

起動

```bash
./pants package src/resnet_torchserve
docker run --rm -p 8080:8080 -it resnet-torchserve-example 
```

リクエスト

```bash
wget https://github.com/pytorch/serve/blob/master/examples/image_classifier/kitten.jpg
curl http://127.0.0.1:8080/predictions/resnet-18 -T ./examples/image_classifier/kitten.jpg
```
