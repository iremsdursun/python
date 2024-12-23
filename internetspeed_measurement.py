import speedtest
speed = speedtest.Speedtest()
download_speed = speed.download()
upload_speed = speed.upload()
print(f'indirme hızı: {download_speed}')
print(f' yükleme hızı: {upload_speed}')
