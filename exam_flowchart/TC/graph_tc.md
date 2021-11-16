``` mermaid
graph TD;
	NuovoPazienteInterno[Arriva un nuovo paziente interno]-->Agenda
	Agenda[C'è in agenda?]--sì-->AgendaSì[Ha la cartella clinica?];
	Agenda[C'è in agenda?]--no-->AgendaNo[Non è un nostro paziente];
	AgendaNo --> ChiamareReparto[Chiamare il reparto di provenienza e informarsi]
	ChiamareReparto --forniscono spiegazioni ragionevoli--> Esame
	ChiamareReparto --spiegazioni non adeguate--> SpiegazioniNO[Torna in reparto]
	AgendaSì --> Esame[Che esame deve fare?] --> EsameBasale[TC Basale]
	Esame --> EsameMdC[TC con MdC]
	EsameMdC --> Consenso[C'è il consenso informato firmato?]
	Consenso --> ConsensoSì[Ha allergie?]
	Consenso --> SpiegazioniNO
```
