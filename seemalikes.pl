like(seema,rayan).
like(rayan,britney).
like(britney,rayan).
like(danny,jose).
meeting(X,Y):-like(X,Y),like(Y,X).
friendship(X,Y):-like(X,Y);like(Y,X).
