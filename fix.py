c = open('index.html', encoding='utf-8').read()
css = """
.body-wrap > [class*='-view'].av { flex: 1 1 0% !important; min-width: 0; }
.body-wrap:has(.campus-view.av) .content-area,
.body-wrap:has(.contracts-view.av) .content-area,
.body-wrap:has(.sources-view.av) .content-area,
.body-wrap:has(.budget-view.av) .content-area,
.body-wrap:has(.audits-view.av) .content-area,
.body-wrap:has(.bonds-view.av) .content-area,
.body-wrap:has(.teaintel-view.av) .content-area { display: none !important; }
"""
c2 = c.replace('</style>', css + '</style>', 1)
open('index.html', 'w', encoding='utf-8').write(c2)
print('done' if c2 != c else 'WARNING: no </style> found')
