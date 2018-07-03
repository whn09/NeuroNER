#mkdir -p ../data/funny/deploy
#cp ../../../../dataset/tag/tags_content.raw.20180703 .
#cd ../data/funny/deploy
#split -l 1 -d --suffix-length=6 --additional-suffix=.txt tags_content.raw.20180703
#cd ../../../src/

python3 main.py --train_model=False --use_pretrained_model=True --dataset_text_folder=../data/funny_all --pretrained_model_folder=../trained_models/conll_2003_en

