#coding=utf-8
#! user/bin/python

import random
def create(str):
	"双色球的机选实现,有去重复号码"
	if(str =='y' or str.lower() =='y'):

		num = 0
		c=[]
		d=[]
		a="红"
		b="蓝"
		while num<6:
			num=num+1
			cc=random.choice(range(1,33))
			if c.count(cc)==1 :
				num=num-1
				continue
			elif cc<10: 
				print a,
				print "%d%d" %(0,cc),
			else:
				print a,cc,
		else:
			dd=random.choice(range(1,17))
		if dd<10:
			print b,"%d%d" %(0,dd)
		else:
			print b,dd,
		return

	else:
		return

while 1:
	print "\n------------------"
	print "----双色球摇奖------"
	print "----启动y-----------"
	print "----其它停止--------"
	print "--------------------"
	str1=raw_input()
	if str1=='y':
		create(str1)
	else:
		break

