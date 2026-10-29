import re,sys
s=open(sys.argv[1],encoding='utf-8').read()
bad=[]
for ch,n in [('ي','Arabic YEH ي'),('ك','Arabic KAF ك'),('٠','Arabic-Indic digit')]:
    if ch in s: bad.append(n)
if re.search(r'letter-spacing',s): bad.append('letter-spacing used')
# Persian text segments with Latin digits outside tags/script
body=re.sub(r'<script.*?</script>|<style.*?</style>','',s,flags=re.S)
for t in re.findall(r'>([^<]+)<',body):
    if re.search(r'[؀-ۿ]',t) and re.search(r'[0-9]',t): bad.append('Latin digit in Persian: '+t)
    if re.search(r'[؀-ۿ]',t) and '?' in t: bad.append('Latin ? in Persian: '+t)
for m in re.findall(r'(?:می|نمی) ',body): bad.append('missing ZWNJ after می: '+m)
print('LINT OK' if not bad else '\n'.join(bad))
