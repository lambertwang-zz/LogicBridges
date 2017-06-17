tesseract -psm 6 --tessdata-dir . Image.png output -l mylang
python3 removeExcess.py
