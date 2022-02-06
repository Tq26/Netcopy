#file -- progressbar.py --

def progressbar(current, total, prefix='', suffix='', decimals=1, length=50, fill='|'):
    percent = "%.1f" % float((current / total) * 100)
    filledLength = int(current * length // total)
    bar = fill * filledLength + ' ' * (length - filledLength)
    print(f'\r{prefix} [ {bar} ] {percent}% {suffix}', end='\r')
    if current == total:
        print() 



