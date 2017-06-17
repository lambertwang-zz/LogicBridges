#!/bin/bash
tesseract -psm 6 --tessdata-dir . Image.png output -l myl
python3 removeExcess.py
