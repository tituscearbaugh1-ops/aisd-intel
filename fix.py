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
.bonds-hdr { padding: 18px 24px 14px; background: rgb(14,11,8); border-bottom: 1px solid rgba(255,255,255,0.07); }
.bonds-title { font-size: 1.35rem; font-weight: 700; color: #fff; margin-bottom: 4px; }
.bonds-sub { font-size: 0.82rem; color: rgba(255,255,255,0.55); }
.bonds-overview { padding: 16px 24px 0; }
.bonds-callout { background: rgba(212,165,65,0.12); border-left: 3px solid #d4a541; border-radius: 6px; padding: 12px 16px; margin: 0 0 16px; font-size: 0.82rem; color: rgba(255,255,255,0.85); line-height: 1.5; }
.bonds-callout strong { color: #d4a541; }
"""

stats_html = """<div class="bonds-overview">
  <div class="bv-summary-grid">
      <div class="bv-sum-card"><div class="bv-sum-n">$1.54B</div><div class="bv-sum-l">Voter-Approved</div><div class="bv-sum-sub">2013 + 2017 bonds passed</div></div>
          <div class="bv-sum-card"><div class="bv-sum-n">$2.44B</div><div class="bv-sum-l">Rejected by Voters</div><div class="bv-sum-sub">2022 Prop A — 53% NO</div></div>
              <div class="bv-sum-card"><div class="bv-sum-n">2 of 3</div><div class="bv-sum-l">Bonds Passed</div><div class="bv-sum-sub">2013 &amp; 2017 approved</div></div>
                  <div class="bv-sum-card"><div class="bv-sum-n">~$160M</div><div class="bv-sum-l">Unaccounted (2017)</div><div class="bv-sum-sub">Status unclear / unverified</div></div>
                      <div class="bv-sum-card"><div class="bv-sum-n">130+</div><div class="bv-sum-l">Projects (2017 Bond)</div><div class="bv-sum-sub">Listed in CIP reports</div></div>
                          <div class="bv-sum-card"><div class="bv-sum-n">$95M+</div><div class="bv-sum-l">Spent on Closing Schools</div><div class="bv-sum-sub">8 schools closing 2026–27</div></div>
                            </div>
                              <div class="bonds-callout"><strong>&#9888;&#65039; Accountability Gap:</strong> AISD spent over <strong>$95M+</strong> in bond funds on schools now being closed in 2026–27. Voters approved these bonds for facility improvements — not for buildings being shuttered within a decade. District is attempting to terminate <strong>$70M+</strong> in contracts.</div>
                              </div>
                              """

c2 = c.replace('</style>', css + '</style>', 1)
c2 = c2.replace('<div class="bonds-scroll">', stats_html + '<div class="bonds-scroll">', 1)
open('index.html', 'w', encoding='utf-8').write(c2)
replaced = (c2 != c)
print('done' if replaced else 'WARNING: no replacement found')
