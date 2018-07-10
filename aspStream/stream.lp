{ assign(J,P,WT) : J=1..jobs } = 1 :- window(elem(P,job(M,D)),WT),
                                      simple=1.
:- assign(J,P1,WT1), assign(J,P2,WT2), (P1,WT1) < (P2,WT2).
job(J,M,D) :-         assign(J,P,WT), window(elem(P,job(M,D)),WT).

watom(elem(P,job(M,D))) :-
  P=1..length, M=1..machines, D=1..horizon.

