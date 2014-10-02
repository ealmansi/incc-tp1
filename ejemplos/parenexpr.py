#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random;
import decimal;

# def _gen(index, word, current_depth, word_depth, target_len, target_depth):

#   while index < len(word) and word[index] != 'x':
#     current_depth = current_depth + (1 if word[index] in ls else -1)
#     word_depth = max(current_depth, word_depth)
#     index = index + 1

#   if index == len(word):
#     if len(word) == target_len and word_depth == target_depth:
#       print("".join(word))

#   else:
#     _gen(index, word[:index] + word[index + 1:],
#       current_depth, word_depth, target_len, target_depth)
#     if index + 2 <= target_len:
#       for l, r in pairs:
#         _gen(index, word[:index] + [l, 'x', r, 'x'] + word[index + 1:],
#           current_depth, word_depth, target_len, target_depth)

# def gen(target_len, target_depth):
#   _gen(0, ['x'], 0, 0, target_len, target_depth)

# def main():
#   target_len, target_depth = 10, 3
#   print('target_len = {l}, target_depth = {d}'.format(l=target_len, d=target_depth))
#   gen(target_len, target_depth)

def gen_rand_word(lnth, max_dpth, pairs):
  if lnth == 0 or max_dpth == 0:
    return '', 0
  else:
    i = random.randint(0, min(max_dpth - 1, lnth - 1))
    l, r = random.choice(pairs)
    w1, d1 = gen_rand_word(i, max_dpth - 1, pairs)
    w2, d2 = gen_rand_word(lnth - 1 - i, max_dpth, pairs)
    return l + w1 + r + w2, max(d1 + 1, d2)

def main():
  secu = []
  count = 0
  ls = ['(', '[', '{', '<', 'x', '+'][:3]
  rs = [')', ']', '}', '>', 'y', '-'][:3]
  pairs = list(zip(ls, rs))
  print pairs
  max_dpth = 1
  for lnth in [3,6,12]:
    print("bien")    
    for max_dpth in range(1,4):
      	while count < 10:
      		word, depth = gen_rand_word(lnth, max_dpth, pairs)
      		if depth == max_dpth:
	      		count+=1
      	  		secu.append("'"+word+"',")

      	  		# flips
      	  		
      	  		word = list(word)
		     	for _ in range(2):
		        	i = random.randint(0, len(word) - 1)
		        	c = random.choice(ls + rs)
		        	while word[i] == c:
		          		c = random.choice(ls + rs)
		        	word[i] = c
		      		# print "la queda"
		      	word = "".join(word)
		      	secu.append("'"+word+"',")

      	count = 0
    print("mal")
    for flips in range(1, 3):
      word, _ = gen_rand_word(lnth, max_dpth, pairs)
      word = list(word)
      for _ in range(flips):
        i = random.randint(0, len(word) - 1)
        c = random.choice(ls + rs)
        while word[i] == c:
          c = random.choice(ls + rs)
        word[i] = c
      word = "".join(word)
      print(word, "flips:", flips)
    random.shuffle(secu)
    for x in secu:
    	print x

if __name__ == '__main__':
  main()