import MySQLdb
from nltk.corpus import wordnet
db = MySQLdb.connect("localhost","root","nive","gre" )
cursor = db.cursor()
while(True) :
 s1 = raw_input("Enter a word and see the magic")
 synsets = wordnet.synsets( s1 )
 for synset in synsets:
  print "-" * 10
  print "Name:", synset.name
  print "Lexical Type:", synset.lexname
  print "Lemmas:", synset.lemma_names
  print "Definition:", synset.definition
  for example in synset.examples:
    print "Example:", example
 if cursor.execute("select count from learnt where learnt_word= %s ",(s1)) :
    result=cursor.fetchone()
    print  "You have viewed this word : %s" % result
    r = int(result[0])
    if(r > 5):
     print "Keep a check on ur memory revise daily .. This is a WARNING"

    r+=1
    cursor.execute("update learnt set count= %s where learnt_word= %s ",(r,s1) )
 else:
 	print "WOOOW NEW WORD GOOD GOING"
 	cursor.execute("Insert into learnt values (%s,%s)",(s1,1))
 	cursor.connection.commit(); 
 cursor.execute('select count(*) from learnt')
 result=cursor.fetchone()
 print "Number of words in your genius  mind  ----> %s " % result


