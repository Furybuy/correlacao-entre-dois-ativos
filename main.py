import yfinance as yf 
import numpy as np
import matplotlib.pyplot as gr
import math as m
from scipy import stats

tickers = ['SNAG11.SA', 'KNCA11.SA']
start_date = '2025-01-01'
end_date = '2026-05-10'

res_df = []

for i in range(len(tickers)):
    res_df.append(yf.download(tickers[i], start= start_date, end= end_date))
    
line = len(res_df[0].Close)
col = 2
data_matrix = np.zeros((line, col))

for i in range(line):
    for j in range(col):
        data_matrix[i,j] = res_df[j].iloc[i,j]

eixox=np.arange(line)
ax0=gr.subplot(211)

ax0.plot(eixox,data_matrix[:,0],'--k',label='SNAG11')
ax0.set_title('Comparação entre SNAG11 e KNCA11')


ax1=ax0.twinx()
ax1.plot(eixox,data_matrix[:,1],'-b',label='KNCA11')
gr.legend()
ax1.grid()

res_df[0]['Retorno'] = res_df[0].Close.pct_change(1)
res_df[1]['Retorno'] = res_df[1].Close.pct_change(1)

retorno0 = res_df[0]['Retorno']
retorno1 = res_df[1]['Retorno']

eixR=np.arange(len(retorno0))

ax1=gr.subplot(212)

ax1.plot(eixR,retorno0,'--ok',label='SNAG11')
ax1.set_title('Retornos')

ax2=ax1.twinx()
ax2.plot(eixR,retorno1,'-b',linewidth=1,label='MXRF11')
gr.legend()
gr.grid()

mi0=retorno0.mean()
mi2=retorno1.mean()
sigma1=retorno0.std()
sigma2=retorno1.std()
correl,pval=stats.pearsonr(retorno0[1:],retorno1[1:])

#######################
# Risco de uma carteira formada por 70% de SNAG11 e 30% de KNCA11
#######################
pa=0.7
pb=1-pa
risco_cart=m.sqrt(pa**2*sigma1**2+pb**2*sigma2**2+2*pa*pb*correl*sigma1*sigma2)


#######################
# Risco x Retorno
#######################


p=np.arange(0,1,0.01)    
rc=np.zeros(len(p))
eixCart=np.zeros(len(p))
i=0
min_rc = 1

for x in p:
    y=1-x
    rc[i]=m.sqrt(x**2*sigma1**2+y**2*sigma2**2+2*x*y*correl*sigma1*sigma2)
    eixCart[i]=x
    i=i+1

min_rc = min(rc)

gr.figure()
gr.plot(rc,eixCart,'-k')
gr.grid()
gr.xlabel('risco',fontsize=18)
gr.ylabel('retorno da carteira',fontsize=18)
gr.title('Fronteira Eficiente - (SNAG11, KNCA11)',fontsize=18)
