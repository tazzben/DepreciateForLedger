
class DepreciationSchedule:
	"""Class to define depreciation schedule for assets"""
	def __init__(self, typofdepreciation='straight line', periods=1, cost=0, residual=0):
		if typofdepreciation.lower().strip() == 'ddb' or typofdepreciation.lower().strip() == 'double':
			self.typofdepreciation = 'ddb'
		elif typofdepreciation.lower().strip() == 'sum-of-years' or typofdepreciation.lower().strip() == 'sum':
			self.typofdepreciation = 'sum'
		else:
			self.typofdepreciation = 'straight'
		
		if self.is_number(periods) and periods>0:
			self.periods = periods
		else:
			return False
		
		if self.is_number(cost):
			self.cost = cost
		else:
			return False
			
		if self.is_number(residual):
			self.residual = residual
		else:
			return False
	
	def is_number(self, s):
		try:
			float(s)
			if s>=0:
				return True
			else:
				return False
		except ValueError:
			return False	
	
	def Straight(self):
		cost = float(self.cost-self.residual)
		perperiodcost = round(cost/self.periods, 2)
		lastperiod = round(float(cost-perperiodcost*(self.periods-1)), 2)
		schedule = []
		i = 0
		
		while i < self.periods:
			i=i+1
			if i == self.periods:
				schedule.append(lastperiod)
			else:
				schedule.append(perperiodcost)
		
		return schedule
		
	def DDB(self):
		cost = self.cost
		balance = float(cost)
		adjcost = balance - float(self.residual)
		periods = float(self.periods)
		start = 1.0
		end = 2.0
		percentage = end*start/periods
		
		schedule = []
		i = 0
		
		while i < periods:
			i=i+1
			expense = round(float(balance*percentage), 2)
			if i == periods:
				expense = round(adjcost, 2)
			elif expense > adjcost and adjcost>0:
				expense = round(adjcost, 2)
			elif expense > adjcost:
				expense = 0			
			if expense>0:
				schedule.append(expense)
				balance = balance - expense	
				adjcost = adjcost - expense
			
		return schedule
	
	def SumYears(self):
		sumofyears = 0.0
		cost = float(self.cost-self.residual)
		balance = cost
		i = 1;
		cperiod = float(self.periods);
		while i < self.periods+1:
			sumofyears = float(sumofyears+i)
			i=i+1
			
		schedule = []
		
		while cperiod > 0:
			percentage = cperiod/sumofyears
			cperiod = float(cperiod - 1)
			expense = round(float(percentage*cost), 2)
			if cperiod==0:
				expense = round(balance, 2)
			elif expense > balance and balance>0:
				expense = round(balance, 2)
			elif expense > balance:
				expense = 0
			
			if expense>0:
				schedule.append(expense)
				balance = balance - expense
			
			

		return schedule
	
	def Schedule(self):
		if self.typofdepreciation=='ddb':
			return self.DDB()
		elif self.typofdepreciation=='sum':
			return self.SumYears()
		else:
			return self.Straight()
