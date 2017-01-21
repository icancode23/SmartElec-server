from django.db import models
 #One table for all users
class User(models.Model):
	identifier=models.IntegerField(default=0,unique=True)
	name=models.CharField(max_length=256)
	creditUnits=models.IntegerField(default=0)
	def __unicode__(self):
	 	return self.name

class UserTransaction(models.Model):
	transactionid=models.IntegerField(default=0,unique=True)
	transactionUnitAmount=models.IntegerField(default=0)
	numberTransactionUnits=models.IntegerField(default=0)
	transactionUserId=models.IntegerField(default=0)
	user=models.OneToOneField(User,  on_delete=models.CASCADE)
	def __unicode__(self):
		return self.transactionid

class UserTask(models.Model):
	taskId=models.IntegerField(default=0,unique=True)
	taskHour=models.IntegerField(default=0)
	taskMinutes=models.IntegerField(default=0)
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	def __unicode__(self):
		return self.taskId

class DailyLog(models.Model):
	day=models.IntegerField(default=0,unique=True)
	month=models.IntegerField(default=0)
	year=models.IntegerField(default=0)

	
	predicted_low=models.IntegerField(default=0)
	current_rate=models.IntegerField(default=0)
	def __unicode__(self):
		return self.month

class Device(models.Model):
	deviceStatus=models.BooleanField(default=False)
	deviceid=models.IntegerField(unique=True)
	devicerating=models.CharField(default="0 W",max_length=255)
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	def __unicode__(self):
		return self.deviceName	



