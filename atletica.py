$ pwd
/home/ccuser/workspace/athletica
$ ls
badminton.txt   cricket.txt    football.txt  gymnastics.txt  lacrosse.txt  swimming.txt
basketball.txt  equipment.txt  games.txt     hockey.txt      roster.txt    tennis.txt
$ ls -la
total 56
drwxr-xr-x 2 ccuser ccuser  259 Jul 12 00:20 .
drwxrwxr-x 1 ccuser ccuser   23 Jul 12 00:20 ..
-rw-r--r-- 1 ccuser ccuser  102 Jul 12 00:20 badminton.txt
-rw-r--r-- 1 ccuser ccuser   97 Jul 12 00:20 basketball.txt
-rw-r--r-- 1 ccuser ccuser  161 Jul 12 00:20 cricket.txt
-rw-r--r-- 1 ccuser ccuser 6148 Mar  5  2016 .DS_Store
-rw-r--r-- 1 ccuser ccuser  304 Jul 12 00:20 equipment.txt
-rw-r--r-- 1 ccuser ccuser  117 Jul 12 00:20 football.txt
-rw-r--r-- 1 ccuser ccuser  393 Jul 12 00:20 games.txt
-rw-r--r-- 1 ccuser ccuser  130 Jul 12 00:20 gymnastics.txt
-rw-r--r-- 1 ccuser ccuser  163 Jul 12 00:20 hockey.txt
-rw-r--r-- 1 ccuser ccuser  159 Jul 12 00:20 lacrosse.txt
-rw-r--r-- 1 ccuser ccuser  605 Jul 12 00:20 roster.txt
-rw-r--r-- 1 ccuser ccuser   69 Jul 12 00:20 swimming.txt
-rw-r--r-- 1 ccuser ccuser  160 Jul 12 00:20 tennis.txt
$ cat basketball.txt
Basketball is a sport played by two teams of five players on a rectangular court. Src: Wikipedia
$ cat hockey.txt
Hockey is a family of sports in which two teams play against each other by trying to maneuver a ball into the opponent's goal using a hockey stick. Src: Wikipedia
$ cat basketball.txt > hockey.txt
$ cat hockey.txt
Basketball is a sport played by two teams of five players on a rectangular court. Src: Wikipedia
$ cat lacrosse.txt
Lacrosse is a contact team sport played between two teams using a small rubber ball and a long-handled stick called a crosse or lacrosse stick. Src: Wikipedia
$ 
$ cat lacrosse.txt >> teniis.txt
$ cat tennis.txt
Tennis is a racket sport that can be played individually against a single opponent (singles) or between two teams of two players each (doubles). Src: Wikipedia
$ cat < gymnastics.txt
Gymnastics is a sport involving the performance of exercises requiring strength, flexibility, balance and control. Src: Wikipedia
$ cat lacrolsc
cat: lacrolsc: No such file or directory
$ cat lacrosee.text | wc
cat: lacrosee.text: No such file or directory
      0       0       0
$ cat equipment.txt
baseball
shuttlecock
shuttlecock
helmet
football
cleats
cleats
cleats
tennis ball
baseball bat
lacrosse stick
hockey stick
hockey stick
hockey stick
tennis racket
cricket bat
cricket bat
cricket bat
goggles
googles
swimming cap
lacrosse ball
hockey puck
sneakers
sneakers
skates
skates
skates
shinguards
$ sort equipment.txt
baseball
baseball bat
cleats
cleats
cleats
cricket bat
cricket bat
cricket bat
football
goggles
googles
helmet
hockey puck
hockey stick
hockey stick
hockey stick
lacrosse ball
lacrosse stick
shinguards
shuttlecock
shuttlecock
skates
skates
skates
sneakers
sneakers
swimming cap
tennis ball
tennis racket
$ sort equipment.txt | uniq
baseball
baseball bat
cleats
cricket bat
football
goggles
googles
helmet
hockey puck
hockey stick
lacrosse ball
lacrosse stick
shinguards
shuttlecock
skates
sneakers
swimming cap
tennis ball
tennis racket
$ grep Japan roster.txt
Yuki Hayashi, Swimming: Japan
Misako Sato, Gymnastics: Japan
Takumi Fujiwara, Basketball: Japan
Toshi Ogawa, Badminton: Japan
$ grep -R player . 
./basketball.txt:Basketball is a sport played by two teams of five players on a rectangular court. Src: Wikipedia
./cricket.txt:Cricket is a bat-and-ball game played between two teams of 11 players each on a field at the centre of which is a rectangular 22-yard-long pitch. Src: Wikipedia
./hockey.txt:Basketball is a sport played by two teams of five players on a rectangular court. Src: Wikipedia
./tennis.txt:Tennis is a racket sport that can be played individually against a single opponent (singles) or between two teams of two players each (doubles). Src: Wikipedia
$ sed 's/loss/win/g' games.txt
Australia vs United Kingdom
Australia: win

United States vs South Africa
United States: win

Mexico vs Colombia
Colombia: win

Brazil vs Argentina
Brazil: win

Kenya vs Ghana
Kenya: win

Jordan vs Morocco
Morocco: win

Malaysia vs Singapore
Singapore: win

India vs China
India: win

Pakistan vs Uzbekistan
Uzbekistan: win

Greece vs Turkey
Greece: win

France vs Spain
France: win$ 