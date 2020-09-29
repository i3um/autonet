
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

import sensor, image, time, math


thresholds = [(30, 100, 15, 127, 15, 127)] #red 
             
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QQVGA)
sensor.skip_frames(time = 2000)
sensor.set_auto_gain(True) 
sensor.set_auto_whitebal(False) 
clock = time.clock()



while(True):
    clock.tick()
    img = sensor.snapshot()
    #for blob in img.find_blobs(thresholds, pixels_threshold=200, area_threshold=200):
    for c in img.find_circles(threshold = 4000, x_margin = 10, y_margin = 10, r_margin = 10, r_min = 2, r_max = 100, r_step = 2):
        img.draw_circle(c.x(), c.y(), c.r(), color = (0, 0, 255))
        print(c)


#for c in img.find_circles(thresholds, pixels_threshold=200, area_threshold=200):
       # if blob.elongation() > 0.5:
           # blob.enclosing_circle()
           # img.draw_edges(blob.min_corners(), color=(255,0,0))
           # img.draw_circle((img.width()//2), (img.height()//2), 20, color = (0, 0, 255), thickness = 2, fill = False)
            
                
      
 #https://github.com/openmv/openmv/blob/master/scripts/examples/10-Color-Tracking/multi_color_blob_tracking.py
##################################################

import sensor, image, time, math


thresholds = [(30, 100, 15, 127, 15, 127)] #red
roi = [0, 0, 0, 0]
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QQVGA)
sensor.skip_frames(time = 2000)
sensor.set_auto_gain(True)
sensor.set_auto_whitebal(False)
clock = time.clock()



while(True):
    clock.tick()
    img = sensor.snapshot()
    #for blob in img.find_blobs(thresholds, pixels_threshold=200, area_threshold=200):
    for c in img.find_circles(threshold = 4000, x_margin = 10, y_margin = 10, r_margin = 10, r_min = 2, r_max = 100, r_step = 2):
        img.draw_circle(c.x(), c.y(), c.r(), color = (0, 0, 255))
        roi[0] = c.x() + c.r() 
        roi[1] = c.y() + c.r() 
        roi[2] = c.r() * 2
        roi[3] = c.r() * 2
        r = img.find_rects(roi, threshold = 10000)
        if r: 
            img.draw_rectangle(r[0].rect(), color = (255, 0, 0))
        print(c)   






#for p in r.corners():
                   # img.draw_circle(p[0], p[1], 5, color = (0, 255, 0))
                #print(r)
    



# if blob.elongation() > 0.5:
    # blob.enclosing_circle()
           # img.draw_edges(blob.min_corners(), color=(255,0,0))
           # img.draw_circle((img.width()//2), (img.height()//2), 20, color = (0, 0, 255), thickness = 2, fill = False)

