#!/usr/bin/python
import pytholog as pl
import pprint

# variance,skewness,curtosis,entropy,class
# "Authentic"  "Counterfeit"
# -0.89569,3.0025,-3.6067,-3.4457,1
# 3.4769,-0.15314,2.53,2.4495,0

kb_rules = [
	"path(authentic1, Result) :- v(V), s(S),       Result is V <= 0.315 and S <=  7.565 and S <=  5.865",
	"path(authentic2, Result) :- v(V), s(S),       Result is V <= 0.315 and S >   7.565 and V <= -4.726",
	"path(authentic3, Result) :- v(V), c(C), s(S), Result is V >  0.315 and C <= -4.394 and S <=  7.192",
	"path(authentic4, Result) :- v(V), c(C),       Result is V >  0.315 and C >  -4.394 and V <=  1.587"
	]

# Positive test
print("\nPositive test")
bank_kb = pl.KnowledgeBase("banknotes")
positive_test = kb_rules + ["v( -0.89569)","s(3.0025)","c(2.53)"]
# pprint.pprint(positive_test)
bank_kb(positive_test)
answer = bank_kb.query(pl.Expr("path(Class, Result)"))
pprint.pprint(answer)

# Negative test
print("\nNegative test")
bank_kb = pl.KnowledgeBase("banknotes")
negative_test = kb_rules + ["v(3.4769)","s(-0.15314)","c(2.53)"]
# pprint.pprint(negative_test)
bank_kb(negative_test)
answer = bank_kb.query(pl.Expr("path(Class, Result)"))
pprint.pprint(answer)
