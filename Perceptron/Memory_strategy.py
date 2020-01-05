
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
    	self.type=None

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

class Mperp(Player): # A player with random attributes, mutation rate var, and memory given by (my_memory,opp_memory), with percepton reulatory network
	def __init__(self,total_turns,var,my_memory,opp_memory,layer_list):
		Player.__init__(self,total_turns)
		self.starting_move='C'
		weight_list=[my_memory+opp_memory]+layer_list
		bias_list=layer_list+[1]
		self.weights=[]
		self.bias=[]
		temp=[]
		temp2=[]
		for i in range(weight_list[n]):
			temp2.append(random.random())
		for j in range(bias_list[n]):
			temp.append(copy.deepcopy(temp2))
		for n in range(len(weight_list)):
			self.weights.append(copy.deepcopy(temp))

		self.normalize_weights()

		for n in bias_list:
			temp=[]
			for i in range(n):
				temp.append(random.random())
			self.bias.append(temp)

		#Memory is stored as a set of weights and bias
		#Final value 1 or 0 correpsonds to playing C or NC
			
		self.var=var
		self.my_memory=my_memory
		self.opp_memory=opp_memory
		self.type='Mperp_'+str(var)+'_'+str(my_memory)+'_'+str(opp_memory)+'_'+str(layer_list)
		#print(self.type,"  ",my_memory,"  ",opp_memory)

	def normalize_weights(self):
		for layer_no,layer in enumerate(self.weights):
			for node_no,node in enumerate(layer):
				sumw=0
				for w in node:
					sumw+=w
				for w_no,w in enumerate(node):
					if sumw!=0:
						self.weights[layer_no][node_no][w_no]/=sumw
					else:
						self.weights[layer_no][node_no][w_no]=1/len(node)

	def normalp(self):
		return np.random.normal(0,self.var)

	def procreate_allM(self):

		new_strat=[]
		for p in self.strategy_params:
			r = self.normalp()
			new_strat.append(max(0,min(1, p+r)))

		kid = Mn(self.total_turns,self.var,self.my_memory,self.opp_memory,new_strat)
		return kid

	def procreate_oneM(self):

		i = random.randint(0,len(self.strategy_params)-1)
		r = normalp()
		new_strat=copy.deepcopy(self.strategy_params)
		new_strat[i]=max(0,min(1, new_strat[i]+r))

		kid = Mn(self.total_turns,self.var,self.my_memory,self.opp_memory,new_strat)
		return kid

	def getp_from_strategy_params(self,para_list):
		
		return

	def make_move(self):
		if self.turn==1:
			return self.starting_move
		elif self.turn<max(self.my_memory,self.opp_memory):
			#Make better
			return self.returnC(0.5)
		else:
			
			return 
