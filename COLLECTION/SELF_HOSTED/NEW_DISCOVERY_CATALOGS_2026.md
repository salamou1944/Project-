# New Discovery Catalogs — 2026-09-25

Status: DISCOVERY_CAPTURED

Fresh web sweep found additional catalogs:
- https://selfhosttools.com/ — 225 curated tools across 17 categories; updated/verified 2026. citeturn0search2
- https://awesomeselfhosted.app/ — 303 apps, with repository health, license and installation metadata; directory says repository data syncs daily. citeturn0search15
- https://github.com/awesome-selfhosted/awesome-selfhosted — canonical broad Free Software self-hosting discovery source; current repository shows 7,114 commits. citeturn0search14
- https://github.com/SolvoHQ/awesome-self-host-saas-alternatives — 100 SaaS mappings / 294 alternatives according to current README. citeturn0search3
- https://github.com/open-saas-directory/awesome-saas-directory — continuously updated open-source SaaS/self-hosted catalog. citeturn0search12

New operational rule:
Discovery catalogs are now treated as a source graph. We should preserve catalog URLs first, then recursively inspect candidates from each category; catalog claims do not become production evidence.
