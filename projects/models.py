from django.db import models

class Project(models.Model):
	name = models.CharField('Project Name', max_length=120)
	description = models.CharField('Description', max_length=300)
	create_date = models.DateField('Date Identified')
	orig_est_cost = models.DecimalField('Estimated Cost', blank=True, max_digits=7, decimal_places=0)
	start_date = models.DateField('Start Date', blank=True)
	complete_date = models.DateField('Date Complete', blank=True)
	complete_cost = models.DecimalField('Cost', blank=True, max_digits=9, decimal_places=2, null=True)

	def __str__(self):
		return self.name

class Expense(models.Model):
	project = models.ForeignKey(Project, blank=True, null=True, on_delete=models.DO_NOTHING)
	invoice_date = models.DateField('Invoice Date')
	paid_date = models.DateField('Paid Date')
	vendor = models.CharField('Vendor', max_length=120)
	amount = models.DecimalField('Amount', max_digits=9, decimal_places=2)


	def __str__(self):
		return self.name
