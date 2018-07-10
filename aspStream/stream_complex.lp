{ assign(J,P,WT) : J=1..jobs } <= 1 :- window(elem(P,job(M,D)),WT), simple=0.
#maximize{ 1@-WT,P : assign(J,P,WT) }.

:- occupies(_,M,_,T), window(occupied(M,T),0).
:- assign(J,P,WT), window(elem(P,_),WT), window(done(WT,P)).

watom(occupied(M,T)) :- M=1..machines, T=1..horizon.
watom(done(WT,P)) :- WT=1-window_size..-1, P=1..length.

