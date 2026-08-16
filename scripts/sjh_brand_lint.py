#!/usr/bin/env python3
"""Lightweight SJH content/HTML brand linter.

Warning tool only; it does not replace human/AI brand review or institutional approval.
"""
import argparse, json, re, sys
from pathlib import Path

APPROVED_HEX = {
    '#2a57a3','#a8c947','#aeccea','#e4ebca','#fbf4a2',
    '#ffffff','#f4f6f8','#929697','#4b5563','#1f2937','#fbf8f2',
    '#e8a317','#c8102e','#2e7d32'
}
ALLOWED_FONTS = {'aptos','aptos display','arial','arial bold','helvetica','sans-serif','calibri'}

def issue(level, code, message, match=None):
    d={'level':level,'code':code,'message':message}
    if match is not None: d['match']=match
    return d

def lint(text, external=False, email_signature=False, strict_colors=False):
    out=[]
    low=text.lower()
    first_full=low.find('st. jude hospital')
    first_sjh=re.search(r'\bsjh\b', low)
    if first_sjh and (first_full < 0 or first_sjh.start() < first_full):
        out.append(issue('REQUIRED CHANGE','SJH_BEFORE_FULL_NAME','SJH appears before “St. Jude Hospital”. Introduce the full name first.'))
    if external:
        if re.search(r'\bst\.\s*jude\b(?!\s+hospital)', text, flags=re.I):
            out.append(issue('REQUIRED CHANGE','ST_JUDE_ALONE','Formal external material should not use “St. Jude” alone.'))
        if 'st. jude hospital, saint lucia' not in low:
            out.append(issue('RECOMMENDED','EXTERNAL_LONG_NAME','External/search-facing material should use “St. Jude Hospital, Saint Lucia” where applicable.'))
    for phrase,msg in {
        'clients are hereby advised':'Use direct patient/public language instead of administrative distance.',
        'failure to comply':'Use direct, respectful instructions unless legally required wording is supplied.',
        'moodboard-led':'Meta design-process language should not appear in the audience-facing artifact.'
    }.items():
        if phrase in low:
            out.append(issue('REQUIRED CHANGE','LANGUAGE',msg,phrase))
    institutional='safe, accessible and compassionate care for southern saint lucia'
    if institutional in low and not email_signature:
        out.append(issue('RECOMMENDED','EMAIL_LINE_CONTEXT','The institutional line is fixed for the approved email-signature system and is not a general-purpose campaign tagline.'))
    hexes={h.lower() for h in re.findall(r'#[0-9A-Fa-f]{6}\b', text)}
    if strict_colors:
        for h in sorted(hexes - APPROVED_HEX):
            out.append(issue('RECOMMENDED','UNAPPROVED_HEX',f'Hex colour {h} is outside the approved SJH palette. Confirm whether it is a utility/production colour or replace it.',h))
    for fam in re.findall(r'font-family\s*:\s*([^;}{]+)', text, flags=re.I):
        names=[x.strip().strip("\"'").lower() for x in fam.split(',')]
        if not any(n in ALLOWED_FONTS for n in names):
            out.append(issue('RECOMMENDED','FONT_FAMILY',f'Font stack may not include an approved SJH typeface: {fam.strip()}',fam.strip()))
    return out

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('file')
    ap.add_argument('--external',action='store_true')
    ap.add_argument('--email-signature',action='store_true')
    ap.add_argument('--strict-colors',action='store_true')
    ap.add_argument('--json',action='store_true')
    args=ap.parse_args()
    text=Path(args.file).read_text(encoding='utf-8',errors='ignore')
    items=lint(text,args.external,args.email_signature,args.strict_colors)
    if args.json:
        print(json.dumps(items,indent=2,ensure_ascii=False))
    else:
        if not items: print('PASS: no mechanical lint issues found.')
        for x in items: print(f"{x['level']}: {x['code']} — {x['message']}")
    sys.exit(1 if any(x['level'] in {'BLOCKER','REQUIRED CHANGE'} for x in items) else 0)

if __name__=='__main__':
    main()
