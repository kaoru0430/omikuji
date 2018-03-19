#!/usr/bin/perl

use CGI;
$q = new CGI;
if($q->param('namae')){$namae=$q->param('namae');}

# CGIヘッダーの出力
print "Content-type: text/html\n\n";

# HTMLの出力
print "<!DOCTYPE html>\n";
print "<html><head>\n";
print "<title>おみくじ結果</title>\n";
print "<meta charset=\"utf-8\">\n";



if($namae){

print "<link rel=\"stylesheet\" type=\"text/css\" href=\"omikuji2.css\">\n";
print "</head><body>\n";

@kuji = ('大吉', '吉','中吉','小吉','末吉', '凶');
@food = ('オムライス', 'オニオングラタンスープ', 'ペペロンチーノ', 'ジェノベーゼ',
         'ローストビーフ丼', '鮭のムニエル', '温玉うどん', '家系らーめん', '炒飯',
         'おでん缶');
@message = (
'おめでとうございます。最高な1日になるでしょう。',
'なにか良いことがありそうです。',
'きっと小さな幸せが見つかります。',
'穏やかな1日になるでしょう',
'ちょっと注意が必要。まわりをよく見て');


# おみくじを引く
$role = int(rand 5);
$role2 = int(rand 10);

if($kuji[$role] eq "大吉"){$i = int(rand 3) + 6; $j = int(rand 3) + 6;
$k = int(rand 3) + 6;}
elsif($kuji[$role] eq "吉"){$i = int(rand 3) + 5; $j = int(rand 3) + 5;
$k = int(rand 3) + 5;}
elsif($kuji[$role] eq "中吉"){$i = int(rand 3) + 4; $j = int(rand 3) + 4;
$k = int(rand 3) + 4;}
elsif($kuji[$role] eq "小吉"){$i = int(rand 3) + 3; $j = int(rand 3) + 3;
$k = int(rand 3) + 3;}
elsif($kuji[$role] eq "末吉"){$i = int(rand 3) + 2; $j = int(rand 3) + 2;
$k = int(rand 3) + 2;}
elsif($kuji[$role] eq "凶"){$i = int(rand 2) + 1; $j = int(rand 2) + 1;
$k = int(rand 2) + 1;}


print "<div class=\"content_wrapper\">\n";
print "<h1>今日の<strong>$namae</strong>さんの運勢は……</h1>\n";
print "<img class=\"gazou\" src=\"$kuji[$role].png\">\n";
print "<h2>" . $message[$role] . "</h2>\n";

print "<div class=\"star\">\n";
print "<h3>全体運：\n";
while($i > 0) {  print "★"; $i--; }
print "</h3>";
print "<h3>恋愛運：\n";
while($j > 0) { print "★"; $j--; }
print "</h3>";
print "<h3>金運：\n";
while($k > 0) { print "★"; $k--; }
print "</h3></div>\n";

print "<p =\"lfood\">ラッキーフード : " . $food[$role2] . "</p>\n";
print "<img class=\"food\" src=\"foods/" . $food[$role2] . ".png\">\n";
print "<a class=\"lbt\" href=\"http://gms.gdl.jp/~kaoru0430/cgi-bin/omikuji/omikuji.cgi\">";
print "もう一度占う</a>\n";
print "</div>\n";
print "</body></html>\n";

} else {

  print "<!DOCTYPE html>\n";
  print "<html>\n";
  print "<head><title>占い！</title>\n";
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
  print "<p>※名前を入れてください</p>\n";
  print "<input type=\"submit\" class=\"sbt\" value=\"おみくじを引く\">\n";
  print "</div>\n";
  print "</div>\n";
  print "</div>\n";
  print "</form>\n";
  print "</body></html>\n";

}



exit 0;
