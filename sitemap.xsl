<?xml version="1.0" encoding="UTF-8"?>
<!-- Renders sitemap.xml as a readable table in browsers. Crawlers ignore it. -->
<xsl:stylesheet version="1.0"
                xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
                xmlns:sm="http://www.sitemaps.org/schemas/sitemap/0.9"
                xmlns:xhtml="http://www.w3.org/1999/xhtml"
                exclude-result-prefixes="sm xhtml">
  <xsl:output method="html" encoding="UTF-8" indent="yes" doctype-system="about:legacy-compat"/>

  <xsl:template match="/">
    <html lang="en">
      <head>
        <meta charset="UTF-8"/>
        <meta name="viewport" content="width=device-width, initial-scale=1"/>
        <meta name="robots" content="noindex"/>
        <title>Fakkerni sitemap</title>
        <style>
          :root {
            --bg: #f7f5ff; --surface: #ffffff; --ink: #1e1b4b; --ink2: #4a4770;
            --ink3: #67648c; --line: #e4e1f5; --primary: #1e1b4b; --mint-ink: #0f7a60;
            color-scheme: light dark;
          }
          @media (prefers-color-scheme: dark) {
            :root {
              --bg: #0d0c1f; --surface: #18172f; --ink: #f7f5ff; --ink2: #c9c6ea;
              --ink3: #9a97c2; --line: #2e2a5e; --primary: #b9b4ff; --mint-ink: #5ed3b4;
            }
          }
          * { box-sizing: border-box; }
          body {
            margin: 0; background: var(--bg); color: var(--ink);
            font: 15px/1.5 system-ui, -apple-system, "Segoe UI", sans-serif;
          }
          main { max-width: 960px; margin: 0 auto; padding: 40px 16px; }
          h1 { margin: 0 0 4px; font-size: 28px; }
          p { margin: 0 0 24px; color: var(--ink2); }
          a { color: var(--primary); text-decoration: none; }
          a:hover { text-decoration: underline; }
          .card {
            background: var(--surface); border: 1px solid var(--line);
            border-radius: 16px; overflow-x: auto;
          }
          table { width: 100%; border-collapse: collapse; }
          th, td { padding: 12px 16px; text-align: left; vertical-align: top; }
          th {
            font-size: 12px; text-transform: uppercase; letter-spacing: .05em;
            color: var(--ink3); border-bottom: 1px solid var(--line);
          }
          tr + tr td { border-top: 1px solid var(--line); }
          td.url a { font-weight: 600; word-break: break-all; }
          .alts { margin-top: 4px; display: flex; gap: 6px; flex-wrap: wrap; }
          .alts a {
            font-size: 12px; padding: 1px 8px; border-radius: 999px;
            border: 1px solid var(--line); color: var(--mint-ink);
          }
          td.num { white-space: nowrap; color: var(--ink2); font-variant-numeric: tabular-nums; }
          @media (max-width: 640px) {
            thead { display: none; }
            table, tbody, tr, td { display: block; }
            tr { padding: 12px 16px; }
            tr + tr { border-top: 1px solid var(--line); }
            tr + tr td { border-top: 0; }
            td { padding: 0; }
            td.num { display: inline; font-size: 13px; }
            td.num + td.num::before { content: " · "; }
            td.url { margin-bottom: 6px; }
          }
        </style>
      </head>
      <body>
        <main>
          <h1>Sitemap</h1>
          <p>
            <xsl:value-of select="count(sm:urlset/sm:url)"/> pages on
            <a href="https://amrcs92.github.io/fakkerni-site/">Fakkerni</a>.
            This file helps search engines find the site's pages.
          </p>
          <div class="card">
            <table>
              <thead>
                <tr>
                  <th>URL</th>
                  <th>Last modified</th>
                  <th>Change frequency</th>
                  <th>Priority</th>
                </tr>
              </thead>
              <tbody>
                <xsl:for-each select="sm:urlset/sm:url">
                  <tr>
                    <td class="url">
                      <a href="{sm:loc}"><xsl:value-of select="sm:loc"/></a>
                      <xsl:if test="xhtml:link">
                        <div class="alts">
                          <xsl:for-each select="xhtml:link[@hreflang != 'x-default']">
                            <a href="{@href}" hreflang="{@hreflang}"><xsl:value-of select="@hreflang"/></a>
                          </xsl:for-each>
                        </div>
                      </xsl:if>
                    </td>
                    <td class="num"><xsl:value-of select="sm:lastmod"/></td>
                    <td class="num"><xsl:value-of select="sm:changefreq"/></td>
                    <td class="num"><xsl:value-of select="sm:priority"/></td>
                  </tr>
                </xsl:for-each>
              </tbody>
            </table>
          </div>
        </main>
      </body>
    </html>
  </xsl:template>
</xsl:stylesheet>
