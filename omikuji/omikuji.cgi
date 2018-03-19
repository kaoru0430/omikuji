#!/usr/bin/perl

use CGI;
$q = new CGI;
if($q->param('namae')){$namae=$q->param('namae');}

# CGIヘッダーの出力
print "Content-type: text/html\n\n";

# HTMLの出力
print "<!DOCTYPE html>\n";
print "<html>\n";
print "<head><title>おみくじTOP</title>\n";
print "<meta charset=\"utf-8\">\n";
print "<link rel=\"stylesheet\" type=\"text/css\" href=\"omikuji.css\">\n";
print "<script src=\"http://ajax.googleapis.com/ajax/libs/jquery/1.8.3/jquery.min.js\">\n";
print "</script>\n";
print "</head><body>\n";
print "<div class=\"content_wrapper\">\n";
print "<div class=\"omikuji_top\" style=\"display:block;\">\n";
print "<h1>名前を入れて占ってみよう！</h1>\n";
print "<img class=\"gazou\" src=\"おみくじ.png\">\n";
print "<form method=\"post\" action=\"./omikuji_kekka.cgi\">\n";
print "<div class=\"nyuryoku\">おなまえ: <input type=\"text\" name=\"namae\" size=\"10\">\n";
print "</div><div class=\"btn\">\n";
print "<input type=\"submit\" class=\"sbt\" value=\"おみくじを引く\">\n";
print "</div>\n";
print "</div>\n";
print "</div>\n";
print "</form>\n";
print "</body></html>\n";

exit 0;
