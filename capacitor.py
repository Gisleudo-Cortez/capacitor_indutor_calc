import math
import numpy as np
import matplotlib.pyplot as plt

# retorna a capacitância em Farads
def capacitancia(Q, V):
	return Q / V

# coulombs de carga, calcula a carga 'Q' para um valor de eletrôns aplicados numa palca
def coulomb_carga(e):
	return e * (1 / (6.242 * 10 ** -18))

def capacitancia_série(list_cap = []): # recebe uma lista de capacitores e retorna o resultado em paralelo. ex: [10,20,30,40]
	cap_cumulative = 0
	for c in list_cap:
		cap_p = 1 / c
		cap_cumulative += cap_p
		cap_final = 1 / cap_cumulative
	return cap_final

def capacitancia_paralelo (list_cap = []): # recebe uma lista de capacitores e retorna o resultado em série. ex: [10,20,30,40]
	return sum(list_cap)

def constante_de_tempo (R, C): # calcula a constante tau, observar os valores para ajustar a unidade de tempo. Resultado parão em segundos
	return R * C

def tensao_no_tempo(V_f,V_i,tau,t): # calcula a tensão do capacitor em relação a o tempo passado
	V_C = V_f + (V_i - V_f) * (math.e ** (-(t*tau)/tau))
	return V_C

def carga_em_funcao_do_tempo_plotagem (vc, tau, t): # plota o grafico da voltagem em função do tempo
	V_C = lambda x : vc - vc * math.e ** (-(x*tau)/tau)
	x = np.linspace(0, t, 100, endpoint = True)
	y = []
	for time in x:
		v_t = V_C(time)
		y.append(v_t)
	#plotagem
	plt.plot(x, y, alpha = 0.6, color = 'black', linestyle = 'dotted')
	plt.xlabel('t * \u03C4')
	plt.ylabel('Voltagem')
	plt.show()

def carga_em_funcao_do_tempo (vc, tau, t): # retorna uma lista com a voltagem vc em funcao do tempo
	V_C = lambda x : vc - vc * math.e ** (-(x*tau)/tau)
	x = np.linspace(0, t, 1000, endpoint = True)
	y = []
	for time in x:
		v_t = V_C(time)
		y.append(v_t)
	return y


# plota o grafico da corrente média em função do tempo (em segundos)
# *usar tempo igual a t da carga em função do tempo*
# a lista_vc deve ser calculada com a função 'carga_em_funcao_do_tempo'
def corrente_media_em_funcao_do_tempo_plotagem (c, lista_vc, tempo):  
	x = np.linspace(0, tempo, len(lista_vc)-1, endpoint = True)
	y = []
	for pos in range(len(lista_vc)-1):
		if pos > 0:
			var_vc = lista_vc[pos] - lista_vc[pos -1]
			i_med = c * (var_vc / x[pos])
			y.append(i_med)
		else:
			var_vc = lista_vc[pos]
			i_med = c * (var_vc / x[pos])
			y.append(i_med)
	plt.plot(x,y)
	plt.xlabel('segundos (s)')
	plt.ylabel('mili ampere (mA)')
	plt.show()


