# importação dos módulos, disponibilizando as funções nesse programa
import capacitor
import indutor

# utilização das funções importadas
# voltagem_capacitor 
vc = 40
# tau
tau = 0.560
# intervalos de tempo
t = 5

# plotagem da carga em função do tempo
capacitor.carga_em_funcao_do_tempo_plotagem(vc, tau, t)

# plotagem da resposta transitoria da corrente indutor
E = 50
R = 2000
tau = 0.002
indutor.resposta_transitoria_corrente_plotagem(E, R, tau, t)

# código de cores
valor_cores = indutor.codigo_de_cores('vermelho', 'violeta', 'marrom', 'ouro')
print(valor_cores)