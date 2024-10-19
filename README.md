# LearningFromNetworksProject
Larning from network projects for unipd

	\section{Note Edoardo}
	\subsection{Arbitraggio} (wikipedia): In economia e finanza, un arbitraggio è un'operazione che consiste nell'acquistare un bene o un'attività finanziaria su un mercato rivendendolo su un altro mercato, sfruttando le differenze di prezzo al fine di ottenere un profitto. L'operazione è possibile se il ricavo che si ottiene supera i costi per il trasferimento del bene trattato da un mercato all'altro. L'intera operazione deve essere senza alcun rischio per l'operatore.
	\subsection{Currency Arbitrage}
		\item \textbf{Circular Arbitrage}: penso sia quello che interessa a noi, è un tipo di arbitraggio nel quale si sfruttano 3 o più valute in un ciclo in modo da ottenere alla fine di esso un guadagno sfruttando la disparità nei tassi di cambio.
		\item \textbf{Exchange Arbitrage}: cerca un guadagno attraverso le differenze di cambio tra diverse piattaforme di trading. Quindi non c'entra nulla con ciò di cui abbiamo bisogno.
		\item Ho trovato questa tesi "https://www.theseus.fi/handle/10024/795754" che parla in alcuni punti di cose simili alle nostre. In particolare accenna l'uso di alcuni API per il reperimento dei tassi di cambio. Per la ricerca di un profitto utilizza il DFS e analizza anche la complessità.
	\subsection{Currency Speculation}
	 	\item La differenza con quella di prima risiede nel fatto che (da come ho capito) si basa su previsioni di mercato e di conseguenza è più rischiosa. Le opportunità di arbitraggio teoricamente durano pochi istanti mentre nella speculazione, prevedendo l'andamento del mercato, si basa su istanti temporali maggiori generando un maggior rischio. Quindi potremo parlare pure di questo topic o fare una differenza tra i due. 
	\begin{itemize}
	\subsection{Possibili Algoritmi}: Dijkstra non possiamo usarlo se usiamo la scala logaritmica con il - davanti, in quanto non gestisce pesi negativi. Ho trovato che c'è Bellman-Ford e Floyd-Warshall. In breve Bellman-Ford parte da un singolo nodo (minor complessità), Floyd-Warshall analizza tutte le coppie del grafo (ha una complessità cubica) però potrebbe essere quello che ci interessa. Devo ancora leggere nello specifico le differenze però potrebbero essere due algoritmi da confrontare. 
Link x Floyd-Warshall: https://www.sciencedirect.com/science/article/pii/S002001901000027X 
Link x Bellman-Ford: https://www.mdpi.com/2227-7390/12/16/2590
Algoritmo ibrido Bellman-Ford+Dijkstra: https://www.sciencedirect.com/science/article/pii/S1570866717300011
