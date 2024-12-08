from bing_image_downloader import downloader

fruits = ["apple", "banana", "cherry", "dragon fruit"]

for fruit in fruits:
    downloader.download(fruit, limit=500, output_dir='dataset', adult_filter_off=True, force_replace=False, timeout=60)
