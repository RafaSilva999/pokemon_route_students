:-ensure_loaded("pokemon_list.pl").
:-ensure_loaded("pokemon_info_attacks.pl").
:-ensure_loaded("pokemon_route.pl").

player_starts(0,0).

% TO DO~
%matrix_rows(M, R) :-
%    length(M, R).
%matrix_cols(M, C) :-
%    M = [Row|_],
%    length(Row, C).

%inside_limits(X, Y, Rows, Cols) :-
%    X >= 0, X =< Rows - 1,
%    Y >= 0, Y =< Cols - 1.

inside_limits(X,Y) :-
    X >= 0, X =< 4,
    Y >= 0, Y =< 4.

%isneighbor(X,Y,X1,Y1) :-
%    (X1 is X + 1,).
%isneighbor(X,Y,X1,Y1) :-
%    (X1 is X - 1).
%isneighbor(X,Y,X1,Y1) :-
%    (Y1 is Y + 1).
%isneighbor(X,Y,X1,Y1) :-
%    (Y1 is Y - 1).


isneighbor(X,Y,X1,Y1) :-
    (X1 is X + 1, Y1 is Y).
isneighbor(X,Y,X1,Y1) :-
    (X1 is X - 1, Y1 is Y).
isneighbor(X,Y,X1,Y1) :-
    (X1 is X, Y1 is Y + 1).
isneighbor(X,Y,X1,Y1) :-
    (X1 is X, Y1 is Y - 1).

next_rooms(X, Y, Rooms) :-
    route(M),
    findall(
        [Id, Name, Level, NX, NY, Types],
        (
            isneighbor(X, Y, NX, NY),
            inside_limits(NX, NY),
            elemento_indice(NX, M, Linha),
            elemento_indice(NY, Linha, (Id, Level)),
            Id \= 0,
            pokemon(Id, Name, Types)
        ),
        Rooms
    ).

elemento_indice(0, [H|_], H).
elemento_indice(N, [_|T], Elem) :-
        N > 0,
        N1 is N - 1,
        elemento_indice(N1, T, Elem).
