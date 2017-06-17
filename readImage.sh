tesseract -psm 6 --tessdata-dir . $1 output -l mylang
python3 removeExcess.py
