
import sensor, image, time
thresholds_index = 0

thresholds = [(30, 100, 15, 127, 15, 127), 
              (30, 100, -64, -8, -32, 32), 
              (0, 30, 0, 64, -128, 0)]
              
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.skip_frames(30)
sensor.set_auto_gain(False) # must be turned off for color tracking
sensor.set_auto_whitebal(False) # must be turned off for color tracking
clock = time.clock()




while(True):
    clock.tick()    
    img = sensor.snapshot()
    for blob in img.find_blobs([thresholds[thresholds_index]], pixels_threshold=200, area_threshold=200, merge=True,):
        img.draw_rectangle(blob.rect())
        img.draw_cross(blob.cx(), blob.cy())
    print(clock.fps())