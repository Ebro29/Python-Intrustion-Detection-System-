import sys
import os
import re

def main():
   filepath2 = 'C:/Users/ebrah/Desktop/signatures.txt'
   filepath = "C:/Users/ebrah/Desktop/iptables.log"

   if not os.path.isfile(filepath):
       print("File path {} does not exist. Exiting...".format(filepath))
       sys.exit()
  
   bag_of_words = {}
   with open(filepath) as fp:
       cnt = 0
       for line in fp:
           #print("line {} contents {}".format(cnt, line))
           record_word_cnt(line.strip().split(' '), bag_of_words)
           cnt += 1
   sorted_words = order_bag_of_words(bag_of_words, desc=True)
   print("Most frequent features {}".format(sorted_words[:16]))
  
def order_bag_of_words(bag_of_words, desc=False):
   words = [(word, cnt) for word, cnt in bag_of_words.items()]
   return sorted(words, key=lambda x: x[1], reverse=desc)

def record_word_cnt(words, bag_of_words):
   for word in words:
       if word != '':
           if word.lower() in bag_of_words:
               bag_of_words[word.lower()] += 1
           else:
               bag_of_words[word.lower()] = 1

def scan_detect():
    with open(filepath) as fp:
        p = re.compile('[a-z]+')
        signarure1 = p.match("PROTO=ICMP")
        signarure2 = p.match("LEN=92")
        signarure3 = p.match("SPT=1434", "PROTO=UDP")
        signarure4 = p.match("SPT=1026", "PROTO=UDP")
        signarure5 = p.match("SPT=25", "PROTO=TCP")
        signarure6 = p.match("DPT=1433")
        signarure7 = p.match("LEN=55808")
        if signature1:
            print('Signature found! ICMP Ping!')
            #print("Most frequent features {}".format(sorted_words[:16])) these are placeholders to display the statistics
        elif signature2:
            print ('Signature found! Nachi worm!')
            #print("Most frequent features {}".format(sorted_words[:16]))
        elif signature3:
            print('Signature found! Slammer communication attempt!')
            #print("Most frequent features {}".format(sorted_words[:16]))
        elif signature4:
            print('Signature found! Windows popup spam!')
        elif signature 5:
            print('Signature found! Slammer communication attempt!')
        elif signature6:
            print('Signature found! Windows popup spam!')
        elif signature 7:
             print('Signature found! Slammer communication attempt!')
        


if __name__ == '__main__':
   main()