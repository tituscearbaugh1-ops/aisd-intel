import re
c = open('index.html', encoding='utf-8').read()
fix = '.body-wrap:has([class*="-view"].av) .content-area { display: none; }\n'
c2 = re.sub(r'(\.content-area\s*\{)', fix + r'\1', c, 1)
open('index.html', 'w', encoding='utf-8').write(c2)
print('done')
