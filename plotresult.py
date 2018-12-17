import matplotlib.pyplot as p
from scipy.stats import pearsonr

f=open("results.list")
lengths=[]
fnums=[]
errors=[]
for line in f:
    parts=line.split(',')
    lengths.append(int(parts[1]))
    fnums.append(float(parts[2]))
    errors.append(abs(float(parts[3])-float(parts[4]))/int(parts[1]))

p.title('Relative Error VS. Protein Length')
p.ylabel('Relative Error')
p.xlabel('Protein Length(aa)')
p.scatter(lengths,errors)
print(pearsonr(lengths,errors)[0])
p.show()

p.title('Relative Error VS. Fiedler Number')
p.ylabel('Relative Error')
p.xlabel('Fiedler Number')
p.scatter(fnums,errors)
print(pearsonr(fnums,errors)[0])
p.show()

p.title('Relative Error VS. Normalized Fiedler Number')
p.ylabel('Relative Error')
p.xlabel('Normalized Fiedler Number')
p.scatter([fnums[i]/lengths[i] for i in range(len(lengths))],errors)
print(pearsonr([fnums[i]/lengths[i] for i in range(len(lengths))],errors)[0])
p.show()
