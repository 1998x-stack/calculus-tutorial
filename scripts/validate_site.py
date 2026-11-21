#!/usr/bin/env python3
"""Static integrity checks for the Calculus Tutorial repository."""
import json, sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit
ROOT=Path(__file__).resolve().parents[1]
CHAPTERS=[f"{i:02d}.html" for i in range(1,29)]
UPDATED=[f"{i:02d}.html" for i in range(1,9)]
VOID={"area","base","br","col","embed","hr","img","input","link","meta","param","source","track","wbr"}
class AuditParser(HTMLParser):
 def __init__(self,path):
  super().__init__(convert_charrefs=True);self.path=path;self.ids=set();self.duplicates=[];self.links=[];self.math_count=0;self.math_errors=[];self.svg_count=0;self.svg_titles=0;self.svg_descs=0;self.h1_count=0;self.course_cards=0;self.stack=[];self.svg_depth=0;self.frac_stack=[]
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if "id" in a:
   if a["id"] in self.ids:self.duplicates.append(a["id"])
   self.ids.add(a["id"])
  if tag in {"a","link","script","img"}:
   k="href" if tag in {"a","link"} else "src"
   if a.get(k):self.links.append((tag,a[k]))
  if tag=="h1":self.h1_count+=1
  if tag=="a" and "data-chapter" in a:self.course_cards+=1
  if tag=="svg":self.svg_count+=1;self.svg_depth+=1
  if tag=="title" and self.svg_depth:self.svg_titles+=1
  if tag=="desc" and self.svg_depth:self.svg_descs+=1
  if tag=="math":
   self.math_count+=1
   if self.svg_depth:self.math_errors.append("MathML nested inside SVG")
   if not(a.get("aria-label") or a.get("aria-labelledby")):self.math_errors.append("math element missing accessible label")
  if self.frac_stack and tag!="mfrac":self.frac_stack[-1]["children"]+=1
  if tag=="mfrac":self.frac_stack.append({"children":0})
  if tag not in VOID:self.stack.append(tag)
 def handle_endtag(self,tag):
  if tag=="svg":self.svg_depth=max(0,self.svg_depth-1)
  if tag=="mfrac" and self.frac_stack:
   n=self.frac_stack.pop()["children"]
   if n!=2:self.math_errors.append(f"mfrac must have 2 direct children (found {n})")
  for i in range(len(self.stack)-1,-1,-1):
   if self.stack[i]==tag:del self.stack[i:];break
def local_issue(source,value):
 if value.startswith(("#","https://","http://","mailto:","tel:","data:","javascript:")):return None
 p=urlsplit(value);target=(source.parent/p.path).resolve()
 if not target.exists():return f"broken local reference: {value}"
 if p.fragment and target.suffix.lower() in {".html",".htm"}:
  parser=AuditParser(target);parser.feed(target.read_text(encoding="utf-8"))
  if p.fragment not in parser.ids:return f"missing fragment #{p.fragment} in {value}"
 return None
def main():
 errors=[]
 for name in CHAPTERS:
  if not(ROOT/name).is_file():errors.append(f"missing chapter: {name}")
 catalog=json.loads((ROOT/"courses.json").read_text(encoding="utf-8"))
 if catalog.get("chapterCount")!=28 or len(catalog.get("chapters",[]))!=28:errors.append("courses.json must describe exactly 28 chapters")
 for i,name in enumerate(CHAPTERS,1):
  item=catalog["chapters"][i-1]
  if item.get("num")!=f"{i:02d}" or item.get("file")!=name:errors.append(f"catalog order/path mismatch: {name}")
 home=AuditParser(ROOT/"index.html");home.feed((ROOT/"index.html").read_text(encoding="utf-8"))
 if home.course_cards!=28:errors.append(f"homepage must expose 28 static chapter links (found {home.course_cards})")
 for path in [ROOT/"index.html"]+[ROOT/x for x in CHAPTERS]:
  p=AuditParser(path);p.feed(path.read_text(encoding="utf-8"))
  if p.h1_count!=1:errors.append(f"{path.name}: expected exactly one h1, found {p.h1_count}")
  if p.duplicates:errors.append(f"{path.name}: duplicate ids {p.duplicates}")
  errors.extend(f"{path.name}: {e}" for e in p.math_errors)
  for _,link in p.links:
   issue=local_issue(path,link)
   if issue:errors.append(f"{path.name}: {issue}")
  if path.name in UPDATED:
   if p.math_count<6:errors.append(f"{path.name}: expected at least 6 semantic MathML expressions (found {p.math_count})")
   if p.svg_count<1 or p.svg_titles<1 or p.svg_descs<1:errors.append(f"{path.name}: accessible SVG title/desc required")
 for required in ["assets/css/calculus.css","assets/js/calculus.js","scripts/validate_site.py","tests/browser.spec.js",".github/workflows/validate.yml"]:
  if not(ROOT/required).is_file():errors.append(f"missing required file: {required}")
 if errors:
  print("VALIDATION FAILED")
  for e in errors:print("- "+e)
  return 1
 print("VALIDATION PASSED")
 print("- 28 chapter files and catalog entries")
 print("- 28 static homepage links")
 print("- 8 refined chapters with semantic MathML and SVG")
 print("- local references and required tooling files")
 return 0
if __name__=="__main__":sys.exit(main())
