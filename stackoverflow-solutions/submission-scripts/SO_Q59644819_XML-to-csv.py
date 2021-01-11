
"""
Purpose: Stackoverflow - XML to CSV using
Date created: 2020-01-08

URI: https://stackoverflow.com/questions/59644819/how-to-write-csv-from-xml-response-in-python/59645553#59645553

Contributor(s):
    Mark M.
"""

import re
import urllib.request as urequest

url = r'http://www.culturaitalia.it/oaiProviderCI/OAIHandler?verb=ListRecords&metadataPrefix=pico&set=collezione_pansa_villa_frigerj'

with urequest.urlopen(url) as r:
    raw_data = r.read().decode('utf-8')



sample = """
<record><header><identifier>oai:culturaitalia.it:oai:culturaitalia.it:museiditalia-work_46880</identifier><datestamp>2018-08-29T17:56:41Z</datestamp><setSpec>museiditalia_opere</setSpec><setSpec>opere_museid</setSpec><setSpec>Beni_culturali</setSpec><setSpec>collezione_pansa_villa_frigerj</setSpec></header><metadata>
<pico:record xmlns:pico="http://purl.org/pico/1.0/" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:iccd="http://purl.org/pico/iccd/2.00/" xmlns:oad="http://purl.org/pico/iccd/2.00/oa-d-n/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:smi="http://purl.org/pico/iccd/2.00/s-mi/" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:bdm="http://purl.org/pico/iccd/2.00/bdm/" xmlns:mets="http://www.loc.gov/METS/" xmlns:f="http://purl.org/pico/iccd/2.00/f/" xmlns:vra="http://www.vraweb.org/vracore4.htm" xmlns:iccd3="http://purl.org/pico/iccd/3.00/" xmlns:mix="http://www.loc.gov/mix/v20" xmlns:nu="http://purl.org/pico/iccd/3.00/nu/" xmlns:premis="info:lc/xmlns/premis-v2" xsi:schemaLocation="http://purl.org/pico/1.0/               http://www.culturaitalia.it/pico/schemas/1.0/pico.xsd                     http://purl.org/pico/iccd/2.00/         http://www.culturaitalia.it/pico/schemas/iccd/2.00/iccd.xsd                     http://purl.org/pico/iccd/2.00/oa-d-n/  http://www.culturaitalia.it/pico/schemas/iccd/2.00/oa-d-n.xsd                     http://purl.org/pico/iccd/2.00/s-mi/    http://www.culturaitalia.it/pico/schemas/iccd/2.00/s-mi.xsd                     http://purl.org/pico/iccd/2.00/bdm/     http://www.culturaitalia.it/pico/schemas/iccd/2.00/bdm.xsd                     http://purl.org/pico/iccd/2.00/f/       http://www.culturaitalia.it/pico/schemas/iccd/2.00/f.xsd                     http://purl.org/pico/iccd/3.00/         http://www.culturaitalia.it/pico/schemas/iccd/3.00/iccd.xsd                     http://purl.org/pico/iccd/3.00/nu/      http://www.culturaitalia.it/pico/schemas/iccd/3.00/nu.xsd">
  <dc:identifier>work_46880</dc:identifier>
  <dc:title>BROCCHETTA MINIATURISTICA</dc:title>
  <dc:subject xsi:type="pico:Thesaurus">http://culturaitalia.it/pico/thesaurus/4.1#reperti_archeologici</dc:subject>
  <dc:description xml:lang="it">BROCCHETTA MONOANSATA. ANSA A DOPPIO BASTONCELLO ARCUATO CHE SI SALDA SULCOLLO AL DI SOTTO DEL LABBRO ESPANSO. CORPO BACCELLATO CON INCISIONE AD XSOTTO L'ANSA, BASSO PIEDE TRONCOCONICO. VERNICE MALCOTTA CON AVVAMPATURESUL PIEDE.</dc:description>
  <dcterms:spatial>Museo Archeologico Nazionale d'Abruzzo, Villa Frigerj, CHIETI (CH) - ITALIA - sala collezione Pansa - vetrina 1, inv. 3130</dcterms:spatial>
  <dcterms:spatial xsi:type="pico:ISTAT">name=CHIETI; year=2001; code=069022</dcterms:spatial>
  <dcterms:created>SEC. III A.C.</dcterms:created>
  <dcterms:created xsi:type="dcterms:Period">start=299; end=250</dcterms:created>
  <dc:type xsi:type="mdi:Type">Opere</dc:type>
  <dc:type xml:lang="it">BROCCHETTA MINIATURISTICA</dc:type>
  <dc:type xsi:type="dcterms:DCMIType">PhysicalObject</dc:type>
  <dcterms:isPartOf xsi:type="dcterms:URI">oai:culturaitalia.it:museiditalia-coll_445</dcterms:isPartOf>
  <dc:rights xml:lang="it"/>
  <dcterms:rightsHolder xml:lang="it">PROPRIETA' STATO, Ministero per i Beni e le Attività Culturali</dcterms:rightsHolder>
  <dcterms:isReferencedBy xml:lang="it">Scheda ICCD RA: 13-00008576</dcterms:isReferencedBy>
  <pico:materialAndTechnique xml:lang="it">ARGILLA</pico:materialAndTechnique>
  <dcterms:extent>altezza: cm 9.4</dcterms:extent>
  <dcterms:extent>diametro: cm 6.9</dcterms:extent>
  <pico:preview xsi:type="dcterms:URI">http://194.242.241.163/fedora/objects/work:46880/datastreams/MM135934/content</pico:preview>
  <dcterms:isReferencedBy xsi:type="pico:Anchor">title=visualizza il file Mets; URL=fedora/objects/work:46880/datastreams/export/content</dcterms:isReferencedBy>
</pico:record>
</metadata></record>
"""


tokens = [i.strip() for i in sample.split('\n') if len(i) > 0]

tst1 = '<dc:type xml:lang="it">BROCCHETTA MINIATURISTICA</dc:type>'

full_pat = r"<(?P<tag>[a-z0-9:\"\.:\= ]+)>(?P<text>[\w\d ]+)<?/?"
p = re.compile(full_pat, flags=re.I)
# xyz = re.findall(full_pat, tst1, flags=re.I).group('tag')
# re.search(full_pat, tst1, flags=re.I).group('tag')
# re.search(full_pat, tst1, flags=re.I).group('text')


ddict = dict()
for i, v in enumerate(tokens):
    res = p.search(v)
    try:
        ddict[i] = dict(tag=res.group('tag'), text=res.group('text'))
    except AttributeError:
        pass
    if res.group('tag'):
        ddict[i] = dict(tag=res.group('tag'), text=res.group('text'))
        res.group('text')


import pandas as pd
pd.DataFrame().from_dict(ddict, orient='index')












