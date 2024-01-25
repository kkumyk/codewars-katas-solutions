
/*

\s matches ASCII whitespace characters ([ \t\n\x0B\f\r]).

* will match zero or more of the previous items. They function
just like plus signs, except they allow you to match ZERO (or
more) of the previous items, whereas plus signs require at least
one match. 
*/

String.prototype.whitespace = function () {
    return /^\s$/g.test(this);
}