import copy
import random
import sys

genes = 20000
sets = 10
sources = 3
random.seed(1)
dropout = 0.05

data = []
for j in range(sources):
	vals = {}
	for i in range(genes):
		vals[f'gene-{i}'] = random.random()
	data.append(vals)

tests = []
for i in range(sets):
	sn = random.randint(0, sources-1)
	src = data[sn]
	print(i, sn)
	cpy = copy.copy(src)
	deletes = []
	for gene in cpy:
		if random.random() < dropout: deletes.append(gene)
	for gene in deletes: del cpy[gene]
	total = 0
	for gene, val in cpy.items(): total += val
	for gene in cpy: cpy[gene] /= total
	tests.append(cpy)

for i, t in enumerate(tests):
	with open(f'fake-{i}.tsv', 'w') as fp:
		for gene, val in t.items():
			print(gene, val, sep='\t', file=fp)

# 2 1 1 0 1 1 0 0 0 0
