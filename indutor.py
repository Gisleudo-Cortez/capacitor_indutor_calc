import numpy as np
import matplotlib.pyplot as plt

# parâmetros básicos dos indutores

# permeabilidade(mu) do ar
mu_ar = 4 * np.pi * 10**-7 # Wb/A *m

# intensidade do fluxo
def intensidade (wb, area):
	return  wb / area # em Wb/m² ou teslas (T)

# força magnetomotriz amperes-espira
def ampere_espira(N,I):
	return N * I # ampére-espira ou Ae

# permeabilidade relativa ao ar
def permeabilidade_relativa (mu):
	return mu / mu_ar

# não precisa elevar o valor da área ao quadrado. manter consistência nas unidades inseridas
def indutancia(mu, Num_espiras, area, comprimento):
	return (mu*(Num_espiras**2)*area)/comprimento

# calculo de código de cores de indutor
# inserir os nomes das cores nos valores
## retorna os valores em micro henries ##
def codigo_de_cores(primeiro, segundo, multiplicador, tolerancia):
	primeiro = primeiro.lower()
	segundo = segundo.lower()
	multiplicador = multiplicador.lower()
	tolerancia = tolerancia.lower()
	algarismo = {'preto':'0', 'marrom':'1', 'vermelho':'2', 'laranja':'3', 
	'amarelo':'4', 'verde':'5', 'azul':'6', 'violeta':'7', 'cinza':'8', 'branco':'9', 'ouro': '.'}
	dict_multiplicador = {'preto':1, 'marrom':10, 'vermelho':100, 'laranja':1000}
	dict_tolerancia = {'nenhuma':20, 'prata':10, 'ouro':5}

	primeiro = algarismo.get(primeiro)
	segundo = algarismo.get(segundo)
	multiplicador = dict_multiplicador.get(multiplicador)
	tolerancia = dict_tolerancia.get(tolerancia)

	valor = int(primeiro + segundo) * multiplicador
	tol_pos, tol_neg = valor + valor*(tolerancia/100), valor - valor*(tolerancia/100)
	print(f'tolerância de {tolerancia}% de : {tol_pos} \u03BCH até {tol_neg} \u03BCH ')
	return valor

# faz a plotagem da corrente em relação o tempo e monta um grafico
# t = numero final das constantes de tempo EX: 5 * tau
def resposta_transitoria_corrente_plotagem(E, R, tau, t):
	I_L = lambda x :(E/R)*(1 - np.exp(1)**(- x * tau/tau))
	x = np.linspace(0, t, 100, endpoint = True)
	y = []
	for time in x :
		i_t = I_L(time)
		y.append(i_t)
	plt.plot(x, y, alpha = 0.6, color = 'black', linestyle = 'dotted')
	plt.ylabel('Ampères')
	plt.xlabel('\u03C4')
	plt.show()

# corrente máxima ou de estado estacionário
def corrente_maxima(E,R):
	return E / R

# resposta da corrente em tempo especifico
def resposta_transitoria_corrente(E, R, tau, t):
	I_L = (E/R)*(1 - np.exp(1)**(- t * tau/tau))
	return I_L

# constante de tempo para indutor em Segundos
def constante_de_tempo(L, R):
	return L/R

# plotagem da tensão da bobina no tempo
def tensao_da_bobina_plotagem(E, tau, t):
	x = np.linspace(0, t, 100, endpoint = True)
	vl = lambda x : E * np.exp(1) ** (- x * tau / tau)
	y = []
	for time in x:
		vt = vl(time)
		y.append(vt)
	# plotagem
	plt.plot(x, y, alpha = 0.6, color = 'black', linestyle = 'dotted')
	plt.xlabel('\u03C4')
	plt.ylabel('Volts')
	plt.show()

# tensão através da bobina Volts
def tensao_da_bobina(E, tau, t):
	V_L = E * np.exp(1)**(- t * tau/tau)
	return V_L

# indutores em série
# usar uma lista com os valores das indutâncias, manter a unidade igual para calculos
def indutancia_serie(n=[]):
	return np.sum(n)

# indutores em paralelo
# usar uma lista com os valores das indutâncias, manter a unidade igual para calculos
def indutancia_paralelo(n=[]):
	ind_cumulative = 0
	for ind in n:
		ind_p = 1 / ind
		ind_cumulative += ind_p
		ind_final = 1 / ind_cumulative
	return ind_final

# energia armazenada indutor em joules
def energia_armazenada(L, I):
	W = 1/2 * L * I **2
	return W

print(indutancia_paralelo([10]))
