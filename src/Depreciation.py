from decimal import *
class DepreciationSchedule:
	"""Class to define depreciation schedule for assets"""
	def __init__(self, typofdepreciation='straight line', periods=1, cost=0, residual=0):
		if typofdepreciation.lower().strip() == 'ddb' or typofdepreciation.lower().strip() == 'double':
			self.typofdepreciation = 'ddb'
		elif typofdepreciation.lower().strip() == 'sum-of-years' or typofdepreciation.lower().strip() == 'sum':
			self.typofdepreciation = 'sum'
		elif typofdepreciation.lower().strip() == 'mixed' or typofdepreciation.lower().strip() == 'hybrid':
			self.typofdepreciation = 'mixed'
		else:
			self.typofdepreciation = 'straight'
		
		if self.is_number(periods) and periods>0:
			self.periods = Decimal(str(periods))
		else:
			return False
		
		if self.is_number(cost):
			self.cost = Decimal(str(cost))
		else:
			return False
			
		if self.is_number(residual):
			self.residual = Decimal(str(residual))
		else:
			return False
	
	def is_number(self, s):
		try:
			Decimal(str(s))
			if s>=0:
				return True
			else:
				return False
		except ValueError:
			return False	
	
	def Straight(self):
		cost = Decimal(self.cost-self.residual)
		perperiodcost = round(cost/self.periods, 2)
		lastperiod = round(cost-Decimal(str(perperiodcost))*(self.periods-Decimal('1')), 2)
		schedule = []
		i = 0
		
		while i < int(self.periods):
			i=i+1
			if i == int(self.periods):
				if lastperiod>0:
					schedule.append(lastperiod)
			else:
				if perperiodcost>0:
					schedule.append(perperiodcost)
		
		return schedule
		
	def DDBMixed(self):
		cost = self.cost
		balance = cost
		adjcost = balance - self.residual
		periods = self.periods
		start = Decimal('1.0')
		end = Decimal('2.0')
		percentage = Decimal(end*start/periods)

		schedule = []
		i = 0
		newperiods = int(round(periods/end))
		remainginperiods = int(Decimal(periods - Decimal(newperiods)));
		while i < newperiods:
			i=i+1
			expense = round(balance*percentage, 2)
			if i == int(newperiods) and int(remainginperiods) <= 0:
				expense = round(adjcost, 2)
			elif Decimal(str(expense)) > adjcost and adjcost>0:
				expense = round(adjcost, 2)
			elif Decimal(str(expense)) > adjcost:
				expense = 0			
			if expense>0:
				schedule.append(expense)
				balance = balance - Decimal(str(expense))	
				adjcost = adjcost - Decimal(str(expense))	
		
		if remainginperiods > 0:
			sl = DepreciationSchedule('straight line', remainginperiods, balance, self.residual)
			sld = sl.Schedule()
			schedule.extend(sld)
		return schedule

	def DDB(self):
		cost = self.cost
		balance = cost
		adjcost = balance - self.residual
		periods = self.periods
		start = Decimal('1.0')
		end = Decimal('2.0')
		percentage = end*start/periods
		
		schedule = []
		i = 0
		
		while i < int(periods):
			i=i+1
			expense = round(balance*percentage, 2)
			if i == int(periods):
				expense = round(adjcost, 2)
			elif Decimal(str(expense)) > adjcost and adjcost>0:
				expense = round(adjcost, 2)
			elif Decimal(str(expense)) > adjcost:
				expense = 0			
			if expense>0:
				schedule.append(expense)
				balance = balance - Decimal(str(expense))	
				adjcost = adjcost - Decimal(str(expense))			
		return schedule
	
	def SumYears(self):
		sumofyears = 0
		cost = self.cost-self.residual
		balance = cost
		i = 1;
		cperiod = int(self.periods);
		while i < int(self.periods)+1:
			sumofyears = sumofyears+i
			i=i+1
		sumofyears = Decimal(sumofyears)
		schedule = []
		
		while cperiod > 0:
			percentage = Decimal(cperiod)/sumofyears
			cperiod = cperiod - 1
			expense = round(percentage*cost, 2)
			if cperiod==0:
				expense = round(balance, 2)
			elif Decimal(str(expense)) > balance and balance>0:
				expense = round(balance, 2)
			elif Decimal(str(expense)) > balance:
				expense = 0
			
			if expense>0:
				schedule.append(expense)
				balance = balance - Decimal(str(expense))

		return schedule
	
	def Schedule(self):
		if self.typofdepreciation=='ddb':
			return self.DDB()
		elif self.typofdepreciation=='sum':
			return self.SumYears()
		elif self.typofdepreciation=='mixed':
			return self.DDBMixed()
		else:
			return self.Straight()
