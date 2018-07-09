#!user/bin/python
# encoding:utf-8
a = "insert into tb_character(`id`,`userId`,`channelId`,`petId`,`petResId`,`username`,`nickname`,`sexTyp`,`coin`,`gold`,`quenching`,`hunTiandan`,`jiuZhuandan`,`totalPay`,`credit`,`payReward`,`lastPaydate`,`level`,`refineExp`,`energy`,`extraEnergy`,`power`,`extraPower`,`packageSize`,`extraPacksize`,`matrix`,`matrixIds`,`spriteId`,`maxCombo`,`totalAtk`,`isOnline`,`activetime`,`outtime`,`createtime`,`donttalk`,`guankaId`,`starId`,`hasheroIdList`,`lastlogindate`,`loginTimes`,`notwarEndtime`,`mendSignNum`,`mendSignindate`,`guideMap`) values('113713','10000','35','10003','41099','DCA6521A09E8D3B087C9607D6836B126','崔芮','0','30000','70','1','0','0','0.0','0','0','NULL','1','0','30','0','120','0','24','0','[-1, 10003L, -1, -1, -1, -1, -1, -1, -1]','[(-1,0),(4109901,1),(-1,0),(-1,0),(-1,0),(-1,0),(-1,0),(-1,0),(-1,0)]','-1','0','1508','0','2016-07-06 12:39:28','2016-07-06 12:39:28','2016-07-05 20:31:35','0','0','1','[41099L, 41001]','2016-07-06 10:36:02','2','2016-07-05 20:31:35','0','0','{1: 2}')"
import datetime
print datetime.datetime.now()
c = a.split("values")
print c[0]
print c[1]