import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

    # Fix: when a view panel is active (.av), content-area steals half the flex space.
    # This rule hides content-area whenever any *-view sibling is active.
    fix_css = '.body-wrap:has([class*="-view"].av) .content-area { display: none; }\n'

    fixed = re.sub(r'(\.content-area\s*\{)', fix_css + r'\1', content, count=1)

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(fixed)

        if fixed != content:
            print('Layout fix applied successfully.')
            else:
                print('WARNING: .content-area pattern not found - no change made.')
                
