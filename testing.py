from bing_image_downloader import downloader
import schedule
import time
import shutil



#shutil.make_archive(output_filename, 'zip', dir_name)


def task():


    downloader.download('cat', limit=10,  output_dir='dataset', adult_filter_off=True, force_replace=False, timeout=60,resize=(224,224) ,verbose=True)
    shutil.make_archive('ds', 'zip', 'dataset')
schedule.every(1).minutes.do(task)
while True:
    schedule.run_pending()
    time.sleep(1)