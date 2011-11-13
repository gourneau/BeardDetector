import SimpleCV
import time

c = SimpleCV.Camera(1)
js = SimpleCV.JpegStreamer() 

while(1):
  img = c.getImage()
  img = img.smooth()
  img = img.dilate()
  img = img.erode()
  lines = img.findLines(threshold=25,minlinelength=20,maxlinegap=20)
  [line.draw(color=(255,0,0)) for line in lines]
  sum = 0
  for line in lines:
      sum = line.length() + sum
  if sum:
      print sum / len(lines)
  else:
      print "No beard found!"
  img.save(js.framebuffer)
  time.sleep(0.1)