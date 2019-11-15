import DH_Game
import Strategy
import random
import matplotlib.pyplot as plt

class Replicator():
	def __init__(self,game_para,total_turns,total_res,pop):
		self.game = DH_Game.Game(game_para)
		self.pop=pop
		self.total_res=total_res
		self.total_turns=total_turns
		self.consumption= total_turns
		self.reproduce_cost=total_turns

	def random_player(self):
		if(len(self.pop)<2):
			print("Error: Pop is less than 2")
			return None
		return random.randint(0,len(self.pop)-1)
		

	def play_match(self,p1_indx,p2_indx):
		#self.generate_fresh_pop()
		
		p1=self.pop[p1_indx]
		p2=self.pop[p2_indx]

		for i in range(0,self.total_turns):
			p1_move=p1.make_move()
			p2_move=p2.make_move()
			p1_reward,p2_reward = self.game.payoff(p1_move,p2_move)

			p1.update_turn()
			p1.update_amount(p1_reward)
			p1.update_move_history(p1_move,p2_move)

			p2.update_turn()
			p2.update_amount(p2_reward)
			p2.update_move_history(p2_move,p1_move)

	def play_day(self):
		#Daytime
		if self.pop==[]:
			print("Error: No Pop")
		elif len(self.pop)==1:
			pop[1].update_reward(game.max_reward()*self.total_turns)
		else:
			for r in range(self.total_res):
				p1_indx=self.random_player()
				p2_indx=self.random_player()
				while(p1_indx==p2_indx):
					p2_indx=self.random_player()
				self.play_match(p1_indx,p2_indx)

		#Nighttime
		new_pop=[]
		for p in self.pop:
			p.update_amount(-self.consumption)
			if not p.is_dead():
				while (p.total_amount()>self.reproduce_cost):
					kid=p.procreate_oneM()
					new_pop.append(kid)
					p.update_amount(-self.reproduce_cost)
					#print("***",p.strategy_params,"-->",kid.strategy_params)
				new_pop.append(p)
			#else :
				#print("***",p.strategy_params)

		self.pop = new_pop

	def append_to_popseries(self,pop_series,vocab):
		if(vocab=="pop types"):
				pop_density=[0,0,0,0,0]
				for p in self.pop:
					for i in range(1,6):
						if p.strategy_params[0]+p.strategy_params[1] <=0.4*i:
							pop_density[i-1]+=1
							break
				for i in range(5):
					pop_series[i].append(pop_density[i])

		elif(vocab=="avg"):
			c=0
			d=0
			for p in self.pop:
				c+=p.strategy_params[0]
				d+=p.strategy_params[1]
			c/=len(self.pop)
			d/=len(self.pop)
			pop_series[0].append(c)
			pop_series[1].append(d)

		elif(vocab=="avg reward"):
			r=0
			for p in self.pop:
				r+=p.total_amount()
			r/=len(self.pop)
			pop_series[0].append(r)

		return pop_series


	def play_days(self,n,vocab):
		if(vocab=="pop types"):
			pop_series=[[],[],[],[],[]]
		elif(vocab=="avg"):
			pop_series=[[],[]]
		elif(vocab=="avg reward"):
			pop_series=[[]]

		pop_series=self.append_to_popseries(pop_series,vocab)

		for i in range(n):
			if i%100 ==0:
				print(i," days")

			self.play_day()
			pop_series=self.append_to_popseries(pop_series,vocab)
			
		self.plot(pop_series)
		for p in self.pop:
			print(p.strategy_params)

		return self.pop

	def plot(self,pop_series):
		for j in pop_series:
			print(j[-1],end=" ")
		print("")

		for ps in pop_series:
			plt.plot(ps)
		plt.show()

game_para=[0.5, 0, 1, 0.2]
total_turns=100
total_res=100
pop=[]
for i in range(40):
	#pop.append(Strategy.M1(total_turns,[1,0]))
	#pop.append(Strategy.M1(total_turns,[0,0]))
	pop.append(Strategy.M1(total_turns,[1,0]))

r=Replicator(game_para,total_turns,total_res,pop)
r.play_days(40000,"pop types")

