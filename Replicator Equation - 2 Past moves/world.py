import matplotlib.pyplot as plt
import Strategy
import Evolution

def plot(pop_series):
	for j in pop_series:
		print(j[-1],end=" ")
	print("")

	for ps in pop_series:
		plt.plot(ps)
	plt.show()

def world(no_worlds,days,pop_density):
	pop_series=[]
	for p in pop_density:
		pop_series.append([])

	for ps in range(len(pop_series)):
		for i in range(days):
			pop_series[ps].append(0)

	#Add pop series from many worlds
	for k in range(no_worlds):
		print(k)

		ptypes = [Strategy.ALLC,Strategy.ALLD,Strategy.Random,Strategy.GRIM,Strategy.TFT,Strategy.TTFT,Strategy.TFTT,Strategy.STFT,Strategy.PAVLOV]
		game_para=[0.5, 0, 1, 0.2]
		total_turns=20
		total_res=1000	

		r=Evolution.Replicator(game_para,total_turns,total_res,ptypes,pop_density)
		tempps=r.play_days(days)
		for ps in range(len(pop_series)):
			for d in range(days):
				pop_series[ps][d]+=tempps[ps][d]

	#Take average of all worlds
	for ps in range(len(pop_series)):
		for d in range(days):
			pop_series[ps][d]/=no_worlds

	plot(pop_series)

total_turns=20
total_res=1000	
world(100,30,pop_density =[1,1,1,1,1,1,1,1,1])