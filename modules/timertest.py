def timer_test(phenny):
   print "sending msg"
   while not phenny.connected:
      phenny.time.sleep(1)
   phenny.msg(phenny.config.broadcast_channel, "HI SOURS!")
   phenny.add_timer(3, timer_test)
timer_test.timer = 3
