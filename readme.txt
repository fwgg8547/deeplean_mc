### voc2012.py

class file : in : ./data/voc2012.name
クラス定義

tfrecord : out : ./data/voc2012_train.tfrecord
outputファイル

image list : in :
学習ファイルリスト
   ./data/voc2012_raw/VOCdevkit/VOC2012/ImageSets/Main/train.txt (training)
   ./data/voc2012_raw/VOCdevkit/VOC2012/ImageSets/Main/val.txt (validation)
annotationファイル
   ./data/voc2012_raw/VOCdevkit/VOC2012/Annotations/"image_filename".xml
教師イメージ
   ./data/voc2012_raw/VOCdevkit/VOC2012/JPEGImages/"image_filename"


Annotations
<filename>
<size><width>
<size><height>
<object><difficult>
<object><bndbox><xmin>
<object><bndbox><ymin>
<object><bndbox><xmax>
<object><bndbox><ymax>
<object><name>
<object><truncated>
<object><pose>


### convert.py
weights を tf 用に変更

./data/yolov3.weights
output: ./checkpoints/yolov3.tf


### train.py
dataset :in: => tfrecord file
val_dataset :in: => 


tf用 weight: out : ./checkpoints/yolov3.tf



clip image
add annotation
make train.txt, val.txt by make_list.py

make tfrecord file
py .\tools\voc_mine.py --split train
py .\tools\voc_mine.py --split val

make training
py .\trainmine.py --batch_size 8 --mode eager_tf --dataset ./data/vocmine_train.tfrecord --val_dataset ./data/vocmine_val.tfrecord --num_classes 1

py .\detectmine.py --image .\data\mindata\test\test1.jpg --output ./out1.jpg --num_classes 1
