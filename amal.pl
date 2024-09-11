indian(amal).
indian(bimal).
leader(amal).
man(X) :- indian(X).

likes_or_dislikes_leader(X) :- man(X), (likes(X, Y) ; dislikes(X, Y)), leader(Y).

likes(bimal, amal).
dislikes(amal, amal).