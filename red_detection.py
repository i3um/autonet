
import sensor, image, time
thresholds_index = 0

thresholds = [(30, 100, 15, 127, 15, 127),  #red 
              (30, 100, -64, -8, -32, 32), #green
              (0, 30, 0, 64, -128, 0)] #blue
              
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.skip_frames(30)
sensor.set_auto_gain(False) 
sensor.set_auto_whitebal(False)
clock = time.clock()




while(True):
    clock.tick()    
    img = sensor.snapshot()
    for blob in img.find_blobs([thresholds[thresholds_index]], pixels_threshold=200, area_threshold=200, merge=True,):
        img.draw_rectangle(blob.rect())
        img.draw_cross(blob.cx(), blob.cy())
    print(clock.fps())
#https://docs.openmv.io/library/omv.image.html#image.image.blob
################################################################################
import sensor, image, time
thresholds_index = 0

thresholds = [(30, 100, 15, 127, 15, 127)]  #red 
red = threshold()

              
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.skip_frames(30)
sensor.set_auto_gain(False) 
sensor.set_auto_whitebal(False)
clock = time.clock()




while(True):
    clock.tick()    
    img = sensor.snapshot()
    for blob in img.find_blobs([thresholds[thresholds_index]], pixels_threshold=200, area_threshold=200, merge=True,):
        if img = red:
            img.draw_circle(blob.rect())
        img.draw_cross(blob.cx(), blob.cy())
    print(clock.fps())  
###################################################
import sensor, image, time, math


thresholds = [(30, 100, 15, 127, 15, 127)] 
              


sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.skip_frames(time = 2000)
sensor.set_auto_gain(False) 
sensor.set_auto_whitebal(False) 
clock = time.clock()


while(True):
    clock.tick()
    img = sensor.snapshot()
    for blob in img.find_blobs(thresholds, pixels_threshold=200, area_threshold=200):
        if blob.elongation() > 0.5:
            img.draw_circle()
            img.draw_edges(blob.min_corners(), color=(255,0,0))
    print(clock.fps())
        
      
 
