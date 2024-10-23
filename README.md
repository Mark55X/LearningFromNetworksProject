# LearningFromNetworksProject
Learning from network projects for unipd

Idea generale:
- Dai dati forniti dalle API (storici) eseguiamo dei meccanismi di inferenza statistica per ottenere al distribuzione di probabilità. 
- Creaimo il grafo (pytthon) con arco variabili aleatorie associate alla distribzuione di probabilità.
- Svolgiamo del sampling ottenuto con l'inverse transofmr sampling
- Otteniamo quindi tante istanze del nostro grafo -> GRAFI EFFETTIVI con pesi


- Un approccio base è quello di svolgere la media 
- Diversi approcci come quello di utilizzare un unico grafo basandosi sulla apsettazione di ogni variabile 

PER RICERCA DEI CICLI:
- Da una valuta BFS oppure posso applicare BFS su tutti i nodi
- Variate di dijkstra
- Dopo aver ottenuto quali nodi che riguardano cicli, faccio la somma dei log dei pesi ( o meglio la può gia fare in se l'algoritmo che rebbe quindi una variante)
- QUelli che noi cerchiamo sono i vlaori > 0 o < 0 in base a cosa mi restituisce l'algoritmo (se min o max)


- In questi approcci si usa qualcos adi definito, invece possiamo dare questo compito ad un algorimto di ML/ deep learning:
- rete neurale  cui didamo in pasto i grafi (UN INPUT -> UN ISTANZA DI UN GRAFO e altre possibili features tra cui betweness): quindi si potrebbe utilizzare l'apporccio STRUTTURATO dove l'input è una matrice di adiacenza, oppure input NON STRUTTURATO ovvero l'istanza del grafo stesso.
- L'output è una matrice di adiacenza che rappresenta una madschera ìdei rami che sono selezionati per l'individuazione dei  cicli a guadagno positivo
- Ciò significa che per l'allenamento ogni inout è associato ad una maschera calcolata tramite un algoritmo (tra quelli di ricerca dei cicli o MILP)
- L'output definitivo della rete neurale ALLENATA è una maschera che però non potrebbe essere perfetta (ovvero ci sono edge a 0 che dovrebbero esser ad 1 e viceversa). Possibile soluzione: COllegare solamente le connected components che non contengono cicli sotto l'assunzione che il grafo sia completo (nel nostro caso lo è)

DATASET:
- nei csv di binance faccio la terxza colonna / la quarta colonna -> ottengo il tasso di cambio teoricamente
- 
## Notes

### Note Marco

#### API exchange
- [BINANCE](https://developers.binance.com/docs/binance-spot-api-docs/rest-api\#exchange-information\item): forse il più attendibile essendo motore per comprare/vendere crypto. Richiede di aver versato dei soldi nel conto.

- [API](https://github.com/fawazahmed0/exchange-api) gratuita, che fornisce dati solo una volta al giorno. No login. Il problema è che non dice la fonte. Saranno dati anche veritieri ma ci serve la fonte.

- [API](https://exchangerate.host/documentation) che aggiorna i suoi dati ogni 10 minuti secondo la documentazione. Richiede accesso con tokern gratuito massimo 100 richieste, contiene le Historical Rates.

- Anche questo è un [dataset](https://www.kaggle.com/datasets/dhruvildave/currency-exchange-rates) interessante. Con exchange di 130 valute. Da capire la validità. Ci sono degli errori come si può notare da [qua](https://www.kaggle.com/discussions/general/234811), non so se siano stati risolti. 
Sarebbe da approfondire se colossi danno i dati sottoforma di dataset perche tanto ci serve lo storico.

- Bel [dataset](https://www.kaggle.com/datasets/kaushiksuresh147/top-10-cryptocurrencies-historical-dataset) ma come base solo i dollari. 
		
- POSSIBILE [DATASET](https://www.binance.com/en/support/faq/how-to-download-historical-market-data-on-binance-5810ae42176b4770b880ce1f14932262) DI BINANCE

#### Ricerca enumerazione cicli
Alcuni algoritmi che possono riguardare l'individuazione e l'enumerazione dei cicli:
- Johnson's Algorithm: per grafi diretti e indiretti O((n+e)(c+1)) con c numero di cicli
- Tiernan's Algorithm: per grafi indiretti. O(V+E+C)
- Paton’s Algorithm: per grafi indiretti
- Hawick and James Algorithm: https://www.researchgate.net/publication/221440635_Enumerating_Circuits_and_Loops_in_Graphs_with_Self-Arcs_and_Multiple-Arcs
### Note Edoardo

#### Arbitraggio

In economia e finanza, un [arbitraggio](https://it.wikipedia.org/wiki/Arbitraggio) è un'operazione che consiste nell'acquistare un bene o un'attività finanziaria su un mercato rivendendolo su un altro mercato, sfruttando le differenze di prezzo al fine di ottenere un profitto.  
L'operazione è possibile se il ricavo che si ottiene supera i costi per il trasferimento del bene trattato da un mercato all'altro. L'intera operazione deve essere senza alcun rischio per l'operatore.

#### Currency Arbitrage

- **Circular Arbitrage**: penso sia quello che interessa a noi, è un tipo di arbitraggio nel quale si sfruttano 3 o più valute in un ciclo in modo da ottenere alla fine di esso un guadagno sfruttando la disparità nei tassi di cambio.
		
- **Exchange Arbitrage**: cerca un guadagno attraverso le differenze di cambio tra diverse piattaforme di trading. Quindi non c'entra nulla con ciò di cui abbiamo bisogno.

- Ho trovato questa [tesi](https://www.theseus.fi/handle/10024/795754) che parla in alcuni punti di cose simili alle nostre. In particolare accenna all'uso di alcune API per il reperimento dei tassi di cambio.  
Per la ricerca di un profitto utilizza il DFS e ne analizza anche la complessità.

#### Currency Speculation
- Differisce dal *Currency Arbitrage* nel fatto che (da come ho capito) si basa su previsioni di mercato e di conseguenza è più rischiosa.  
Le opportunità di arbitraggio teoricamente durano pochi istanti mentre nella speculazione, prevedendo l'andamento del mercato, si basa su istanti temporali maggiori generando un maggior rischio.  
Quindi potremo parlare pure di questo topic o fare una differenza tra i due.

#### Possibili Algoritmi
 - Dijkstra non possiamo usarlo se usiamo la scala logaritmica con il - davanti, in quanto non gestisce pesi negativi. Ho trovato che c'è Bellman-Ford e Floyd-Warshall.
 - In breve [Bellman-Ford](https://www.mdpi.com/2227-7390/12/16/2590) parte da un singolo nodo (minor complessità)
 - [Floyd-Warshall](https://www.sciencedirect.com/science/article/pii/S002001901000027X) analizza tutte le coppie del grafo (ha una complessità cubica) però potrebbe essere quello che ci interessa. Devo ancora leggere nello specifico le differenze però potrebbero essere due algoritmi da confrontare.
 - Algoritmo ibrido [Bellman-Ford+Dijkstra](https://www.sciencedirect.com/science/article/pii/S1570866717300011)

### Note Luigi

#### API exchange
- [exchange-api](https://swapzone.io/partners/exchange-api) offre un'[API](https://documenter.getpostman.com/view/16362858/UVXokDS6#06a5c43d-be60-45ef-8b76-161bf275c5bd) che sembra proprio fare al caso nostro. Non fornisce lo storico però e bisogna capire se è accessibile in modo gratuito.
l'[API](https://documenter.getpostman.com/view/16362858/UVXokDS6#898f2264-7286-41a4-8843-bf143a67a6ab) permette di fare un interrogazione puntuale.
- [ExchangeController](https://simpleswap.io/affiliate-program/en/how-to-start/api?ref=660adad2c784&utm_source=coinmonks&utm_medium=sponsored&utm_campaign=API) ha diverse [API](https://api.simpleswap.io/#/Exchange/ExchangeController_getEstimated)

- In generale in questo [articolo](https://medium.com/coinmonks/best-crypto-apis-for-developers-5efe3a597a9f) ci sono diversi fornitori da analizzare
