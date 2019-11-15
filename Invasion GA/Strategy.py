
import random
import numpy as np
import copy

class Player():
    def __init__(self,total_turns):
    	self.starting_move='C'
    	self.my_move_history=[]
    	self.opp_move_history=[]
    	self.turn=1
    	self.total_turns=total_turns
    	self.amount=0

    def make_move(self):
    	return None

    def update_amount(self,r):
    	self.amount+=r

    def update_turn(self):
    	self.turn+=1

    def update_move_history(self, my_move, opp_move):
    	self.my_move_history.append(my_move)
    	self.opp_move_history.append(opp_move)

    def total_amount(self):
    	return self.amount

    def is_dead(self):
    	if self.amount<0:
    		return True
    	return False

    def change_move(self,move):
    	if move=='C':
    		return 'NC'
    	elif move =='NC':
    		return 'C'
    	else:
    		print("Error: not a valid choice")
    		return None

    def returnC(self, p):
    	r=random.random()
    	if r<p:
    		return 'C'
    	else:
    		return 'NC'

def rand(s,e):
	r=random.random()
	r*=(e-s)
	r+=s
	return r

def normal():
	return np.random.normal(0,0.02)




class M1(Player):
	# (prob of C given opp played C, prob of C given opp played NC)
	def __init__(self,total_turns,strategy_params):
		Player.__init__(self,total_turns)
		self.starting_move='C'
		self.strategy_params=strategy_params

	def procreate_allM(self):

		new_strat=[]
		for p in self.strategy_params:
			r = normal()
			new_strat.append(max(0,min(1, p+r)))

		kid = M1(self.total_turns,new_strat)
		return kid

	def procreate_oneM(self):

		i = random.randint(0,len(self.strategy_params)-1)
		r = normal()
		new_strat=copy.deepcopy(self.strategy_params)
		new_strat[i]=max(0,min(1, new_strat[i]+r))

		kid = M1(self.total_turns,new_strat)
		return kid

	def make_move(self):
		[c,d]=self.strategy_params
		if self.turn==1:
			return self.starting_move
		else:
			r=random.random()
			if self.opp_move_history[-1]=='C':
				if r<c:
					return 'C'
				return 'NC'
			else:
				if r<d:
					return 'C'
				return 'NC'

class M2(Player): # 2 moves history of opp
	def __init__(self,total_turns,strategy_params):
		Player.__init__(self,total_turns)
		self.starting_move='C'
		self.strategy_params=strategy_params

	def procreate(self):

		new_strat=[]
		for p in self.strategy_params:
			r = rand(-0.1,0.1)
			new_strat.append(min(0,max(1, p+r)))

		kid = M1(self.total_turns,new_strat)
		return kid

	def make_move(self):
		[cc,cd,dc,dd]=self.strategy_params
		if self.turn==1:
			return self.starting_move
		elif self.turn==2:
			r=random.random()
			if self.opp_move_history[-1]=='C':
				self.returnC(cc)
			else:
				self.returnC(cd)

		else:
			r=random.random()
			if self.opp_move_history[-2:]==['C','C']:
				self.returnC(cc)
			if self.opp_move_history[-2:]==['C','NC']:
				self.returnC(cd)
			if self.opp_move_history[-2:]==['NC','C']:
				self.returnC(dc)
			if self.opp_move_history[-2:]==['NC','NC']:
				self.returnC(dd)

class M3(Player):
	def __init__(self,total_turns,starting_move):
		Player.__init__(self,total_turns)
		self.starting_move='C'
		self.opp_defected=False
		self.type="GRIM"

	def make_move(self):
		if self.turn==1:
			return self.starting_move
		else:
			if self.opp_move_history[-1]=='NC':
				self.opp_defected=True
			if self.opp_defected:
				return 'NC'
			else:
				return 'C'
