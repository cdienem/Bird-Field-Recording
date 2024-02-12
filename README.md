# Bird-Field-Recording
Collection of instructions and tools to handle and analyze bird field recordings using a simple pipeline:

.wav files → (predict) BirdNet → (review/correct) AviaNZ → extract segments → (retrain) BirdNet

Once the BirdNet weights have been retrained on the data, this model can be used to predict a larger set of field recordings automatically.

This workflow requires:
- Installatuon of BirdNet
- Installation of AviaNZ
- Annotation data conversion from BirdNet to AviaNZ annotations (and backwards)
- Some way to extract segments based on the annotation (using BirdNet/segments.py?)


## Installation of tools

### Miniconda

Because the tools described here require quite different configurations, it is recommended to use conda environments.

Install Miniconda3 according to https://docs.anaconda.com/free/miniconda/#quick-command-line-install:
```
  mkdir -p ~/miniconda3
  wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
  bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
  rm -rf ~/miniconda3/miniconda.sh
```
### AviaNZ

Download the current release from 

### BirdNet
