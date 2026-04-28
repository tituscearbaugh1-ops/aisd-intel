c = open('index.html', encoding='utf-8').read()
css = '\n.body-wrap:has([class*="-view"].av) .content-area { display: none; }\n'
c2 = c.replace('</style>', css + '</style>', 1)
open('index.html', 'w', encoding='utf-8').write(c2)
print('done - css injected' if c2 != c else 'WARNING: no </style> found')
